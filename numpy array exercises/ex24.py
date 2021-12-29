"""
Write a NumPy program to test whether any array element along a given axis evaluates to True.

"""

import numpy as np

print(np.all([[True,False],[True,True]], axis=0))
print(np.all([[True,False],[True,True]], axis=1))
print(np.all([[True,True],[True,True]]))
print(np.all([10, 20, 0, -50], axis=0))
print(np.all([10, 20, -50]))