#7. Replace Values Using NumPy + Pandas
#A Series:
#S = pd.Series([10, 50, 30, 80, 20])
#Task:
#● Replace values greater than 40 with 0 using NumPy logic
#● Return updated Series

import pandas as pd
import numpy as np

S = pd.Series([10, 50, 30, 80, 20])

print("Before update:")
print(S)

S[S > 40] = 0

print("After Update:")
print(S)
