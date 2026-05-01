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


# ADDING ELEMENTS

# append() - add to end
fruits.append("orange")
print(fruits)

# insert(index, value) - add at specific position
fruits.insert(0, "lemon")
print(fruits)


# REMOVING ELEMENTS

# pop() - removes last element
fruits.pop()
print(fruits)

# # pop(index) - removes element at index
fruits.pop(1)
print(fruits)

# remove(value) - removes by value
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


# NEGATIVE INDEXING
fruits = ["apple", "banana", "grape", "orange"]

print(fruits[-1])  # orange
print(fruits[-2])  # grape


# SLICING

# list[start:stop]
print(fruits[1:3])   # ['banana', 'grape']

# first two elements
print(fruits[:2])    # ['apple', 'banana']

# from index to end
print(fruits[2:])    # ['grape', 'orange']

# using negative indexing
print(fruits[-3:])   # ['banana', 'grape', 'orange']


# SLICING WITH STEP

# list[start:stop:step]
# step = interval
print(fruits[::2])      # ['apple', 'grape']
print(fruits[1:4:2])    # ['banana', 'orange']

# reverse from index 2
print(fruits[2::-1])    # ['grape', 'banana', 'apple']

# first 3 elements, every second item
print(fruits[:3:2])     # ['apple', 'grape']

# reverse entire list
print(fruits[::-1])     # ['orange', 'grape', 'banana', 'apple']

# copy list
copied = fruits[:]
print(copied)


# DELETING ELEMENTS WITH DEL
numbers = [10, 20, 30, 40, 50]

# delete by index
del numbers[1]
print(numbers)  # [10, 30, 40, 50]
