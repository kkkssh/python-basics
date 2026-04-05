#Types : strings, integers, floats, booleans

# String : characters between quotes " "
country = "UK"

# Integer : represents whole numbers without decimal places
score =13

# Float : describes floating-point numbers with one or more decimal places after a point
pi = 3.14159

# Boolean : represents only two values - the special values True and False.
#           when storing True in is_on, we say that we assign a value to a variable.
is_on = True


# type() : if we are unsure of a value type, we can get a variable's type using type() with the variable name
#          by adding print(), we can see the variable type in the console          
is_ready = False
fuel_deposit = 60.78
best_grade = "A"
number_of_pets = 4
print(type(is_ready))
print(type(fuel_deposit))
print(type(best_grade))
print(type(number_of_pets))


# Python has built-in functions to convert data types - int(), str(), float(), bool()
# int()
age = "33"
print(type(age))

converted_age = int(age)
print(type(converted_age))

print(converted_age < 35)

# if we use int() on a float value, we'll simply remove the decimal point and subsequent values
price = 26.99
print(int(price))

# if we use int() on a boolean, the equivalent numerical value will be 1 for True and 0 for False
member = True
not_member = False
value = int(member)
second_value = int(not_member)
print(value)
print(second_value)

# str()
password = 123456
old_password = "dkfjd789"
print(str(password) == old_password)

# float()
weeks = 14
print(float(weeks))

# bool() : we can use bool() to convert a variable into a Boolean
#          if the variable has content, it will become True
#          if it's empty or 0, it'll become False
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
