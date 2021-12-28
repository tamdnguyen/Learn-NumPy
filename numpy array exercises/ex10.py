"""
Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern. Go to the editor
Checkerboard pattern:
[[0 1 0 1 0 1 0 1]
..........
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]]

"""

import numpy as np

x = np.ones((8, 8))
"""
We start with the original array with full of ones like this
[[1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]]
 """

x[::2, ::2] = 0
"""
Next, for the row with even indices (i.e., row 0, 2, 4, 6), we change the number with even indices (also 0, 2, 4, 6)
to 0 using slicing.

[[0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]]

"""

x[1::2, 1::2] = 0
"""
Next, for the row with odd indices (1, 3, 5, 7), the elements with odd indices are changed to 0 using slicing.
Ultimately, we have a checkerboard pattern.
"""
print("Checkerboard pattern:")
print(x)
