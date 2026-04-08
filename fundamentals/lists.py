# =========================
# LISTS
# =========================

# CREATING A LIST
fruits = ["apple", "banana", "grape"]

# INDICES : start at zero and increase with each further value
# INDEX : the position of an element in a list

# ACCESSING ELEMENTS
print(fruits[0])  # apple

# CHANGING ELEMENTS
fruits[1] = "mango"
print(fruits)

# ADDING AN ELEMENT TO THE END OF THE LIST
fruits.append("orange")
print(fruits)

# ADDING AN ELEMENT AT A SPECIFIC INDEX
fruits.insert(0, "lemon")
print(fruits)

# REMOVING THE LAST ELEMENT
fruits.pop()
print(fruits)

# REMOVING AN ELEMENT BY INDEX
fruits.pop(1)
print(fruits)

# REMOVING AN ELEMENT BY VALUE
fruits.remove("mango")
print(fruits)

