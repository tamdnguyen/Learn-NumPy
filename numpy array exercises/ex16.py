"""
Write a NumPy program to find the number of elements of an array,
length of one array element in bytes and total bytes consumed by the elements. Go to the editor
Expected Output:
Size of the array: 3
Length of one array element in bytes: 8
Total bytes consumed by the elements of the array: 24

"""

import numpy as np

x = np.array([1, 2, 3], dtype=np.float64)
print("Size of the array:", x.size)
print("Length of one array element in bytes:", x.itemsize)
print("Total bytes consumed by the elements of the array:", x.nbytes)
