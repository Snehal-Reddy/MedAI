from medacy.ner.model import Model
import time 
import requests
import cv2
import operator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D 

_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/RecognizeText'
_key = "ca1f6160084846acbcab166cd2719365"
  #Here you have to paste your primary key
_maxNumRetries = 10

def processRequest( json, data, headers, params ):
    retries = 0
    result = None

    while True:
        response = requests.post(_url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429:
            print( "Message: %s" % ( response.json() ) )
            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break
        elif response.status_code == 202:
            result = response.headers['Operation-Location']
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json() ) )
        break
        
    return result

def getOCRTextResult( operationLocation, headers ):
    retries = 0
    result = None

    while True:
        response = requests.get(operationLocation, json=None, data=None, headers=headers, params=None)
        if response.status_code == 429:
            print("Message: %s" % (response.json()))
            if retries <= _maxNumRetries:
                time.sleep(1)
                retries += 1
                continue
            else:
                print('Error: failed after retrying!')
                break
        elif response.status_code == 200:
            result = response.json()
        else:
            print("Error code: %d" % (response.status_code))
            print("Message: %s" % (response.json()))
        break

    return result

def showResultinFile(result):
	lines = result['recognitionResult']['lines']
	for i in range(len(lines)):
		words = lines[i]['words']
		s = ""
		for word in words:
			s += word['text'] + " "
		print(s)

def showResultOnImage( result, img ):
    img = img[:, :, (2, 1, 0)]
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(img, aspect='equal')

    lines = result['recognitionResult']['lines']

    for i in range(len(lines)):
        words = lines[i]['words']
        for j in range(len(words)):
            tl = (words[j]['boundingBox'][0], words[j]['boundingBox'][1])
            tr = (words[j]['boundingBox'][2], words[j]['boundingBox'][3])
            br = (words[j]['boundingBox'][4], words[j]['boundingBox'][5])
            bl = (words[j]['boundingBox'][6], words[j]['boundingBox'][7])
            text = words[j]['text']
            x = [tl[0], tr[0], tr[0], br[0], br[0], bl[0], bl[0], tl[0]]
            y = [tl[1], tr[1], tr[1], br[1], br[1], bl[1], bl[1], tl[1]]
            line = Line2D(x, y, linewidth=3.5, color='red')
            ax.add_line(line)
            ax.text(tl[0], tl[1] - 2, '{:s}'.format(text),
            bbox=dict(facecolor='blue', alpha=0.5),
            fontsize=14, color='white')

    plt.axis('off')
    plt.tight_layout()
    plt.draw()
    plt.show()

def text_from_image(img):

    # pathToFileInDisk = r'/home/thebhatman/Downloads/69107836_1116226275432174_5239825646892351488_n.jpg'
    # with open(pathToFileInDisk, 'rb') as f:
    #     data = f.read()
    data = img.read()
    params = {'mode' : 'Handwritten'}

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = _key
    headers['Content-Type'] = 'application/octet-stream'

    json = None

    operationLocation = processRequest(json, data, headers, params)

    result = None
    if (operationLocation != None):
        headers = {}
        headers['Ocp-Apim-Subscription-Key'] = _key
        while True:
            time.sleep(1)
            result = getOCRTextResult(operationLocation, headers)
            if result['status'] == 'Succeeded' or result['status'] == 'Failed':
                break

    text_file = []
    if result is not None and result['status'] == 'Succeeded':
        data8uint = np.fromstring(data, np.uint8)
        img = cv2.cvtColor(cv2.imdecode(data8uint, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
        showResultinFile(result)
        # showResultOnImage(result, img)
        all_text = result['recognitionResult']['lines']
        for i in range(len(all_text)):
            one_line = all_text[i]['words']
            each_line_as_string = ""
            for word in one_line:
                each_line_as_string += word['text'] + " "
            text_file.append(each_line_as_string)
    return text_file


def drug_extraction(img):
	model = Model.load_external('medacy_model_clinical_notes')
	all_text_as_list = text_from_image(img)
	all_text = ""
	for line in all_text_as_list:
		all_text += line + " "
	print(all_text)
	annotation = model.predict(all_text)
	print(annotation)
	return annotation

if __name__ == "__main__":
	drug_extraction(img)