# #Task: Print total stock available in each category.

import json

stock = []
data = {
    "inventory": [
        {"category": "Books", "items": [{"title": "Python 101", "stock": 12}, {"title": "Flask Guide", "stock": 5}]},
        {"category": "Electronics", "items": [{"title": "Mouse", "stock": 20}, {"title": "Keyboard", "stock": 15}]}
    ]
}

for i in data["inventory"]:
    category_name = i['category']
    total_stock = sum(item['stock'] for item in i['items']) #calculating the sum of key:stock in a list of items
    stock.append({'category': category_name, 'total_stock': total_stock})

print(stock)

with open("grouping_and_summarise.json","w") as file:
    json.dump(stock,file,indent=2)
