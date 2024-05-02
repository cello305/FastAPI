# import spacy
# from spacy import displacy
# from .main import getBody


# # from ..app.main import db

# NER = spacy.load("en_core_web_sm")
# raw_text = getBody
# text1 = NER(raw_text)
# for word in text1.ents:
#     print(word.text,word.label_)

# import requests
# import spacy

# NER = spacy.load("en_core_web_sm")

# def fetch_and_process_body(id):
#     url = f"http://localhost:8000/{1}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         raw_text = response.text
#         doc = NER(raw_text)
#         for ent in doc.ents:
#             processed = print(ent.text, ent.label_)
#     else:
#         print(f"Failed to fetch data: {response.status_code} - {response.text}")

# def save_to_db(processed):
#     url = f"http://localhost:8000/add"
#     response = requests.post(url, data={'body': processed})
#     if response.status_code == 200:
#         print("Data saved successfully")
#     else:
#         print(f"Failed to save data: {response.status_code} - {response.text}")

# if __name__ == "__main__":
#     body_id = 1 
#     processed = fetch_and_process_body(body_id)
#     save_to_db(processed)

import requests
import spacy

NER = spacy.load("en_core_web_sm")

def fetch_and_process_body(id):
    url = f"http://localhost:8000/{id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        raw_text = response.json()  # Assuming the body is returned directly
        doc = NER(raw_text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

# def save_to_db(processed):
#     if processed:
#         # for text, label in processed:
#         url = "http://localhost:8000/add"
#         response = requests.post(url, processed)
#         if response.status_code == 201:
#             print("Data saved successfully")
#         else:
#             print(f"Failed to save data: {response.status_code} - {response.text}")

if __name__ == "__main__":
    body_id = 1 
    processed = fetch_and_process_body(body_id)
    print(processed)
    # save_to_db(processed)
