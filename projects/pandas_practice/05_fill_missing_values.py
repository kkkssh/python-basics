import pandas as pd

# Create a DataFrame with missing values
data_missing = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Passengers": [120, 150, None, 180, 200],
    "Route": ["A", "B", "A", None, "A"]
}

df_missing = pd.DataFrame(data_missing)

print(df_missing)


# Calculate the average number of passengers
average_passengers = df_missing["Passengers"].mean()

print(average_passengers)  # 162.5


# Fill missing passenger values with the average
df_filled = df_missing.copy()

df_filled["Passengers"] = df_filled["Passengers"].fillna(average_passengers)

print(df_filled)


# Check for remaining missing values
print(df_filled.isna().sum())


# Fill missing route values with "Unknown"
df_filled["Route"] = df_filled["Route"].fillna("Unknown")

print(df_filled)


# Check for remaining missing values
print(df_filled.isna().sum())