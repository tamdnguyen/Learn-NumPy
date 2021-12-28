"""
Write a NumPy program to convert the values of Fahrenheit degrees into Centigrade degrees.
Centigrade values are stored into a NumPy array. Go to the editor

Sample Array [0, 12, 45.21 ,34, 99.91]
Expected Output:
Values in Fahrenheit degrees:
[ 0. 12. 45.21 34. 99.91]
Values in Centigrade degrees:
[-17.77777778 -11.11111111 7.33888889 1.11111111 37.72777778]

"""

import numpy as np

f_lst = [0, 12, 45.21, 34, 99.91]
f = np.asarray(f_lst)
conversion_lst = np.full((len(f_lst),), 32)
c = (f - conversion_lst) * 5/9

print("Values in Fahrenheit degrees:")
print(f)
print("Values in Centigrade degrees:")
print(c)
