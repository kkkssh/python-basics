# =========================
# SETS AND OPERATIONS
# =========================

# SET: a collection of unique values (no duplicates)
# Sets are unordered, so the printed order may be different each time
numbers = {1, 2, 3, 3, 4}
print(f"Numbers (duplicates removed): {numbers}")   # duplicates removed automatically


# ADDING ITEMS
answer_options = {"yes", "no"}

answer_options.add("maybe")
print(answer_options)


# CHECKING ITEMS : sets don't have indices
print(f"Is 'no' an option? {'no' in answer_options}")    # True


# LOOPING THROUGH A SET
for answer in answer_options:
    print(f"Answer options: {answer_options}")


# REMOVING ITEMS
classes = {"Geometry", "Music", "French", "Spanish"}

classes.remove("French")    # error if the item is not found
classes.discard("German")   # no error if the item is not found

if "History" in classes:    # to avoid an error
    classes.remove("History")

print(f"Remaining classes: {classes}")


# SETS IN LISTS : removing duplicates from a list
grocery_list = ["broccoli", "cereal", "milk", "broccoli"]

unique_grocery_set = set(grocery_list)
unique_grocery_list = list(set(grocery_list))

print(f"Unique grocery items as a set: {unique_grocery_set}")
print(f"Unique grocery items as a list: {unique_grocery_list}")


# USING A FUNCTION TO REMOVE DUPLICATES
def remove_duplicates(items):
    return list(set(items))

print(f"Removed duplicates using a function: {remove_duplicates(grocery_list)}")


# SET OPERATIONS: len, issubset, union, intersection, difference
friends = {"Louis", "Brenda", "Emma", "Ed"}
chat = {"Emma", "Ed"}   # a subset of friends
study_group = {"Louis", "Lisa"}

print(f"Number of friends: {len(friends)}")
print(f"Is chat a subset of friends? {chat.issubset(friends)}")                 # True
print(f"Is study group a subset of friends? {study_group.issubset(friends)}")   # False


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Union using method: {a.union(b)}")
print(f"Union using operator: {a | b}")   

print(f"Intersection using method: {a.intersection(b)}")
print(f"Intersection using operator: {a & b}")   

print(f"Difference using method: {a.difference(b)}")
print(f"Difference using operator (a - b): {a - b}")
print(f"Difference using operator (b - a): {b - a}")