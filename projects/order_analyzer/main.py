# MINI PROJECT 4 - ORDER ANALYZER

# Description:
# This program analyzes customer order data

# Features:
# - Calculates total sales
# - Calculates the average order price
# - Filters orders above a certain price
# - Counts how many times each item was ordered



orders = [
    {"item": "latte", "price": 4.5},
    {"item": "americano", "price": 3.0},
    {"item": "latte", "price": 4.5},
    {"item": "cake", "price": 5.0},
    {"item": "matcha latte", "price": 5.0},
    {"item": "tea", "price": 2.5}
]

# TOTAL SALES
total_sales = 0
for order in orders:
    total_sales += order["price"]

print(f"\nTotal sales: {total_sales}")


# AVERAGE PRICE
average_price = total_sales / len(orders)
print(f"\nAverage price: {average_price:.2f}")


# FILTER EXPENSIVE ORDERS
print("\nExpensive orders:")
for order in orders:
    if order["price"] >= 4.0:
        print(f"- {order}")


# ITEM COUNTING
item_counts = {}

for order in orders:
    item = order["item"]

    if item in item_counts:
        item_counts[item] += 1
    else:
        item_counts[item] = 1

print(f"\nItem counts: {item_counts}")
