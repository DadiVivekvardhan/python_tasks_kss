#7. Filtered Bar Chart
#Scenario:
#marks = np.array([45, 80, 60, 30, 90])
#names = ["A", "B", "C", "D", "E"]
#Task:
#● Convert to DataFrame
#● Filter students with marks > 50
#● Plot bar chart only for filtered students

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks})

print("Original DataFrame:")
print(df)

filtered_df = df[df["Marks"] > 50]

print("\nFiltered DataFrame:")
print(filtered_df)

plt.bar(filtered_df["Name"], filtered_df["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students with Marks Greater Than 50")

plt.show()
