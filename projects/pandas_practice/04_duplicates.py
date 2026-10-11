import pandas as pd

# Create a DataFrame with duplicate rows
data_duplicated = {
    "Day": ["Monday", "Tuesday", "Tuesday", "Wednesday", "Thursday"],
    "Passengers": [120, 150, 150, 90, 180],
    "Route": ["A", "B", "B", "A", "B"]
}

df_duplicated = pd.DataFrame(data_duplicated)

print(df_duplicated)


# Check for duplicate rows
print(df_duplicated.duplicated())

# True: The row is a duplicate
# False: The row is not a duplicate


# Count duplicate rows
print(df_duplicated.duplicated().sum())


# Remove duplicate rows
print(df_duplicated.drop_duplicates())


# Save the cleaned DataFrame
df_clean = df_duplicated.drop_duplicates()

print(df_clean)


# Reset the index and keep the old index as a column
df_with_old_index = df_clean.reset_index()

print(df_with_old_index)


# Reset the index and discard the old index
df_clean = df_clean.reset_index(drop=True)

print(df_clean)

# reset_index(): Reset the row index
# drop=True: Discard the old index instead of keeping it as a column


