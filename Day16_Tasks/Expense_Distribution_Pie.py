#3. Expense Distribution Pie Chart
#Scenario:
#Monthly expenses:
#expenses = np.array([500, 300, 200])
#labels = ["Food", "Rent", "Travel"]
#Task:
#● Create a pie chart
#● Show percentage distribution

import numpy as np
import matplotlib.pyplot as plt

expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

plt.pie(expenses,labels=labels,autopct="%1.1f%%")

plt.title("Monthly Expense Distribution")
plt.show()
