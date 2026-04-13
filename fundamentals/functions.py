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

# CREATING PARAMETER
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