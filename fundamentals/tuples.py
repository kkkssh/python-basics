# =========================
# TUPLES
# =========================

# TUPLE: grouping related pieces of data
vertigo_data = ("Vertigo", 1958, "A. Hitchcock")
user_data = ("Joe",)   # single-item tuple needs a comma

print(vertigo_data)
print(user_data)


# TUPLE vs LIST
scores = [("Mia", 75), ("Lee", 90)]
print(len(scores))  # 2
print(scores[0])    # ("Mia", 75)

# tuple unpacking in a loop
for name, score in scores:
    print(f"{name}: {score}")

# tuples are immutable
# we can't update, add, or delete values from tuples
# we use tuples to store information that shouldn't be modified

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 100   # possible
# my_tuple[0] = 100   # impossible

print(my_list)
print(my_tuple)


# RETURNING TUPLES
def get_scores_data(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return highest_score, lowest_score

scores_numbers = [31, 17, 80]
highest, lowest = get_scores_data(scores_numbers)   # unpacking

print((highest, lowest))
print(f"Smallest score: {lowest}")
print(f"Highest score: {highest}")


def get_top_three(players):
    first = players[0]
    second = players[1]
    third = players[2]
    return first, second, third

players = ["Tom", "Ed", "Ann", "Tyra"]
top_three = get_top_three(players)

print(f"First: {top_three[0]}")
print(f"Second: {top_three[1]}")
print(f"Third: {top_three[2]}")


# returning a tuple
def form_team(players):
    return players[0], players[2]

players = ["Tom", "Ed", "Ann", "Tyra"]
team = form_team(players)

print(team)
# team[0] = "Chloe"   # impossible because tuple is immutable


def check_age(age):
    can_drive = age >= 18
    return age, can_drive

age, can_drive = check_age(17)

print((age, can_drive))
print(f"Age: {age}")
print(f"Can drive: {can_drive}")
