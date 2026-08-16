#8. Pie Chart with Conditional Data
#Scenario:
#scores = np.array([40, 60, 80, 30, 90])
#Task:
#● Categorize into:
#○ Pass (>50)
#○ Fail (<=50)
#● Count using NumPy/Pandas
#● Plot pie chart for Pass vs Fail

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])
categories = np.where(scores > 50, "Pass", "Fail")

df = pd.DataFrame({
    "Score": scores,
    "Result": categories})

print(df)

counts = df["Result"].value_counts()

print("\nCounts:")
print(counts)

plt.pie(counts,labels=counts.index,autopct="%1.1f%%")

plt.title("Pass vs Fail")
plt.show()
