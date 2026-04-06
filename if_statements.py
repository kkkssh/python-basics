# =========================
# IF STATEMENTS
# =========================

# IF STATEMENT : run code only if it is evaluated as true
# CONDITIONS : True, False - decide if the code runs or gets skipped 
# CONDITIONALS : statements relying on conditions
if True:
    print("Hello!")

# if we want to skip the code, use False
if False:
    print("Hi!")

# INDENTATION : the space between the code and the code editor's margin
# INDENTATION OF 4 SPACES : to highlight code blocks, like indenting this display statement
# CODE BLOCKS : codes that are indented after an if statement. It can be more than a one-liner
con = True
if con:
    print("Look at me")
    print("I'm a code block")

# IndentationError : if the indentation is incorrect
if con:
    print("Look at me")
#  print("I'm a code block")

# COMPARISON OPERATORS
answer = "Picasso"
if answer == "Picasso":
#   print(answer + " is correct!")
    print(f"{answer} is correct!")

if answer != "Picasso":
    print(answer + " is wrong!")

age = 75
if age >= 55:
    print("Discount applied")

is_day = True
if is_day == True:
    print("Lights off!")

can_drive = False
if age >= 18:
    can_drive = True
print(can_drive)

# NOT OPERATOR
available = False
if available:
    print("In stock")
if not available:
    print("Out of stock")

# IF-ELSE
if available:
    print("1 in stock")
else:
    print("Out of stock")

number = 99
if number == 1:
    print("It's 1")
else:
    print("It's not 1")

# IF-ELIF-ELSE : multiple conditions
hour = 20
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else:
    print("Good night")
