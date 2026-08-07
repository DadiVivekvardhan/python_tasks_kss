#3. Product Rating System
#An e-commerce website stores product ratings:
#[4, 5, 3, 4, 2]
#Task:
#● Convert it to a NumPy array.
#● Print the first and last rating using indexing.

import numpy as np

ratings = [4, 5, 3, 4, 2]

ratings_array = np.array(ratings)

print("Ratings:", ratings_array)
print("First Rating:", ratings_array[0])
print("Last Rating:", ratings_array[-1])
