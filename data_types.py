# =========================
# DATA TYPES
# =========================

# STRING : characters between quotes " "
country = "UK"

# STRING CONCATENATION (expression)
first_name = "Sanghee"
last_name = "Kim"

# using variables
full_name = first_name + " " + last_name
print("Full name:", full_name)

# mixing variable and string
print("Direct:", first_name + " Kim")


# NUMERIC TYPES
# INTEGER : represents whole numbers without decimal places
a = 10
b = 3
# ARITHMETIC OPERATIONS (expressions)
print("Addition:", a + b)       # +
print("Subtraction:", a - b)    # -
print("Multiplication:", a * b) # *
print("Division:", a / b)       # /
print("Floor division:", a // b)  
print("Remainder:", a % b)        

# FLOAT : describes floating-point numbers with one or more decimal places after a point
pi = 3.14159


# BOOLEAN : the special values True and False.
#           when storing True in is_on, we say that we assign a value to a variable
is_on = True


# type() : if we are unsure of a value type, we can get a variable's type using type() with the variable name
#          by adding print(), we can see the variable type in the console     
print("=== type() examples ===")     
is_ready = False
fuel_deposit = 60.78
best_grade = "A"
number_of_pets = 4
print("type(is_ready):", type(is_ready))
print("type(fuel_deposit):", type(fuel_deposit))
print("type(best_grade):", type(best_grade))
print("type(number_of_pets):", type(number_of_pets))


# TYPE CONVERSION : int(), str(), float(), bool()
# int()
print("\n=== int() conversion ===")
age = "33"
print("type(age):", type(age))

converted_age = int(age)
print("type(converted_age):", type(converted_age))
print("converted_age < 35:", converted_age < 35)

# if we use int() on a float value, we'll simply remove the decimal point and subsequent values
price = 26.99
print("int(price):", int(price))

# if we use int() on a boolean, the equivalent numerical value will be 1 for True and 0 for False
member = True
not_member = False
member_as_int = int(member)
not_member_as_int = int(not_member)
print("int(True):", member_as_int)
print("int(False):", not_member_as_int)

# str()
print("\n=== str() conversion ===")
password = 123456
old_password = "dkfjd789"
print(str(password) == old_password)

# float()
print("\n=== float() conversion ===")
weeks = 14
print(float(weeks))

# bool() : we can use bool() to convert a variable into a Boolean
#          if the variable has content, it will become True
#          if it's empty or 0, it'll become False
print("\n=== bool() conversion ===")
name = "Sam"
middle_name = ""
foot_size = 7.5
siblings = 0

boolean_name = bool(name)
boolean_middle_name = bool(middle_name)
boolean_foot_size = bool(foot_size)
boolean_siblings = bool(siblings)

print(boolean_name)
print(boolean_middle_name)
print(boolean_foot_size)  
print(boolean_siblings)

print(bool(""))   # False
print(bool(" "))  # True