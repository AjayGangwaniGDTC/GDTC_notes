import json
from collections import defaultdict
from operator import itemgetter

file_name = 'feedback_data.json'
def load_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

grouped_data = defaultdict(list)
data = load_data()
for i in data:
    group_key = (i['course'], i['instructor'])
    grouped_data[group_key].append(i['rating'])
    print(grouped_data)

new_data = []
for k,v in grouped_data.items():
    total = sum(item for item in v)
    average = total/len(v)
    data1 = {
        'course': k[0],
        'instructor': k[1],
        'average_rating': average
    }
    new_data.append(data1)

sorted_new_data = sorted(new_data, key=itemgetter('average_rating'), reverse=True)
def save_data():
    with open("feedback_summary.json", 'w') as file:
        json.dump(sorted_new_data, file, indent=2)

save_data()