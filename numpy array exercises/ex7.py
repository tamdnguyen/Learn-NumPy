"""
Write a NumPy program to convert an array to a float type. Go to the editor
Sample output:
Original array
[1, 2, 3, 4]
Array converted to a float type:
[ 1. 2. 3. 4.]

"""

import numpy as np

x = np.arange(1, 5)
y = x.astype(float)

print("Original array")
print(x)
print("Array converted to a float type:")
print(y)
