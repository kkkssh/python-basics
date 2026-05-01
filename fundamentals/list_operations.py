# =========================
# LIST OPERATIONS
# =========================

# GETTING LIST LENGTH
# len() : to get the number of elements in a list
final_scores = [17, 20, 33, 12]
print(f"Total scores: {len(final_scores)}")  # Total scores: 4


# FINDING MAXIMUM
temperatures = [3, 7, 1, 12, -5, 8.8, -10]
print(max(temperatures))


# FINDING MINIMUM
print(min(temperatures))


# SORTING LISTS : in ascending order
temperatures.sort()
print(temperatures)

sodas = ["coke", "fanta", "7up"]
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