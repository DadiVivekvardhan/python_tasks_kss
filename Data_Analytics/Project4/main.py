'''
=================================================================================================================================
---------------------------------------------📊 Project Title: House Sales Data Analysis--------------------------------------
--------------------------------------Analyze House Sales dataset using NumPy, Pandas, Matplotlib-----------------------------
=================================================================================================================================
'''
'''
=================================================================================================================================
 📦 1. Import Required Libraries
=================================================================================================================================
 👉 Import numpy
 👉 Import pandas
 👉 Import matplotlib.pyplot
 👉 (Optional) Import os for folder creation
<Import your libraries>
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

'''
=================================================================================================================================
                                     🟢 SCENARIO 1: Data Loading & Basic Cleaning
=================================================================================================================================
�� Tasks:
1. Load the dataset using Pandas.
2. Display:
○ First 5 rows
○ Column names
3. Check for missing values in:
○ bedrooms
○ bathrooms
○ sqft_living
○ price
4. Fill missing values:
○ bedrooms → use mode
○ bathrooms → use mean
○ sqft_living → use mean
○ price → use mean
5. Convert these columns to numeric if required:
○ bedrooms
○ bathrooms
○ sqft_living
○ price
'''
os.makedirs("graphs", exist_ok=True)
# ==============================
# Scenario 1: Data Loading & Basic Cleaning
# ==============================

df = pd.read_csv("kc_house_data.csv")

# 2. Display:
# First 5 rows
print("First 5 Rows:")
print(df.head())

# Column names
print("\nColumn Names:")
print(df.columns)

# 3. Check for missing values in required columns
print("\nMissing Values Before Filling:")
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())

# 4. Fill missing values
# bedrooms → use mode
df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].mode()[0])

# bathrooms → use mean
df["bathrooms"] = df["bathrooms"].fillna(df["bathrooms"].mean())

# sqft_living → use mean
df["sqft_living"] = df["sqft_living"].fillna(df["sqft_living"].mean())

# price → use mean
df["price"] = df["price"].fillna(df["price"].mean())

# 5. Convert columns to numeric if required
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["bathrooms"] = pd.to_numeric(df["bathrooms"], errors="coerce")
df["sqft_living"] = pd.to_numeric(df["sqft_living"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Final check after cleaning
print("\nMissing Values After Filling:")
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())

'''
=================================================================================================================================
                                     🟢 SCENARIO 2: Line Graph + Save
=================================================================================================================================
�� Tasks:
1. Select:
○ id
○ price
2. Take the first 10 rows only.
3. Convert price into a NumPy array.
4. Plot a line graph:
○ X-axis → index (0–9)
○ Y-axis → Price
5. Add:
○ Title
○ X-label
○ Y-label
6. Save the graph: plt.savefig("house_prices_line.png")
'''
line_df = df[['id','price']].head(10)
price_array = line_df['price'].to_numpy()
plt.plot(price_array, marker = 'o',color = 'darkblue')
plt.xlabel("Index")
plt.ylabel("Price")
plt.title("House Prices of first 10 records")
plt.savefig("graphs/house_price_line.png")
plt.tight_layout()
plt.show()

'''
=================================================================================================================================
                                     🟡 SCENARIO 3: Filtering + Bar Chart + Save
=================================================================================================================================
�� Tasks:
1. Filter houses where:
○ price > 1000000
2. Count number of houses per:
○ bedrooms
3. Select top bedroom categories.
4. Convert results to NumPy arrays.
5. Plot a bar chart:
○ X-axis → Bedrooms
○ Y-axis → Count
6. Rotate labels if needed.
7. Save graph: plt.savefig("expensive_houses_bar.png")

'''
#Cleaning data
df["price"] = pd.to_numeric(df["price"], errors = "coerce")
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors = "coerce")

#Converting bedrooms to proper integer
df["bedrooms"] = df["bedrooms"].round().astype(int)

#Filter expensive houses (balanced threshold)
expensive_houses = df[df["price"] > 1000000]

#Counting number of houses per bedrooms
bedrooms_counts = expensive_houses["bedrooms"].value_counts()

#Selecting top bedroom categories
top_bedrooms = bedrooms_counts.head(5)

#Converting results to NumPy arrays
x = top_bedrooms.index.to_numpy()
y = top_bedrooms.values

#Bar plot
plt.figure(figsize = (8,5))
plt.bar(x,y, color = "skyblue",edgecolor = "navy")
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Expensive Houses by Bedrooms")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.savefig("graphs/expensive_houses_bar.png")
plt.show()
'''
=================================================================================================================================
                                     🟡 SCENARIO 4: Pie Chart (Region Distribution) + Save
=================================================================================================================================
�� Tasks:
1. Count number of houses by:
○ bedrooms
2. Select top 5 bedroom categories.
3. Prepare:
○ Labels
○ Values
4. Plot a pie chart.
5. Add percentage labels.
6. Save graph: plt.savefig("bedroom_distribution.png")
'''
# 1. Count number of houses by: bedrooms
bedroom_counts = df['bedrooms'].value_counts()

# 2. Select top 5 bedroom categories
top_5_bedrooms = bedroom_counts.head(5)

# 3. Prepare: Labels and Values
# Converting index to string labels and values to a list
labels = [f"{int(b)} Bedrooms"
          for b in top_5_bedrooms.index]
values = top_5_bedrooms.values

# 4. Plot a pie chart
# 5. Add percentage labels
plt.figure(figsize=(10, 7))
plt.pie(
    values, 
    labels=labels,
    shadow = True,
    autopct='%1.1f%%',  # Adds percentage labels formatted to 1 decimal place
    startangle=140
)

# Adding details for clarity
plt.title('Top 5 Bedroom Categories', pad = 20)
plt.axis('equal')  # Ensures the pie chart is a circle
plt.legend()
plt.tight_layout()
# 6. Save graph
plt.savefig("graphs/bedroom_distribution.png")
plt.show()
print("Pie chart successfully generated and saved as 'bedroom_distribution.png'")

'''
=================================================================================================================================
                                     🔴 SCENARIO 5: Advanced Analysis + Multiple Graphs
=================================================================================================================================
�� Part 1: Feature Creation
Create a new column:
Price Category
● price >= 1000000 → "Luxury"
● 500000 – 999999 → "Mid Range"
● < 500000 → "Affordable"
�� Part 2: NumPy Usage
1. Convert price column to a NumPy array.
2. Calculate price differences using:
np.diff()
�� Part 3: Visualizations
�� Line Graph
Plot price trend for all houses
�� Stacked Bar Chart
Show count of Price Category per Bedrooms.
�� Histogram
Plot distribution of:
● price
�� Part 4: Save All Graphs
plt.savefig("price_trend.png")
plt.savefig("price_category_stacked.png")
plt.savefig("price_histogram.png")
�� Part 5: Insights
Answer these:
1. Which bedroom category has the most expensive houses?
2. Which price category is most common?
3. What is the distribution pattern of house prices?
○ Right-skewed?
○ Normal?
○ Concentrated in a lower price range?
'''


# ==============================
# Part 1: Feature Creation
# ==============================

# Convert price to numeric (safety)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Create Price Category column
def categorize_price(price):
    if price >= 1000000:
        return "Luxury"
    elif price >= 500000:
        return "Mid Range"
    else:
        return "Affordable"

df["price_category"] = df["price"].apply(categorize_price)

print("\nPrice Category Counts:")
print(df["price_category"].value_counts())


# ==============================
# Part 2: NumPy Usage
# ==============================

# Convert price column to NumPy array
price_array = df["price"].to_numpy()

# Calculate price differences
price_diff = np.diff(price_array)

print("\nFirst 10 Price Differences:")
print(price_diff[:10])


# ==============================
# Part 3: Visualizations
# ==============================

# -------- 1. Line Graph --------
price_array = df["price"].dropna().to_numpy()

plt.figure(figsize=(10,5))
plt.plot(price_array[:100], marker='o', color="green")

plt.title("House Price Trend")
plt.xlabel("Index")
plt.ylabel("Price")

plt.tight_layout()
plt.savefig("graphs/price_trend.png")
plt.show()

#---------2. Stacked Bar Chart-----------
# Clean bedrooms column
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["bedrooms"] = df["bedrooms"].round()

# Remove unrealistic values (optional but recommended)
df = df[df["bedrooms"] <= 10]

# Group by bedrooms and price category
stack_data = df.groupby(["bedrooms", "price_category"]).size().unstack(fill_value=0)

# Select top bedroom categories (important fix)
stack_data = stack_data.head(5)

# Plot stacked bar chart
stack_data.plot(kind='bar', figsize=(10,6))

plt.title("Price Category Distribution by Bedrooms", pad=15)
plt.xlabel("Bedrooms")
plt.ylabel("Count")

plt.xticks(rotation=0)
plt.legend(title="Price Category")

plt.tight_layout()
plt.savefig("graphs/price_category_stacked.png")
plt.show()

# -------- 3. Histogram --------
plt.figure(figsize=(10,5))
upper_limit = df["price"].quantile(0.95)
filtered_prices = df[df["price"] <= upper_limit]["price"]
plt.hist(filtered_prices, bins=30, color = "gold")
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.ticklabel_format(style='plain', axis='x')
plt.tight_layout()
plt.savefig("graphs/price_histogram.png")
plt.show()
# ==============================
# Part 5: Insights
# ==============================

print("\n========== INSIGHTS ==========")

# 1. Bedroom category with most expensive houses
expensive = df[df["price_category"] == "Luxury"]
top_bedroom = expensive["bedrooms"].value_counts().idxmax()

print("1. Bedroom category with most expensive houses:", top_bedroom)

# 2. Most common price category
common_category = df["price_category"].value_counts().idxmax()
print("2. Most common price category:", common_category)

# 3. Distribution pattern
print("3. Price distribution is right-skewed (most houses are in lower price range with few very high values).")


'''
================================================================================================================
-----------------------------------------------------THE END----------------------------------------------------
================================================================================================================
'''

