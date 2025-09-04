import json

file_name = "employee_directory.json"
def load_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

data = load_data()
print(data)
lst=[]
for i in data:
    if(i["role"] == "Team Lead"):
        lst.append(i)
print(lst)

lst1=[]
for i in lst:
    i['team_size'] = len(i['team'])
    lst1.append(i)

def save_data():
    with open("hr_digital_shift.json", 'w') as file:
        json.dump(lst1, file, indent=2)
print(lst1)
save_data()