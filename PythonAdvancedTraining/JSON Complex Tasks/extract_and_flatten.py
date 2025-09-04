# Task:Extract and print each course title along with its module names and durations in a flat format like:
# Python - Basics (2 weeks)
# Python - REST APIs (1 week)
# …and so on.

import json

#loading the data from json file into data variable to read 
with open('courses.json','r') as f:
    data = json.load(f)

for i in data['courses']:
    #storing the title values in title variable
    title=i['title']
    #traversing the modules list which contains name and duration
    for item in i['modules']:
        print(f"{title} - {item['name']} ({item['duration']})")