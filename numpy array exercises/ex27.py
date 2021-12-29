"""
Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array. Go to the editor
Original array: [1 2 3 4 5 6]
Maximum Values: 5
Minimum Values: 0

"""

import numpy as np

x = np.array([1, 2, 0, 3, 4, 10, 5, 6])
print(x.argmax())
print((x.argmin()))
