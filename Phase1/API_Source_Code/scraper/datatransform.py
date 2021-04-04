import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
import json 
import pycountry 
from datetime import datetime
with open('./transformed.json') as f:
  data = json.load(f)

#print(pycountry.countries.search_fuzzy('England')[0].name)

#newdata = {}
newdata = {}
dates = []
countries = []
for a in data:
    #print(a)
    # if a['location'] != "unknown" and a['disease'] != "unknown":
    #     newdata.append(a)
    try:
        country = pycountry.countries.search_fuzzy(a['location'])
        
        if  country != None:
            #print(country)
            report = { 
                "id": country[0].alpha_2,
                "disease": a['disease']
            }
            x = datetime.strptime(a['date'], '%B %d, %Y')
            formatted = x.strftime("%Y-%m-%d")
            
            if (not formatted in newdata ):
                newdata[formatted] = [report]
                dates.append(formatted)
                if not country[0].alpha_2 in countries:
                    countries.append(country[0].alpha_2)

            else:
                newdata[formatted].append(report)
            #print(formatted)
    except LookupError:
        continue
    

#print(sorted(dates))
readydata = []
for date in sorted(dates):
    day = {}
    day['date'] = date
    day['list'] = newdata[date]
    readydata.append(day)
for report in readydata[-1]['list']:
    countries.remove(report['id'])
for country in countries:
    readydata[-1]['list'].append({
        "id": country,
        "disease": "Z"
    })
    
with open('transformed1.json', 'w') as json_file:
  json.dump(readydata, json_file)