import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
import json 
import pycountry 
from datetime import datetime
with open('./chart.json') as f:
  data = json.load(f)
newdata = []
for a in data:
    x = datetime.strptime("January 1, 2021", '%B %d, %Y')
    x1 = datetime.strptime(a['date'], '%B %d, %Y')
    if (x1 >= x):
        newdata.append(a)

with open('./chartmidyear1.json') as f1:
  midyeardata = json.load(f1)

for a in midyeardata:
    newdata.append(a)

with open('no2020.json', 'w') as json_file:
  json.dump(newdata, json_file)