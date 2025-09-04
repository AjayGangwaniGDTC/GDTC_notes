#Task: Print each client's name and email. If email is missing, print "Email not provided".

import json

data = {
    "clients": [
        {"id": 1, "profile": {"name": "Kiran", "contact": {"email": "kiran@example.com"}}},
        {"id": 2, "profile": {"name": "Divya"}},
        {"id": 3, "profile": {"name": "Amit", "contact": {"email": "amit@example.com"}}}
    ]
}

#Creating an empty list to store the output
result = []
for i in data['clients']:
    #the name is inside the key profile and the profile itself is a dictionary so data is being extracted from nested dictionary
    name = i['profile']['name']
    email = i['profile'].get('contact', {}).get('email', 'Email not provided')
    result.append({'name': name, 'email': email})
    print(name, email)
    
with open("extracting_deeply_nested_fields.json","w") as file:
    json.dump(result,file,indent=2)