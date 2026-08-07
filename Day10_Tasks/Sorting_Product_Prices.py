#3. Sorting Product Prices
#An e-commerce company stores product prices in a NumPy array.
#Scenario:
#Prices = [499, 299, 799, 199, 599]
#Task:
#● Convert it into a NumPy array.
#● Sort the prices in ascending order


import numpy as np

prices = [499, 299, 799, 199, 599]

prices_array = np.array(prices)

sorted_prices = np.sort(prices_array)

print("Original Prices:", prices_array)
print("Sorted Prices:", sorted_prices)
