#Scenario 1: Data Loading & Preprocessing
#You are given the ign.csv dataset containing game reviews.
#👉 Tasks:
#1. Load the dataset using Pandas.
#2. Display:
#○ First 5 rows (head())
#○ Last 5 rows (tail())
#○ Shape of dataset
#3. Remove the unnecessary column:
#○ "Unnamed: 0" (index column)
#4. Check for missing values in:
#○ score, genre, platform
#5. Handle missing values:
#○ Fill numeric column score with mean
#○ Fill categorical column genre with mode
#6. Ensure correct data types:
#○ score → float
#○ release_year, release_month, release_day → integer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("graphs", exist_ok=True)

# Load dataset
df = pd.read_csv("ign.csv")

# First 5 rows
print("First 5 rows:")
print(df.head())

# Last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Shape
print("\nShape of dataset:")
print(df.shape)

# Remove unnecessary column
df = df.drop("Unnamed: 0", axis=1)

# Check missing values
print("\nMissing values:")
print(df[["score", "genre", "platform"]].isnull().sum())

# Fill missing score with mean
df["score"] = df["score"].fillna(df["score"].mean())

# Fill missing genre with mode
df["genre"] = df["genre"].fillna(df["genre"].mode()[0])

# Convert data types
df["score"] = df["score"].astype(float)
df["release_year"] = df["release_year"].astype(int)
df["release_month"] = df["release_month"].astype(int)
df["release_day"] = df["release_day"].astype(int)

# Check data types
print("\nData types:")
print(df.dtypes)


#Scenario 2: Line Graph (Score Trend) + Save
#You want to analyze how game scores change over time.
#👉 Tasks:
#1. Group data by release_year.
#2. Calculate average score per year using Pandas.
#3. Convert results into NumPy arrays.
#4. Plot a line graph:
#○ X-axis → release_year
#○ Y-axis → average score
#5. Add:
#○ Title: "Average Game Score Over Years"
#○ Axis labels
#6. Save the graph: plt.savefig("avg_score_trend.png")


# Group by release year and calculate average score
yearly_score = df.groupby("release_year")["score"].mean()

# Convert results into NumPy arrays
years = yearly_score.index.to_numpy()
scores = yearly_score.values

plt.figure(figsize=(6, 4))

# Create line graph
plt.plot(years, scores,marker="o")

# Add title and labels
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")

# Save graph
plt.savefig("graphs/avg_score_trend.png")

#Scenario 3: Filtering + Bar Chart + Save
#You want to compare top platforms.
#👉 Tasks:
#1. Filter dataset where:
#○ score > 7
#2. Count number of high-rated games per platform.
#3. Select top 10 platforms using Pandas.
#4. Convert data into NumPy arrays.
#5. Plot a bar chart:
#○ X-axis → platform
#○ Y-axis → count of games
#6. Rotate x-axis labels for readability.
#Save the graph: plt.savefig("top_platforms_bar.png")


# Filter games with score greater than 7
high_rated = df[df["score"] > 7]

# Count high-rated games for each platform
platform_counts = high_rated["platform"].value_counts()

# Select top 10 platforms
top_platforms = platform_counts.head(10)

# Convert results into NumPy arrays
platforms = top_platforms.index.to_numpy()
counts = top_platforms.values

plt.figure(figsize=(6, 4))

# Create bar chart
plt.bar(platforms, counts)

# Add title and labels
plt.title("Top 10 Platforms with High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")

# Rotate x-axis labels
plt.xticks(rotation=45)

# Save graph
plt.savefig("graphs/top_platforms_bar.png")


#Scenario 4: Aggregation + Pie Chart + Save
#You want to analyze genre distribution.
#👉 Tasks:
#1. Count the number of games per genre.
#2. Select top 5 genres using Pandas.
#3. Prepare labels and values.
#4. Plot a pie chart:
#○ Labels → genre
#○ Values → count
#5. Add percentage labels (autopct).
#Save the graph: plt.savefig("genre_distribution.png")


# Count games by genre
genre_counts = df["genre"].value_counts()

# Select top 5 genres
top_genres = genre_counts.head(5)

# Prepare labels and values
labels = top_genres.index.to_numpy()
values = top_genres.values

plt.figure(figsize=(6, 4))

# Create pie chart
plt.pie(values, labels=labels, autopct="%1.1f%%")

# Add title
plt.title("Top 5 Game Genres")

# Save graph
plt.savefig("graphs/genre_distribution.png")


#Scenario 5: Advanced Analysis + Multiple Graphs
#You are asked to perform a detailed analysis of review patterns.
#👉 Part 1: Feature Engineering
#1. Create a new column:
#○ score_category:
#■ score >= 9 → "Excellent"
#■ 7 <= score < 9 → "Good"
#■ < 7 → "Average"
#2. Convert editors_choice:
#○ Y → 1, N → 0

conditions = [df["score"] >= 9,df["score"] >= 7]

categories = ["Excellent", "Good"]

df["score_category"] = np.select(
    conditions,
    categories,
    default="Average")

# Convert editors_choice
df["editors_choice"] = df["editors_choice"].map({"Y": 1, "N": 0})

# Check the result
print(df[["score", "score_category", "editors_choice"]].head())


print("---------------------------------------------------------------------")

#👉 Part 2: NumPy Analysis
#3. Use NumPy to:
#○ Calculate yearly score growth using np.diff() on average yearly scores

# Group the data by release year
# Calculate the average score for each year
yearly_score = df.groupby("release_year")["score"].mean()

# Convert the release years into a NumPy array
years = yearly_score.index.to_numpy()

# Convert the average scores into a NumPy array
scores_array = yearly_score.values

# Calculate the difference between consecutive yearly scores
# np.diff() gives the yearly score growth
yearly_growth = np.diff(scores_array)

# Display the yearly average scores
print("Average Score for Each Year:")
print(yearly_score)

# Display yearly score growth
print("\nYearly Score Growth:")
print(yearly_growth)

# Display the years corresponding to the growth values
# We use years[1:] because np.diff() produces one less value
print("\nYears for Yearly Growth:")
print(years[1:])

#👉 Part 3: Visualizations
#📈 Line Graph
#4. Plot trend of:
#○ Average score per release_year
#📊 Stacked Bar Chart
#5. Show count of:
#○ score_category per release_year
#📉 Histogram
#6. Plot distribution of:
#○ score

# =========================================================
# LINE GRAPH
# =========================================================

plt.figure(figsize=(6, 4))

# Plot average score for each release year
# marker="o" adds circles at each data point
plt.plot(years, scores_array, marker="o")

# Add title
plt.title("Average Game Score Over Years")

# Add X-axis label
plt.xlabel("Release Year")

# Add Y-axis label
plt.ylabel("Average Score")

# Save the line graph
plt.savefig("graphs/score_trend.png")


# =========================================================
# STACKED BAR CHART
# =========================================================

# Count each score category for every release year
# crosstab creates a table:
# rows    -> release_year
# columns -> score_category
category_counts = pd.crosstab(
    df["release_year"],
    df["score_category"]
)

# Make sure all three categories are present
# reindex adds a category if it is missing
category_counts = category_counts.reindex(
    columns=["Average", "Good", "Excellent"],
    fill_value=0
)

plt.figure(figsize=(6, 4))

# Create the stacked bar chart
plt.bar(
    category_counts.index,
    category_counts["Average"],
    label="Average"
)

plt.bar(
    category_counts.index,
    category_counts["Good"],
    bottom=category_counts["Average"],
    label="Good"
)

plt.bar(
    category_counts.index,
    category_counts["Excellent"],
    bottom=(
        category_counts["Average"]
        + category_counts["Good"]
    ),
    label="Excellent"
)

# Add title
plt.title("Score Category per Release Year")

# Add X-axis label
plt.xlabel("Release Year")

# Add Y-axis label
plt.ylabel("Number of Games")

# Add legend
plt.legend()

# Save the stacked bar chart
plt.savefig("graphs/score_category_stacked.png")


# =========================================================
# HISTOGRAM
# =========================================================

# Convert score column into a NumPy array
score_array = df["score"].to_numpy()

plt.figure(figsize=(6, 4))

# Create histogram
plt.hist(score_array, bins=10)

# Add title
plt.title("Distribution of Game Scores")

# Add X-axis label
plt.xlabel("Score")

# Add Y-axis label
plt.ylabel("Frequency")

# Save the histogram
plt.savefig("graphs/score_distribution.png")

# Display the graphs
plt.show()

#Identify:
#● Which years had highest scores
#2007 had higest score


#● Whether high scores increased over time
#High scores fluctuated over time rather than increasing consistently.


#● If editors_choice correlates with high scores
#Editor’s Choice games generally had higher scores than non-Editor’s Choice games.





