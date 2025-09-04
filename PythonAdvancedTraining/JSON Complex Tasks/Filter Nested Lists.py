#Task: Print the names of attendees under 25 years old for each event

#importing the library
import json

#working data
data = {
    "events": [
        {"title": "Webinar", "attendees": [{"name": "Anil", "age": 28}, {"name": "Meera", "age": 22}]},
        {"title": "Workshop", "attendees": [{"name": "Ravi", "age": 35}, {"name": "Neha", "age": 19}]}
    ]
}


filtered_data = []
#traversing through events list in the data
for i in data["events"]:
    #traversing through attendees list inside the events list
    for attendee in i['attendees']:
        if attendee['age'] > 25:
            filtered_data.append({'name': attendee['name'], 'age': attendee['age']})

with open("filter.json","w") as f:
    json.dump(filtered_data, f, indent=2)