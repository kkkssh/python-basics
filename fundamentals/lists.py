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

# GETTING LIST LENGTH
# len() : to get the number of elements in a list
print(f"Total scores: {len(final_scores)}")      # Total scores: 4 

# CONDITIONAL STATEMENTS WITH LISTS
sodas = ["coke", "fanta", "7up"]
if len(sodas) > 2:
    print("Too much soda!")
else:
    print("All good")

# FINDING MAXIMUM
temperatures = [3, 7, 1, 12, -5, 8.8, -10]
print(max(temperatures))

# FINDING MINIMUM
print(min(temperatures))

# SORTING LISTS : in ascending order
temperatures.sort()
print(temperatures)

sodas.sort()
print(sodas)

# SUMMING DATA
total = sum(temperatures)
print(total)

avg = total / len(temperatures)
print(f"Average temperature: {avg}")

# JOINING LISTS
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
print(numbers1 + numbers2)

# COUNTING ELEMENTS
survey_answers = ["yes", "no", "sometimes", "yes"]
print(survey_answers.count("yes"))  # 2

# CHECKING ELEMENT EXISTENCE
print("no" in survey_answers)      # True
print("none" in survey_answers)    # False

if "yes" in survey_answers:
    print("There is at least one yes")

