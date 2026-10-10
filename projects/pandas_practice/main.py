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
print(df.shape)  # (5, 3): 5 rows and 3 columns


# Calculate the average number of passengers 
print(df["Passengers"].mean())  # 148.0


# Filter rows where the number of passengers is greater than 150
print(df[df["Passengers"] > 150])


# Sort by passengers in descending order (highest to lowest)
print(df.sort_values(by="Passengers", ascending=False))


# Sort by passengers in ascending order (lowest to highest)
print(df.sort_values(by="Passengers", ascending=True))


# Calculate the average number of passengers by route
print(df.groupby("Route")["Passengers"].mean())

# groupby("Route"): Group rows with the same route
# ["Passengers"]: Select the Passengers column
# mean(): Calculate the average for each route


# Calculate the total number of passengers by route
print(df.groupby("Route")["Passengers"].sum())

# sum(): Add up the passenger numbers for each route


# Count the number of passenger records by route
print(df.groupby("Route")["Passengers"].count())

# count(): Count non-missing values in each group


# Calculate multiple statistics by route
print(df.groupby("Route")["Passengers"].agg(["count", "mean", "sum"]))

# agg(): Apply multiple aggregation functions at once


# Calculate the minimum and maximum passenger numbers by route
print(df.groupby("Route")["Passengers"].agg(["min", "max"]))


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


# Remove rows with missing values
print(df_missing.dropna())

# dropna(): Remove rows with at least one missing value


# Save the cleaned DataFrame in a new variable
# df_clean = df_missing.dropna()
# print(df_clean)

# dropna() returns a new DataFrame by default.
# The original DataFrame remains unchanged.