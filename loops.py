# =========================
# LOOPS
# =========================

# WHILE

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
