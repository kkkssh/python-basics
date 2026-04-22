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
player_scores = {
    "Ann": 13,
    "Michael": 20,
    "Ava": 34
}

player_scores["Ann"] = 23   
print(player_scores)


# ADDING NEW KEY-VALUE PAIRS
player_scores["Chloe"] = 35
print(player_scores)


# USING FOR LOOP WITH DICTIONARY
for player in player_scores:
    score = player_scores[player]
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
