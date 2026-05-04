# MINI PROJECT 4 - ORDER ANALYZER

# Description:
# This program analyzes customer order data

# Features:
# - Calculates total sales
# - Calculates the average order price
# - Filters orders above a certain price
# - Counts how many times each item was ordered
# - Finds the most popular item
# - Formats prices with currency symbols (€)
# - Allows user input for new orders



orders = [
    {"item": "latte", "price": 4.5},
    {"item": "americano", "price": 3.0},
    {"item": "latte", "price": 4.5},
    {"item": "cake", "price": 5.0},
    {"item": "matcha latte", "price": 5.0},
    {"item": "tea", "price": 2.5}
]


# ADD USER INPUT
while True:
    add_order = input("Would you like to add new orders? (y/n): ")

    if add_order.lower() == "n":
        break
    elif add_order.lower() == "y":
        item = input("Enter item name: ")
        price = float(input("Enter price: "))

        orders.append({"item": item, "price": price})
        print("Order added!")
    else:
        print("Please enter y or n")


# TOTAL SALES
total_sales = 0
for order in orders:
    total_sales += order["price"]

print(f"\nTotal sales: €{total_sales:.2f}")


# AVERAGE PRICE
average_price = total_sales / len(orders)
print(f"\nAverage price: €{average_price:.2f}")


# FILTER EXPENSIVE ORDERS
print("\nExpensive orders:")
for order in orders:
    if order["price"] >= 4.0:
        print(f"- {order}")


# ITEM COUNTING
item_counts = {}

for order in orders:
    item_name = order["item"]

    if item_name in item_counts:
        item_counts[item_name] += 1
    else:
        item_counts[item_name] = 1

print(f"\nItem counts: {item_counts}")


# FIND THE MOST POPULAR ITEM
most_popular = ""
max_count = 0

for menu_name in item_counts:
    if item_counts[menu_name] > max_count:
        max_count = item_counts[menu_name]
        most_popular = menu_name

print(f"\nMost popular item: {most_popular}")

