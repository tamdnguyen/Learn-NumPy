"""
Write a NumPy program to repeat elements of an array. Go to the editor
Expected Output:
[3 3 3 3]
[1 1 2 2 3 3 4 4]
"""

import numpy as np

print(np.repeat(3, 4))
x = np.array([[1,2],[3,4]])
print(x)
print(np.repeat([1,2,3,4], 2))
print(np.repeat(x, 2))
print(np.repeat(x, 3, axis=1))
print(np.repeat(x, [2,3], axis=0))





