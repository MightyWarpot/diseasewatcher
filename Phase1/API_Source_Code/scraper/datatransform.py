import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
import json 
import pycountry 
from datetime import datetime, timedelta
with open('./taggedchart.json') as f:
  data = json.load(f)

#print(pycountry.countries.search_fuzzy('England')[0].name)

#newdata = {}
newdata = []
dates = []
countries = []
final = {}
i = 0
for a in data:
    if a['location'] != "unknown" and a['disease'] != "unknown":
        newdata.append(a)
        i += 1

print(i)
j = 0
for a in newdata:
    
    try:
        country = pycountry.countries.search_fuzzy(a['location'])
        
        if  country != None:
            j += 1
            #print(country)
            report = { 
                "id": country[0].alpha_2,
                "disease": a['disease']
            }
            x = datetime.strptime(a['date'], '%B %d, %Y')
            formatted = x.strftime("%Y-%m-%d")
            
            if (not formatted in final ):
                final[formatted] = [report]
                dates.append(formatted)
                if not country[0].alpha_2 in countries:
                    countries.append(country[0].alpha_2)

            else:
                final[formatted].append(report)
            #print(formatted)
    except LookupError:
        continue

print(j) 

#print(sorted(dates))
readydata = []
for date in sorted(dates):
    day = {}
    day['date'] = date
    day['list'] = final[date]
    readydata.append(day)
lastday = {
    "date": (datetime.strptime(readydata[-1]['date'], "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d"),
    "list": []
}
readydata.append(lastday)
for country in countries:
    
    readydata[-1]['list'].append({
        "id": country,
        "disease": "Z"
    })
    
with open('transformed1.json', 'w') as json_file:
  json.dump(readydata, json_file)