# =========================
# FUNCTIONS
# =========================

# FUNCTIONS: reusing code
# Function names usually start with verbs so you can easily understand what they do

# DEF
def greet_user():
    print("Good morning Chloe")
    print("Welcome back")

greet_user()

def show_user_status():
    status = "Active"
    username = "Ron"
    print(f"{username} is {status}")

show_user_status()


# CREATING PARAMETERS
def greet(name):    # name = parameter
    print(f"Hello, {name}")

greet("April") 
greet("Leslie")

def display_half(number):
    half = number / 2
    print(half)

display_half(10)


# RETURNING VALUES
def age_label(age):
    return f"User age: {age}"        # if we don't return a value, we get None

result = age_label(22)
print(result)

def give_me_ten():
    return 10

print(give_me_ten())

def half_twice(number):
    half = number / 2
    half_again = half / 2
    return half_again

result = half_twice(12)
print(result)

def is_freezing(temperature):
    return temperature < 0

freezing = is_freezing(-3)
print(freezing)      # True

def is_adult(age):
    return age >= 18

print(is_adult(20))  # True


# MULTIPLE PARAMETERS
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

def display_full_name(first, last):
    print(first + " " + last)

display_full_name("Chloe", "Kim")

def show_winners(first, second, third):
    print("1st: " + first)
    print("2nd: " + second)
    print("3rd: " + third)

show_winners("Kim", "Lee", "Ava")

def create_email(name, year):
    return name + year + "@gmail.com"

email = create_email("jo", "2026")
print(email)


# VARIABLE SCOPE
def apply_discount(price):
    discount = 20    # local scope
    return price - discount

final_price = apply_discount(50)
print(final_price)

rent = 1000   # global scope
def calculate_spendings(groceries):
    print(f"Total: {rent + groceries}")

print(f"Rent: {rent}")
calculate_spendings(300)


# FUNCTIONS WITH CONDITIONALS
def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")

add_shipping(45)
add_shipping(200)

def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"Unknown: {operator}")

calculate("-", 30, 10)

def show_progress(points):
    if points > 1000:
        print("New highest score!")
    print("Ready for the next level?")

show_progress(900)


# FUNCTIONS WITH LISTS
def is_multiplayer(players):
    print(len(players) == 2)

players = ["Amy", "Jay"]
is_multiplayer(players)  # True

def display_programme(movies):
    print(f"Airing tonight: {movies}")

movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def count_passengers(passengers):
    print(len(passengers))

passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)

def is_booked(passengers):
    print(len(passengers) > 4)

passengers = ["June", "Sam", "Lee"]
is_booked(passengers)   # False

def get_winner(top_players):
    winner = top_players[0]
    print(f"Game winner: {winner}")

top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)    # Game winner: Jay

def update_first_place(leaderboard, player):
    leaderboard[0] = player
    return leaderboard

leaderboard = ["Jay", "Meg", "Cy"]
leaderboard = update_first_place(leaderboard, "Lena")
print(leaderboard)  # ['Lena', 'Meg', 'Cy']

def is_valid(parts):
    print(len(parts) == 2)

email = "laurie@gmail.com"
user_and_domain = email.split("@")
is_valid(user_and_domain)   # True


# FUNCTIONS WITH LOOPS
def onboard_passengers_while(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1

onboard_passengers_while(4)

def onboard_passengers_for(bookings):
    for i in range(1, bookings + 1):
        print(f"Passenger {i} on board")

onboard_passengers_for(4)

def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")

do_countdown(3)

def display_progress(total_files):
    for i in range(total_files):    # how many times a loop runs
        print(f"Downloading file {i + 1} out of {total_files}")

display_progress(3)

def display_halved_prices(cart):
    for price in cart:
        print(f"New price: {price / 2}")

cart_list = [5, 20, 8]
display_halved_prices(cart_list)

def get_halved_prices(cart):
    new_prices = []
    for price in cart:
        new_prices.append(price / 2)
    return new_prices

cart_list = [5, 20, 8]
print(get_halved_prices(cart_list))


# FUNCTIONS WITH TUPLES
# returns multiple values as a tuple
def get_user():
    return ("Chloe", 33)

user = get_user()
print(user)


# FUNCTIONS WITH DICTIONARIES
def get_score(scores, player):
    if player in scores:
        return scores[player]
    return "Player not found"

player_scores = {"Ann": 23, "Michael": 20}
print(get_score(player_scores, "Ann"))