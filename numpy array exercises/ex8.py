"""
Write a NumPy program to create a 2d array with 1 on the border and 0 inside. Go to the editor
Expected Output:
Original array:
[[ 1. 1. 1. 1. 1.]
...................
[ 1. 1. 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 1. 1. 1. 1. 1.]
...................
[ 1. 1. 1. 1. 1.]]

IMPORTANT
Explanation about slicing, indexing arrays here:
https://towardsdatascience.com/slicing-numpy-arrays-like-a-ninja-e4910670ceb0

"""

import numpy as np

x = np.ones((5, 5))
print("Original array:")
print(x)

x[1:-1, 1:-1] = 0
print("1 on the border and 0 inside in the array")
print(x)
