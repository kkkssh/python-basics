# TODO List CLI App

A simple command-line TODO list program built with Python.

## Features

- Allows users to add tasks to the list
- Displays all tasks with numbering
- Allows users to mark tasks as complete
- Displays task status (☑️ completed / ❎ not completed)
- Shows a message if the list is empty
- Allows users to remove tasks by selecting a task number
- Validates task number before removing a task
- Runs continuously until the user chooses to exit

## How to Run

Run the Python file:

```bash
python main.py
```

## Example

```
1. Add a task
2. View tasks
3. Mark a task as complete
4. Remove a task
5. Exit

Enter the number of the menu (1/2/3/4/5): 1
Enter a task: Study Python
Task added

Enter the number of the menu (1/2/3/4/5): 2

1. [❎] Study Python

Enter the number of the menu (1/2/3/4/5): 3
Enter the task number to mark as complete: 1

Study Python is marked as complete

1. [☑️] Study Python
```

## Skills Used

- Lists
- Tuples (for storing task and completion status)
- Loops (for, while)
- Conditional statements (if/elif/else)
- User input handling
- Basic data structuring

## Future Improvements

- Save tasks to a file
- Improve user interface
- Add task editing feature
- Handle invalid input more safely