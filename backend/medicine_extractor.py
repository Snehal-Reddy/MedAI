from medacy.ner.model import Model
from my_azure_api import *


model = Model.load_external('medacy_model_clinical_notes')
all_text_as_list = text_from_image()
all_text = ""
for line in all_text_as_list:
	all_text += line + " "
print(all_text)
annotation = model.predict(all_text)
print(annotation)