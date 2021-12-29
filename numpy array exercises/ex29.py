"""
Write a NumPy program to sort an along the first, last axis of an array. Go to the editor
Expected Output:
Original array:
[[4 6]
[2 1]]
Sort along the first axis:
[[2 1]
[4 6]]
Sort along the last axis:
[[1 2]
[4 6]]
"""

import numpy as np

x = np.array([[4, 6], [2, 1]])
print("Original array")
print(x)
print("Sort along the first axis")
print(np.sort(x, axis=0))
print("Sort along the last axis")
print(np.sort(x))

