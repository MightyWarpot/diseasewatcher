import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
import spacy
import scispacy
import json 
from spacy import displacy
from collections import Counter
import en_core_web_sm
import pycountry 
nlp = en_core_web_sm.load()
nlp1 = spacy.load("en_ner_bc5cdr_md")
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

newdata = []
with open('./chart.json') as f:
  data = json.load(f)
#print(len(data[20:22]))
i = 0
for a in data:
    if a['title'] == None or a['region'] == 'Research':
        i += 1
        
        
    else:
        #parse first line of article
        #print(a['title'])
        #print(a)
        geo1 = nlp(a['title'])
        dis1 = nlp1(a['title'])
        
        a['disease'] = 'unknown'
        for X in dis1.ents:
            #print(X.text, X.label_)
            if (X.label_ == 'DISEASE' or X.text == 'COVID-19')and 'death' not in X.text:
                a['disease'] = X.text
                
                break 
        if (a['disease'] == 'unknown' and len(a['body']) > 1):
            dis2 = nlp1(a['body'][1])
            for X in dis2.ents:
                #print(X.text, X.label_)
                if (X.label_ == 'DISEASE' or X.text == 'COVID-19')and 'death' not in X.text:
                    a['disease'] = X.text
                    
                    break 
        if (a['disease'] == 'unknown' and len(a['body']) > 2):
            dis2 = nlp1(a['body'][2])
            for X in dis2.ents:
                #print(X.text, X.label_)
                if (X.label_ == 'DISEASE' or X.text == 'COVID-19')and 'death' not in X.text:
                    a['disease'] = X.text
                    
                    break 
       
        loc = []
        a['location'] = 'unknown'
        #print(a['location'])
        for X in geo1.ents:
            #print(X.text, X.label_)
            if X.label_ == 'GPE':
                a['location'] = X.text
                loc.append(X.text.lower())
                break 
        
        #if location was not able to be extracted from title , try first line of article
        if (a['location'] == 'unknown' and len(a['body']) > 1):
            
            doc1 = nlp(a['body'][1])
            for X in doc1.ents:
              #  print(X.text, X.label_)
                if X.label_ == 'GPE':
                    a['location'] = X.text
                    loc.append(X.text.lower())
                    break 
       # print(loc)
        #print(a['location'])
        try:
          country = pycountry.countries.search_fuzzy(a['location'])
          
          if  country != None:
              a['location'] = country[0].name
        except LookupError:
            continue
            

print(i)
with open('taggedchart.json', 'w') as json_file:
  json.dump(data, json_file)