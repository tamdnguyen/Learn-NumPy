"""
Write a NumPy program to create a null vector of size 10 and update sixth value to 11.Go to the editor
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

"""

import numpy as np

a = np.zeros(10)
print(a)
a[6] = 11
print("Update sixth value to 11")
print(a)
