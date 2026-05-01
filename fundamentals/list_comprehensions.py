# =========================
# LIST COMPREHENSIONS
# =========================


prices = [10, 38, 40, 58, 62]

# BASIC LIST COMPREHENSION VS LOOP
halved_lc = [price/2 for price in prices]
print(halved_lc)


halved_loop = []
for price in prices:
    half_price = price / 2
    halved_loop.append(half_price)

print(halved_loop)


# WITH CONDITION
even_prices = [price for price in prices if price % 2 == 0]
print(even_prices)

mid_prices = [price for price in prices if price > 30 and price < 50]
print(mid_prices)


# WITH IF-ELSE
price_labels = ["high" if price >= 50 else "low" for price in prices]
print(price_labels)


# WITH FUNCTIONS
def halve(num):
    return num / 2

halved = [halve(price) for price in prices]
print(halved)


# STRING TRANSFORMATION
names = ["chloe", "sarah", "james"]

capitalized_names = [name.capitalize() for name in names]
print(capitalized_names)


authors = ["Virginia Woolf", "John Steinbeck"]  

def add_comma(name):
    parts = name.split(" ")
    return parts[1] + ", " + parts[0]   

authors_update = [add_comma(name) for name in authors]
print(authors_update)


# FILTERING WITH FUNCTION
words = ["apple", "alligator", "abracadabra", "avatar"]

def has_double_a(word):
    count = word.count("a")
    return count == 2 

double_a = [word for word in words if has_double_a(word)]
print(double_a)


# BOOLEAN TRANSFORMATION
answers = [True, False, False]

opposite_loop = []
for answer in answers:
    opposite_loop.append(not answer)

print(opposite_loop)


opposite_lc = [not answer for answer in answers]
print(opposite_lc)