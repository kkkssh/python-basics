import pandas as pd

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Passengers": [120, 150, 90, 180, 200],
    "Route": ["A", "B", "A", "B", "A"]
}

# Create a DataFrame (convert the dictionary into a table)
df = pd.DataFrame(data)

print(df)


# Display the first 5 rows
print(df.head())  


# Show the number of rows and columns
print(df.shape)  # (5, 3)


# Calculate the average number of passengers 
print(df["Passengers"].mean())  # 148.0


# Filter rows where the number of passengers is greater than 150
print(df[df["Passengers"] > 150])