# MEDAI

[![Built with ❤](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com/#)

An intelligent and responsible medical app.

# Installation and Requirements to run the backend:

1. Basic libraries such as numpy, matplotlib, cv2, requests, time, flask.

2. `pip install git+https://github.com/NLPatVCU/medaCy.git` and `pip install git+https://github.com/NLPatVCU/medaCy_model_clinical_notes.git` . This installs medaCy NER which is built upon Spacy.

3. We use Google console Computer Vision API to extract text (both handwritten and typed). You will require a valid key which you can find in your Google console Cognitive Services Account.

4. Add the key in the file `backend/my_google_api.py` by setting the value of the variable `_key`.
