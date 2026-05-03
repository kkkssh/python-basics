# =========================
# DICTIONARIES
# =========================

# Note: This file is for practicing dictionary operations in Python,
# including creating, updating, accessing, and deleting key-value pairs.


# DICTIONARY: a collection of key-value pairs
locations = {
    "headquarters": "New York", 
    "flagship": "Paris"
} 
# keys - unique identifiers (can be string, tuple, boolean, or number) 
# e.g. "headquarters", "flagship"

# values - data associated with each key  
# e.g. "New York", "Paris" 

print(locations)


# ACCESSING VALUES
car_data = {
    "brand": "Cadillac",
    "year": 1960,
    "restoration": ["1990", "2018"],
    "rented": False
}

print(car_data)
print(car_data["brand"])


# UPDATING VALUES
player_scores_basic  = {
    "Ann": 13,
    "Michael": 20,
    "Ava": 34
}

player_scores_basic ["Ann"] = 23   
print(player_scores_basic )


# ADDING NEW KEY-VALUE PAIRS
player_scores_basic ["Chloe"] = 35
print(player_scores_basic )


# USING FOR LOOP WITH DICTIONARY
for player in player_scores_basic :
    score = player_scores_basic [player]
    print(player, score)   


# CHECKING IF A DICTIONARY CONTAINS A CERTAIN KEY
personal_data = {
    "name": "Mac Miller",
    "phone": "0047865791"
}

print("name" in personal_data)  # True
print("address" in personal_data)  # False


# REMOVING KEY-VALUE PAIRS
stock = {
    "dresses": 25,
    "t-shirts": 50,
    "jeans": 1
}

stock.pop("jeans")
# stock.pop("caps")   # would raise KeyError if key does not exist
print(stock)


# SAFE ACCESS (CHECK BEFORE USING KEY)
if "t-shirts" in stock:
    print(stock["t-shirts"])  # safely accessing value

if "dresses" in stock:
    stock.pop("dresses")  # safely removing key

print(stock)


# GET METHOD (SAFE ACCESS)

# get() allows safe access to dictionary values
# it returns None (or a default value) if the key does not exist

user = {
    "name": "Chloe",
    "age": 33
}

print(user.get("name"))  # Chloe
print(user.get("email"))  # None (no error)
print(user.get("email", "Not found"))  # default value if key is missing


# LOOPING WITH items()

# items() returns key-value pairs as tuples
# useful when looping through both key and value

player_scores_loop  = {
    "Ann": 23,
    "Michael": 20,
    "Ava": 34
}

for player, score in player_scores_loop .items():
    print(player, score)


# KEYS AND VALUES
print(player_scores_loop .keys())     # keys() returns all keys
print(player_scores_loop .values())   # values() returns all values


# NESTED DICTIONARIES

# a dictionary can contain other dictionaries as values
# useful for representing structured data

users = {
    "user1": {
        "name": "Chloe",
        "age": 33
    },
    "user2": {
        "name": "James",
        "age": 28
    }
}

# accessing nested values
print(users["user1"]["name"])  # Chloe

# looping through nested dictionaries
for user_id, info in users.items():
    print(user_id, info["name"], info["age"])

# safe access in nested dictionary (recommended in real-world scenarios)
for user_id, info in users.items():
    print(user_id, info.get("name"), info.get("age"))


# LIST OF DICTIONARIES

# commonly used structure for real-world data
# each dictionary represents one item

products = [
    {"name": "Latte", "price": 4.5},
    {"name": "Americano", "price": 3.5}
]

# accessing data
print(products[0]["name"])  # Latte


# looping through list of dictionaries
for product in products:
    print(product["name"], product["price"])


# DICTIONARY WITH LIST VALUES

# one key can store multiple values

orders = {
    "table1": ["pizza", "cola"],
    "table2": ["pasta"]
}

for table, items in orders.items():
    print(table, items)