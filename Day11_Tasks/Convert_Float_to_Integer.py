#Q. Convert Float Prices to Integer
#A shop stores product prices:
#[10.5, 20.8, 15.3]
#Scenario:
#The billing system requires integer values.
#Task:
#● Convert the array from float to integer using astype().

import numpy as np

prices = np.array([10.5, 20.8, 15.3])

int_prices = prices.astype(int)

print("Original Prices:", prices)
print("Original Data Type:", prices.dtype)

print("Integer Prices:", int_prices)
print("New Data Type:", int_prices.dtype)
