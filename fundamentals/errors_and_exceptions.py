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


# INDENTATION ERRORS

# IndentationError is a specific type
# of SyntaxError

# if cost > 10:
# print("Too expensive")


# CARET (^)

# a caret (^) indicates where Python
# found the error in the code


# EXCEPTIONS

# Traceback helps us debug our code,
# which means finding errors
# best read from bottom to top


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