#5. Product Sales Bar Chart
#Scenario:
#products = ["Pen", "Book", "Pencil"]
#sales = np.array([50, 80, 40])
#Task:
#● Create DataFrame
#● Plot bar chart
#● Add labels and title

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

df = pd.DataFrame({
    "Product": products,
    "Sales": sales})
print(df)

plt.bar(df["Product"], df["Sales"])

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()
