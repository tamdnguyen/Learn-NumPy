"""
Write a NumPy program to convert a list and tuple into arrays. Go to the editor

Input:
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
[1 2 3]]

SAMPLE SOLUTION: using np.asarray()
"""

import numpy as np

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

lst = np.array(my_list)
tupl = np.array(my_tuple)

print("List to array:")
print(lst)
print("Tuple to array:")
print(tupl)
