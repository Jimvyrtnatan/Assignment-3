#Example 2 : Saving and Loading 1D Array

import numpy as np

# Create a sample 1D NumPy array
data = np.array([1, 2, 3, 4])

# Save the array to a file
np.save("one_d_array.npy", data)

# Load the array from the file
loaded_data = np.load("one_d_array.npy")

print(loaded_data)