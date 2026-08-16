#2. Monthly Sales Analysis
#Scenario:
#sales = np.array([100, 150, 200, 180, 220, 300])
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#Task:
#● Create DataFrame
#● Plot:
#○ Line graph → sales trend
#○ Bar chart → month-wise comparison
#○ Pie chart → contribution of each month
#○ Histogram → frequency of sales values
#○ Scatter plot → month index vs sales

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({
    "Month": months,
    "Sales": sales})
print(df)

plt.subplot(2, 3, 1)
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(df["Month"], df["Sales"])
plt.title("Month-wise Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.subplot(2, 3, 3)
plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
plt.title("Monthly Sales Contribution")

plt.subplot(2, 3, 4)
plt.hist(df["Sales"], bins=5, edgecolor="black")
plt.title("Sales Frequency Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Sales"])
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")


plt.tight_layout()

plt.show()
