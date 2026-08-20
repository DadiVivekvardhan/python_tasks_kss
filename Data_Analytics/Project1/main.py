#Scenario 1: Basic Data Loading & Cleaning
#You are given a CSV file containing railway gauge data.
#👉 Tasks:
#1. Load the dataset into a Pandas DataFrame.
#2. Display the first 5 rows and column names.
#3. Check for missing values and replace them with 0.
#4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("graphs", exist_ok=True)

df = pd.read_csv("railway_gauges.csv")

print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

df = df.fillna(0)

gauge_columns = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]

for column in gauge_columns:
    df[column] = pd.to_numeric(df[column])

df[gauge_columns] = df[gauge_columns].fillna(0)

print("\nData after cleaning:")
print(df.head())

print("\nData types after cleaning:")
print(df.dtypes)

#Scenario 2: Simple Visualization
#You want a quick understanding of total railway track growth.
#👉 Tasks:
#1. Extract Year and Total columns.
#2. Plot a line graph showing Total tracks over years.
#3. Add:
#○ Title
#○ X and Y labels
#4. Identify whether the trend is increasing or decreasing.
year = df["Year"]
total = df["Total"]

plt.plot(year, total)

plt.title("Total Railway Tracks Over Years")
plt.xlabel("Year")
plt.ylabel("Total Railway Tracks")

# Rotate year labels
plt.xticks(rotation=60)

# Save the graph
plt.savefig("graphs/total_tracks_trend.png")

#Scenario 3: Filtering + Bar Chart
#You are asked to analyze modern railway expansion.
#👉 Tasks:
#1. Filter the dataset for years after 2000.
#2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
#3. Plot a grouped bar chart comparing all three gauges.
#4. Add legend and proper labels.
#5. Identify which gauge dominates in recent years.

plt.figure()

# Get starting year
df["Start_Year"] = df["Year"].str[:4].astype(int)

# Filter years after 2000
recent_data = df[df["Start_Year"] > 2000]

# Select gauge columns
broad = recent_data["Broad Gauge"]
metre = recent_data["Metre Gauge"]
narrow = recent_data["Narrow Gauge"]

# Create positions
x = np.arange(len(recent_data))
width = 0.25

# Create grouped bar chart
plt.bar(x - width, broad, width, label="Broad Gauge")
plt.bar(x, metre, width, label="Metre Gauge")
plt.bar(x + width, narrow, width, label="Narrow Gauge")

# Add title and labels
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Gauge Length")

# Add year labels
plt.xticks(x, recent_data["Year"], rotation=45)


plt.legend()

plt.savefig("graphs/gauge_comparison.png")


#Scenario 4: Feature Engineering + Pie Chart
#You want to analyze the contribution of each gauge type.
#👉 Tasks:
#1. Calculate total sum of each gauge across all years.
#2. Create a new structure (Series/DataFrame) for totals.
#3. Plot a pie chart showing percentage contribution.
#4. Add percentage labels (autopct).

# Calculate total of each gauge
broad_total = df["Broad Gauge"].sum()
metre_total = df["Metre Gauge"].sum()
narrow_total = df["Narrow Gauge"].sum()

# Create a Series
gauge_totals = pd.Series({
    "Broad Gauge": broad_total,
    "Metre Gauge": metre_total,
    "Narrow Gauge": narrow_total})

# Start a new graph
plt.figure()

# Create pie chart
plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct="%1.1f%%")
# Add title
plt.title("Railway Gauge Contribution")

# Save graph
plt.savefig("graphs/gauge_contribution.png")

#5. Interpret which gauge contributes the most.
#Broad Gauge contributes the most across the years.

#Scenario 5: Advanced Analysis + Multiple Graphs
#You are asked to perform a complete analysis of railway trends.
#👉 Tasks:
#1. Create new columns:
#○ % Broad Gauge
#○ % Metre Gauge
#○ % Narrow Gauge
#2. Use NumPy (np.diff) to calculate yearly growth of Total tracks.
#3. Plot:
#○ Line graph for all gauges
#○ Stacked bar chart showing composition
#4. Highlight:
#○ Years with highest growth

# Step 1: Create percentage columns

df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100

print("\nPercentage columns:")
print(df[["Year", "% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].head())


# Step 2: Calculate yearly growth using NumPy

total_array = df["Total"].to_numpy()

growth = np.diff(total_array)

print("\nYearly growth:")
print(growth)


# Step 3: Find highest growth

highest_growth = growth.max()

highest_index = growth.argmax()

highest_year = df["Year"].iloc[highest_index + 1]

print("\nHighest yearly growth:", highest_growth)
print("Year with highest growth:", highest_year)


# Step 4: Line graph for all gauges

plt.figure()

plt.plot(df["Year"], df["Broad Gauge"], label="Broad Gauge")
plt.plot(df["Year"], df["Metre Gauge"], label="Metre Gauge")
plt.plot(df["Year"], df["Narrow Gauge"], label="Narrow Gauge")

plt.title("Railway Gauge Trends")
plt.xlabel("Year")
plt.ylabel("Gauge Length")

plt.xticks(rotation=45)

plt.legend()

plt.savefig("graphs/all_gauges_trend.png")


# Step 5: Stacked bar chart

plt.figure()

plt.bar(
    df["Year"],
    df["Broad Gauge"],
    label="Broad Gauge"
)

plt.bar(
    df["Year"],
    df["Metre Gauge"],
    bottom=df["Broad Gauge"],
    label="Metre Gauge"
)

plt.bar(
    df["Year"],
    df["Narrow Gauge"],
    bottom=df["Broad Gauge"] + df["Metre Gauge"],
    label="Narrow Gauge"
)

plt.title("Railway Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Gauge Length")

plt.xticks(rotation=45)

plt.legend()

plt.savefig("graphs/gauge_composition.png")

plt.show()

#○ Decline in any gauge
#Narrow Gauge is declined

#5. Provide a final conclusion:
#👉 “Is the railway system shifting towards a single dominant gauge?”
# Yes.Railway system shifting towards Broad Gauge.








