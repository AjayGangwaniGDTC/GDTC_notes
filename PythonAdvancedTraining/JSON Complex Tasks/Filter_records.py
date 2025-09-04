# Task:Read the JSON file and print the names of employees in the Engineering department with a salary above ₹70,000.

import json

#loading the data from other file for reading
with open("employees.json","r") as f:
    data = json.load(f)

#creating empty list for the result
summary_list=[]
for i in data['employees']:
    #checking the condition
    if i['department'] == 'Engineering' and i['salary'] > 70000:
        summary_list.append({'id':i['id'], 'name': i['name'], 'salary':i['salary']})

with open('employees_summary.json','w') as file:
    json.dump(summary_list,file,indent=2)

print(summary_list)