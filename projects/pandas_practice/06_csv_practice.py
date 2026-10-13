import pandas as pd

# Read the CSV file
df = pd.read_csv("projects/pandas_practice/passengers.csv")

print(df)


# Display the first 5 rows
print(df.head())


# Check the number of rows and columns
print(df.shape)


# Check column names and data types
print(df.info())


# Check the number of missing values in each column
print(df.isna().sum())


# Count duplicate rows
print(df.duplicated().sum())


# Remove duplicate rows
df_clean = df.drop_duplicates().copy()

print("\n=== After Removing Duplicates ===")
print(df_clean)


# Fill missing passenger values with the average
average_passengers = df_clean["Passengers"].mean()
df_clean["Passengers"] = df_clean["Passengers"].fillna(average_passengers)


# Fill missing route values with "Unknown"
df_clean["Route"] = df_clean["Route"].fillna("Unknown")

print("\n=== Cleaned Data ===")
print(df_clean)


# Check for remaining missing values
print("\n=== Remaining Missing Values ===")
print(df_clean.isna().sum())


# Save the cleaned DataFrame to a new CSV file
df_clean.to_csv(
    "projects/pandas_practice/passengers_cleaned.csv",
    index=False
)

print("\nCleaned data saved successfully!")
