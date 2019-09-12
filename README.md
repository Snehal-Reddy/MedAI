# MEDAI

[![Built with ❤](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com/#)

An intelligent and responsible medical app.

# Installation and Requirements to run the backend:

1. Basic libraries such as numpy, matplotlib, cv2, requests, time, flask.

2. `pip install git+https://github.com/NLPatVCU/medaCy.git` and `pip install git+https://github.com/NLPatVCU/medaCy_model_clinical_notes.git` . This installs medaCy NER which is built upon Spacy.

3. We use Microsoft Azure's Computer Vision API to extract text (both handwritten and typed). You will require a valid key which you can find in your Microsoft Azure Cognitive Services Account.

4. Add the key in the file `backend/my_azure_api.py` by setting the value of the variable `_key`. 

# Results 

## Doctor Prescription Parser - 
![alt_text] (https://github.com/Snehal-Reddy/MedAI/blob/master/static/prescription.jpg)

![alt_text] (https://github.com/Snehal-Reddy/MedAI/blob/master/static/Screenshot%20from%202019-09-12%2022-52-18.png)

## Interctive Symptom Checker -

![alt_text] (https://github.com/Snehal-Reddy/MedAI/blob/master/static/Screenshot%20from%202019-09-12%2022-23-24.png)
![alt_text] (https://github.com/Snehal-Reddy/MedAI/blob/master/static/Screenshot%20from%202019-09-12%2022-27-07.png)
![alt_text] (https://github.com/Snehal-Reddy/MedAI/blob/master/static/Screenshot%20from%202019-09-12%2022-27-18.png)







