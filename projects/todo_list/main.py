# MINI PROJECT 2 - TODO LIST

# Description:
# A simple command-line TODO list program

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

# Extra features added:
# - User can mark tasks as complete
# - Tasks show completion status



todo_lists = []

while True:

    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Exit")

    choice = input("Enter the number of the menu(1/2/3/4/5): ")

    if choice == "1":
        todo = input("Enter a task: ")
        todo_lists.append((todo, False))
        print("Task added")
    
    elif choice == "2":
        if len(todo_lists) == 0:
            print("Your todo list is empty")
        else:
            index = 1
            for task, done in todo_lists:
                if done == True:
                    status = "Done"
                else:
                    status = "Not done"
                print(f"{index}. {task} - {status}")
                index += 1

    elif choice == "3":
        if len(todo_lists) == 0:
            print("Your todo list is empty")
        else:
            index = 1
            for task, done in todo_lists:
                if done == True:
                    status = "Done"
                else:
                    status = "Not done"
                print(f"{index}. {task} - {status}")
                index += 1

            complete_num = int(input("Enter the task number to mark as complete: "))

            if 1 <= complete_num <= len(todo_lists):
                    task_name, task_done = todo_lists[complete_num - 1]

                    if task_done == True:
                        print("This task is already completed")
                    else:
                        todo_lists[complete_num - 1] = (task_name, True)
                        print(f"{task_name} is marked as complete")
            else:
                print("Please enter a valid number")

    elif choice == "4":
        if len(todo_lists) == 0:
            print("Your todo list is empty")
        else:
            index = 1
            for task, done in todo_lists:
                if done == True:
                    status = "Done"
                else:
                    status = "Not done"
                print(f"{index}. {task} - {status}")
                index += 1


            delete_num = int(input("Enter the task number to remove: "))

            if delete_num >= 1 and delete_num <= len(todo_lists):
                remove_task, done = todo_lists.pop(delete_num - 1)
                print(f"{remove_task} was deleted")
            else:
                print("Please enter a valid number")
    
    elif choice == "5":
        print("Exiting the program")
        break

    else:
        print("Choose the right number")
        

