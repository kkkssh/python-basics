import pandas as pd

# Create a DataFrame with missing values
data_missing = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Passengers": [120, 150, None, 180, 200],
    "Route": ["A", "B", "A", None, "A"]
}

df_missing = pd.DataFrame(data_missing)

print(df_missing)


# Check for missing values
print(df_missing.isna())

# True: The value is missing
# False: The value is not missing


# Count missing values in each column
print(df_missing.isna().sum())

# isna(): Check for missing values
# sum(): Count missing values in each column


# Remove rows with at least one missing value
print(df_missing.dropna())

# dropna(): Remove rows with at least one missing value


# Save the cleaned DataFrame in a new variable
# df_clean = df_missing.dropna()
# print(df_clean)

# dropna() returns a new DataFrame by default.
# The original DataFrame remains unchanged.