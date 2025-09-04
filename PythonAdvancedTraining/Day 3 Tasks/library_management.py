import json
from datetime import date, datetime

file_name = "library_records.json"
def load_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

data = load_data()

current_date = datetime.today()
lst=[]
for i in data:
    if(i['due_date']) < str(current_date) and i['returned'] == False:
        book = i['title']
        borrower_name = i['borrower']
        dt_object = datetime.strptime(i['due_date'], "%Y-%m-%d")
        difference = current_date - dt_object
        totalSeconds = difference.total_seconds()
        days = difference.days
        new_data = {
            'title': book,
            'borrower': borrower_name,
            'days_overdue': days
        }
        lst.append(new_data)
    else:
        pass

def save_data():
    with open("library_summary.json", 'w') as file:
        json.dump(lst, file, indent=2)

save_data()
