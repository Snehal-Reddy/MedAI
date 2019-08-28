# Dr.RIP
Keep your cancer in check !!

# Installation and Requirements to run the backend:

1. Basic libraries such as numpy, matplotlib, cv2, requests, time.

2. `pip install git+https://github.com/NLPatVCU/medaCy.git` and `pip install git+https://github.com/NLPatVCU/medaCy_model_clinical_notes.git` . This installs medaCy NER which is built upon Spacy.

3. We use Microsoft Azure's Computer Vision API to extract text (both handwritten and typed). You will require a valid key which you can find in your Microsoft Azure Cognitive Services Account.

4. Add the key in the file `backend/my_azure_api.py` by setting the value of the variable `_key`. 


