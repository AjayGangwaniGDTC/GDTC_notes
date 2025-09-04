import json

file_name = "portfolio.json"
def load_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

data = load_data()
lst = []
for i in data:
    total_invested = i['quantity'] * i['purchase_price']
    current_value = i['quantity'] * i['current_price']
    if(i['purchase_price'] < i['current_price']):
        status = 'Gain'
        percent_change = (current_value - total_invested) / total_invested * 100
    else:
        status = 'Loss'
        percent_change = (current_value - total_invested) / total_invested * 100

    new_data = {
        'total_invested': total_invested,
        'current_value': current_value,
        'status': status,
        'gain_or_loss_percent': round(percent_change, 2)
    }
    lst.append(new_data)

def save_data():
    with open("portfolio_summary.json", 'w') as file:
        json.dump(lst, file, indent=2)

save_data()