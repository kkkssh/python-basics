# =========================
# LOOPS
# =========================

# WHILE LOOPS

# INFINITE LOOPS : if a while loop's condition stays True forever
#while True:
#    print("Hi there!")

# STOPPING WHILE LOOPS
keep_going = True
while keep_going:
    print("Loop is running")
    keep_going = False    

# CONTROLLING WHILE LOOPS
# COUNTER VARIABLE : controls loop repetition
#                    start with a variable set to a number
counter = 1
while counter < 5:
    print(counter)
    counter += 1        # 1 2 3 4

counter = 5
while counter < 10:
    counter += 1
    print(counter)       # 6 7 8 9 10

counter = 6
while counter <= 10:
    print(counter)
    counter += 1        # 6 7 8 9 10



# FOR LOOPS

for i in range(3):      # i = loop counter 
    print(i)
    print("For loops are great!")

line = "*"
for i in range(5):
    print(line)
    line += "*"



# CONTINUE : used to skip the current block and move to the next iteration
# CONTINUE IN FOR LOOPS
for i in range(1, 6):
    if i == 2:
        continue
    print(i)    # 1 3 4 5

shopping_list = ["apples", "grapes", "bread", "milk", "eggs"]
for item in shopping_list:
    if item == "apples":
        continue
    print(f"Don't forget to buy: {item}")

# CONTINUE IN WHILE LOOPS
tasks = ["pending", "completed", "pending", "pending"]
index = 0
while index < len(tasks):
    if tasks[index] == "completed":
        print(f"Skipping task {index + 1}")
        index += 1
        continue
    print(f"Processing task {index + 1}")
    index += 1



# BREAK : used to stop the loop
# BREAK IN FOR LOOPS
for i in range(1, 6):
    if i == 3:
        break
    print(i)    # 1 2

for char in "hello":
    if char == "o":
        break
    print(char)

tasks = ["email boss", "fix bug", "attend meeting"]
for task in tasks:
    if task == "fix bug":
        print("Urgent task found: fix bug")
        break
    print(f"Working on: {task}")

# BREAK IN WHILE LOOPS
password = "open"
while True:
    if input("Enter the password: ") == password:
        print("Access granted!")
        break
    print("Incorrect password. Try again.")



# LOOP ELSE: runs after the loop finishes normally
for i in range(1, 6):
    print(i)    
else:
    print("Loop has ended")     # 1 2 3 4 5 Loop has ended

for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:
    print("Loop has ended")     # 1 2 3 4

shows = ["Dexter", "Friends", "The Office"]
for show in shows:
    print(show)
else:
    print("Those are my favorite shows!")
