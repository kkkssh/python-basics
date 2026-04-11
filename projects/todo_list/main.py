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
# - Displays all tasks with numbering
# - Shows a message if the list is empty
# - Allows user to remove tasks by selecting a task number
# - Validates task number before removing a task
# - Repeats continuously until the user chooses to exit



todo_lists = []

while True:

    print("\n1. Add a task")
    print("2. View todo lists")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter the number of the menu(1/2/3/4): ")

    if choice == "1":
        todo = input("Write your todo list: ")
        todo_lists.append(todo)
        print("Task added")
    
    elif choice == "2":
        if len(todo_lists) == 0:
            print("Your todo list is empty")
        else:
            index = 1
            for task in todo_lists:
                print(f"{index}. {task}")
                index += 1

    elif choice == "3":
        if len(todo_lists) == 0:
            print("Your todo list is empty")
        else:
            index = 1
            for task in todo_lists:
                print(f"{index}. {task}")
                index += 1

            delete_num = int(input("Enter the task number to remove: "))

            if delete_num >= 1 and delete_num <= len(todo_lists):
                remove_task = todo_lists.pop(delete_num - 1)
                print(f"{remove_task} is deleted")
            else:
                print("Please enter a valid number")
    
    elif choice == "4":
        print("Exiting the program")
        break

    else:
        print("Choose the right number")
        


