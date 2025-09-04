import json
from collections import defaultdict

file_name = "registrations.json"
def load_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

data = load_data()
print(data)
unique_data = list({json.dumps(item) for item in data})
print(unique_data)
unique_data_decode = [json.loads(item) for item in unique_data]
print(unique_data_decode)

slots_count = defaultdict(int)
for item in unique_data_decode:
    slot= item.get("slot")
    print(slot)
    if slot:
        slots_count[slot] += 1

def save_data():
    with open("unique_registrations.json", 'w') as file:
        json.dump(unique_data_decode, file, indent=2)
    with open("slot_counts.json", 'w') as file:
        json.dump(slots_count, file, indent=2)

save_data()