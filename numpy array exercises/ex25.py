"""
Write a NumPy program to construct an array by repeating. Go to the editor

Sample array: [1, 2, 3, 4]
Expected Output:
Original array
[1, 2, 3, 4]
Repeating 2 times
[1 2 3 4 1 2 3 4]
Repeating 3 times
[1 2 3 4 1 2 3 4 1 2 3 4]
"""

import numpy as np

x = np.array([1, 2, 3, 4])
print("Original array")
print(x)
print("Repeating 2 times")
print(np.hstack([x]*2))
print("Repeating 3 times")
print(np.tile(x, 3))
