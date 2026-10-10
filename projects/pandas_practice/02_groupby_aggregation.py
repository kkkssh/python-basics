import pandas as pd

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Passengers": [120, 150, 90, 180, 200],
    "Route": ["A", "B", "A", "B", "A"]
}

df = pd.DataFrame(data)


# Calculate the average number of passengers by route
print(df.groupby("Route")["Passengers"].mean())

# groupby("Route"): Group rows with the same route
# ["Passengers"]: Select the Passengers column
# mean(): Calculate the average for each route


# Calculate the total number of passengers by route
print(df.groupby("Route")["Passengers"].sum())

# sum(): Add up the passenger numbers for each route


# Count the number of non-missing passenger records by route
print(df.groupby("Route")["Passengers"].count())

# count(): Count non-missing values in each group


# Calculate multiple statistics by route
print(df.groupby("Route")["Passengers"].agg(["count", "mean", "sum"]))

# agg(): Apply multiple aggregation functions at once


# Calculate the minimum and maximum passenger numbers by route
print(df.groupby("Route")["Passengers"].agg(["min", "max"]))