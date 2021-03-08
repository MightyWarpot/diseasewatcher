import re


temp = 'helloworld'


if re.search("\w", temp) != None:
    print("Hello")

combined =[{'location': 'China', 'disease': 'COVID-19'}]


# re.split("\s", txt)
# location =

# if temp == re.search("^The.*Spain$", txt)
for entry in combined:
    if (re.search("\w", entry['location'])):
        print("YoYoYo")
    # if (entry['location'] )
    # if (entry['location'] == location and
    #         entry['disease'] == disease):
    #     combined_filtered.append(entry)
