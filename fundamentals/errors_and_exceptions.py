# =========================
# ERRORS AND EXCEPTIONS
# =========================

# errors stop a program from running

# exceptions are errors that occur
# while the program is running


# SYNTAX ERRORS

# SyntaxError usually occurs when Python
# cannot understand the code

# misspelled keywords
# iff cost > 10:

# missing symbols
# if cost < 10
#     print("You can buy it")

# incomplete statements
# if cost > 10:

# unexpected EOF (End Of File)
# occurs when Python reaches the end
# of a file before completing the code

# print(



# INDENTATION ERRORS

# IndentationError is a specific type
# of SyntaxError

# if cost > 10:
# print("Too expensive")



# CARET (^)

# a caret (^) indicates where Python
# found the error in the code



# DEBUGGING

# Traceback helps us debug our code,
# which means finding errors

# Tracebacks are usually read
# from bottom to top



# COMMON EXCEPTIONS

# ZeroDivisionError occurs when
# dividing by zero

# print(10 / 0)


# NameError occurs when referencing
# a variable that does not exist

# print(username)


# TypeError occurs when an operation
# is used with an inappropriate type

# print("5" + 5)


# ModuleNotFoundError occurs when Python
# cannot find a module

# import tiime


# IndexError occurs when an index
# is out of range

# scores = [25, 50, 10]
# print(scores[5])


# ValueError occurs when a value
# is of the correct type but
# has an invalid value

# int("hello")


# KeyError occurs when a dictionary
# key does not exist

# person = {"name": "Chloe"}
# print(person["age"])


# AttributeError occurs when an object
# does not have the requested attribute or method

# text = "hello"
# text.append("!")



# RAISING EXCEPTIONS

# raise is used to create an exception
# when a condition is not met

# raise can help prevent invalid data
# from being used in a program

# slices = 18
# diners = 0

# if diners < 1:
#     raise Exception("There must be at least one diner")
# else:
#     slices_each = slices / diners


# we can define both the kind of error
# and the error message

# age = -3

# if age < 0:
#     raise ValueError("Age cannot be negative")


# we can use conditions to validate inputs
# and raise an exception when the conditions are not met

# scores = [125, 60, 189, 88, 16]

# if min(scores) < 0 or max(scores) > 180:
#     raise ValueError("Error in scores")


# raise a specific type of exception

# name = 123

# if type(name) != str:
#     raise TypeError("Name must be a string")



# LOGIC ERRORS

# logic errors occur when there is
# no error or exception, but the code
# does not produce the expected result

# john = 24
# alana = 18

# average_age = john + alana / 2

# print(average_age)

# Correct version:
# average_age = (john + alana) / 2

