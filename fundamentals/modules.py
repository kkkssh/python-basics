# =========================
# MODULES
# =========================

# a module is a Python file
# that contains code such as
# functions, variables, or classes

# modules help organize code
# and make it reusable


# IMPORTING A MODULE

import math

print(f"The value of pi is {math.pi}")
print(f"The square root of 25 is {math.sqrt(25)}")
print(f"Rounded up to the nearest number {math.ceil(22.7324)}")

# help(math)  # displays documentation for the module


# IMPORTING ANOTHER MODULE

import statistics

scores = [4, 4, 3, 6, 1, 2, 8, 4]
mean_score = statistics.mean(scores)

print(f"Mean score is {mean_score}")


# IMPORTING MULTIPLE MODULES

import statistics, math

diameters = [9, 7, 4, 6]
mean_diameter = statistics.mean(diameters)

print(f"Mean diameter is {mean_diameter}")
print(f"Value of pi is {math.pi}")


# IMPORTING SPECIFIC ITEMS

from math import pi

print(f"Value of pi is {pi}")


from statistics import mean

test_scores = [33, 7, 4, 6]
mean_result = mean(test_scores)

print(f"Mean result is {mean_result}")