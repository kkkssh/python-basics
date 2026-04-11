# MINI PROJECT 2 - TODO LIST

# Description:
# A simple command-line TODO list program.

# Requirements:
# - User can add tasks
# - User can view tasks
# - User can remove tasks
# - Program runs until user exits

# Features:
# - Allows user to add tasks to the list
# - Displays all tasks currently stored
# - Allows user to remove tasks from the list
# - Repeats continuously until the user chooses to exit



todo_lists = []

while True:

    print("1. Add a list")
    print("2. View todo lists")
    print("3. Remove a list")
    print("4. Exit")

    choice = input("Enter the number of the menu(1/2/3/4): ")

    if choice == "1":
        todo = input("Write your todo list: ")
        todo_lists.append(todo)
    
    elif choice == "2":
        print(todo_lists)

    elif choice == "3":
        delete = input("Remove your task: ")
        todo_lists.remove(delete)
    
    elif choice == "4":
        print("Exiting the program")
        break

    else:
        print("Choose the right number")
        


