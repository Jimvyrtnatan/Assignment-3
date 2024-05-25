#Example 3: Saving and Loading Multiple Arrays

import numpy as np

# Create sample multiple arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Save both arrays to a single file using savez()
np.savez("multiple_arrays.npz", arr1=array1, arr2=array2)

# Load both arrays from the file using load()
loaded_arrays = np.load("multiple_arrays.npz")

print(loaded_arrays["arr1"])
print(loaded_arrays["arr2"])