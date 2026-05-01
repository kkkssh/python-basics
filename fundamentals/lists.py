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


# LOOPING THROUGH LISTS
final_scores = [17, 20, 33, 12]

for score in final_scores:
    print(f"Adjusted score: {score + 1}")

# FILTERING DATA
for score in final_scores:
    if score > 16:
        print(f"High score: {score}")


# FILTERING DATA (STORING RESULTS)
high_scores = []

for score in final_scores:
    if score > 16:
        high_scores.append(score)

print(high_scores)


# CONDITIONAL STATEMENTS WITH LISTS
sodas = ["coke", "fanta", "7up"]

if len(sodas) > 2:
    print("Too much soda!")
else:
    print("All good")
