# Order Analyzer

A simple Python program that analyzes customer order data.

## Features

- Calculates total sales
- Calculates the average order price
- Filters orders above a certain price
- Counts how many times each item was ordered
- Finds the most popular item
- Formats prices with currency symbols (€)
- Allows user input for new orders

## How to Run

Run the Python file:

```bash
python main.py
```

## Example

```
Total sales: €24.50

Average price: €4.08

Expensive orders:
- {'item': 'latte', 'price': 4.5}
- {'item': 'latte', 'price': 4.5}
- {'item': 'cake', 'price': 5.0}
- {'item': 'matcha latte', 'price': 5.0}

Item counts: {'latte': 2, 'americano': 1, 'cake': 1, 'matcha latte': 1, 'tea': 1}

Most popular item: latte
```

## Skills Used
- Lists
- Dictionaries
- Loops
- Conditional statements
- Basic data analysis
- Basic output formatting
- User input handling

## Future Improvements
- Save order data to a file