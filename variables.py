# =========================
# VARIABLES
# =========================

# VARIABLES: store information
#            use snake_case for multiple words

# = : to store a value inside it
#     we assign a value to a variable

# Lines of code are instructions for the computer to follow

# print() : we tell the computer to display a value in an area called the console


# BASIC VARIABLES
name = "Chloe"
print(name)
print("Hello, World!")


# UPDATING VARIABLES : the values they store can change
status = "Relaxing"
status = "Watching Netflix"
print(status)

status = "Reading a book"
print(status)


# ASSIGNING FROM OTHER VARIABLES
default_option = "upload"
new_status = "download"

new_status = default_option
print(new_status)


# SELF-ASSIGNMENT : increase or decrease variables set to numbers
#                   used to track changing values over time
wallet = 3
wallet += 2      # wallet = wallet + 2
wallet -= 1      # wallet = wallet -1
print(wallet)

name = "Account name: "
name += "Joanne"    # name = name + "Joanne"
name += " Rowling"  # name = name + " Rowling"
print(name)