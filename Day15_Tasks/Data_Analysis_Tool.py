#6. Data Analysis Tool (NumPy + Pandas)
#Scenario:
#Analyze student marks.
#Task:
#● Generate marks using NumPy
#● Convert into Pandas DataFrame
#● Use conditions to filter passing students
#● Calculate mean using math/NumPy
#● Use loop to print results

import numpy as np
import pandas as pd

marks = np.random.randint(30, 101, size=(5, 3))

df = pd.DataFrame(marks, columns=["Maths", "Science", "English"])

df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("Student Marks:")
print(df)

passing_students = df[df["Average"] >= 40]

print("\nPassing Students:")
print(passing_students)

mean_marks = np.mean(marks)

print("\nOverall Mean Marks:", mean_marks)

print("\nStudent Results:")

for index, row in df.iterrows():
    if row["Average"] >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(
        "Student", index + 1,
        "- Total:", row["Total"],
        "- Average:", row["Average"],
        "- Result:", result
    )
