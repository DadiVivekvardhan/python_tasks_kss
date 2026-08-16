#3. Employee Salary Insights
#Scenario:
#salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
#departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
#Task:
#● Convert into DataFrame
#● Plot:
#○ Line graph → salary trend
#○ Bar chart → department-wise salary comparison
#○ Pie chart → department distribution
#○ Histogram → salary distribution
#○ Scatter plot → index vs salary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({"Department": departments,"Salary": salaries})
print(df)

plt.subplot(2, 3, 1)
plt.plot(df.index, df["Salary"], marker="o")
plt.title("Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid(True)

department_salary = df.groupby("Department")["Salary"].mean()

plt.subplot(2, 3, 2)
plt.bar(department_salary.index, department_salary.values)
plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

department_count = df["Department"].value_counts()

plt.subplot(2, 3, 3)
plt.pie(
    department_count.values,
    labels=department_count.index,
    autopct="%1.1f%%")
plt.title("Department Distribution")

plt.subplot(2, 3, 4)
plt.hist(df["Salary"], bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Salary"])
plt.title("Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()
