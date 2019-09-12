from flask import Flask, request, render_template, jsonify
# from backend.my_azure_api import *
from backend.medicine_extractor import *
from backend.symptoms import *
import json

b,c,d = None, None, None

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("main.html")

@app.route('/image', methods = ['POST'])
def solve():
	img = request.files.get('file', '')
	annotation = drug_extraction(img)
	print(type(annotation))
	return jsonify(annotation.get_entity_annotations(return_dictionary = True))

@app.route('/disease', methods = ['POST'])
def search():
	global b, c, d
	data = request.get_json()['symptoms']
	a,b,c,d = solver(data)
	return jsonify(a)
	# return solver(data)

@app.route('/find', methods = ['POST'])
def super():
	data = request.get_json()['symptoms']
	print(data)
	#return "hellll OOOOOO"
	return react_out(data, b, c, d)

if __name__ == '__main__':
   app.run(debug = True, port=3000)