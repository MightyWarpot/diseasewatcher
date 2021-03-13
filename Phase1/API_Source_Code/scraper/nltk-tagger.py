import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
import nltk
import json
import numpy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


ex = 'China reports 3 human H9N2 avian influenza cases '
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    sent = nltk.ne_chunk(sent)
    return sent
with open('./articles.json') as f:
  data = json.load(f)



for a in data[0:5]:
    print(a['title'][1])
    print(preprocess(a['body'][1]))