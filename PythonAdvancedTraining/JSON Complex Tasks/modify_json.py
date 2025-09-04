# Task:For each order, calculate the total amount (sum of qty × price for all items) and add it as a new key total_amount. Save the modified data back to a new JSON file.

import json

with open("orders.json","r") as f:
    data = json.load(f)

orders = []
for i in data["orders"]:
    order_id=i['order_id']
    total_amount = sum(item['qty'] * item['price'] for item in i['items']) #calculating the sum of the qty*price for each order
    orders.append({'order_id': order_id, 'total_amount': total_amount})

with open("orders_summary.json","w") as file:
    json.dump(orders,file,indent=2)
    