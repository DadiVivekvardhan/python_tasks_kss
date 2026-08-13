#7. Data Alignment Issue in Series Addition
#Two Series:
#S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
#S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
#Task:
#● Add both Series
#● Explain why some values become NaN
#● Replace NaN with 0 and compute final result

import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

result = S1 + S2
print("After addition:")
print(result)

result = result.fillna(0)
print("\nAfter replacing NaN with 0:")
print(result)

#If an index is missing in one Series, Pandas cannot perform the addition for that index, so it gives NaN (Not a Number).
