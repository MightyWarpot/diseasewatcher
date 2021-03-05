import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
import spacy
import scispacy
import json 
from spacy import displacy
from collections import Counter
import en_core_web_sm

nlp = en_core_web_sm.load()
nlp1 = spacy.load("en_core_web_sm")
keywords = ["covid-19", "zika", "mers", "salmonella", "legionnaire", "measles", "anthrax", "botulism", "plague", "smallpox",
    "pox", "tularemia", "junin fever", "machupo fever", "guanarito fever", "chapare fever", "lassa fever", "lujo fever", "hantavirus",
    "rift valley fever", "crimean-congo hemorrhagic fever", "dengue", "ebola", "marburg", "unknown", "other", "anthrax cutaneous", "anthrax gastrointestinous", 
    "anthrax inhalation", "brucellosis", "chikungunya", "cholera", "cryptococcosis", "cryptosporidiosis", "diphteria", "ebola haemorrhagic fever", 
    "ehec", "e.coli", "enterovirus 71 infection", "influenza a/h5n1", "influenza a/h7n9", "influenza a/h9n2", "influenza a/h1n1", "influenza a/h1n2", 
    "influenza a/h3n5", "influenza a/h3n2", "influenza a/h2n2", "hand, foot and mouth disease", "hepatitis a", "hepatitis b", "hepatitis c", "hepatitis d", 
    "hepatitis e", "histoplasmosis", "hiv", "aids", "malaria", "mers-cov", "mumps", "nipah virus", "norovirus infection", "pertussis", "pneumococcus pneumonia", 
    "poliomyelitis", "q fever", "rabies", "rotavirus infection", "rubella", "salmonellosis", "sars", "shigellosis", "staphylococcal enterotoxin b", 
    "thypoid fever", "tuberculosis", "vaccinia", "cowpox", "varicella", "west nile virus", "yellow fever", "yersiniosis", "listeriosis", "legionares", 
    "listeriosis", "monkeypox", "2019 nCoV"]


with open('./articles.json') as f:
  data = json.load(f)
n = 0
for a in data[0:10]:
    if a['title'] == None:
        data.remove(a)
    else:
        print(a['title'])
        doc = nlp(a['title'])
        #doc1 = nlp1(a['title'])
        #print(doc1.ents)
       
        loc = []
        a['location'] = 'unknown'
        for X in doc.ents:
            print(X.text, X.label_)
            if X.label_ == 'GPE':
                a['location'] = X.text
                loc.append(X.text.lower())
                break 
        print(loc)
    n += 1
    
    # for token in doc1:
    #     if token.tag_ == 'NNP' or token.tag_ == "NNPS":
    #         print(token.text, token.tag_)
    #         print(token.text)
    #         for place in loc:
    #             if (token.text.lower() not in place and token.text.lower() != place):
    #                 print(token.text)
    #                 break

           # print([(X, X.text, X.label_) for X in nlp(token.text).ents])


with open('taggedata.json', 'w') as json_file:
  json.dump(data, json_file)