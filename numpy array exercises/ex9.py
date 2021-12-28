"""
Write a NumPy program to add a border (filled with 0's) around an existing array. Go to the editor
Expected Output:
Original array:
[[ 1. 1. 1.]
[ 1. 1. 1.]
[ 1. 1. 1.]]
0 on the border and 1 inside in the array
[[ 0. 0. 0. 0. 0.]
...........
[ 0. 0. 0. 0. 0.]]

"""

import numpy as np

x = np.ones((3, 3))
y = np.pad(x, (1, 1), mode='constant', constant_values=0)

print("Original array:")
print(x)
print("0 on the border and 1 inside in the array")
print(y)

