"""
 Write a NumPy program to sort pairs of first name and last name return their indices.
 (first by last name, then by first name). Go to the editor
first_names = (Betsey, Shelley, Lanell, Genesis, Margery)
last_names = (Battle, Brien, Plotner, Stahl, Woolum)
Expected Output:
[1 3 2 4 0]

BETTER EXAMPLE TO UNDERSTAND
surnames =    ('Hertz',    'Galilei', 'Hertz')
first_names = ('Heinrich', 'Galileo', 'Gustav')

Here we first sort using last name, then we will have [1, 2, 0] or [1, 0, 2] because 'Galilei' first
then 'Hertz' but there are two hertz.

So we use the fisrt name to sort these 2 hertz, and then we have our sorted names.
"""

import numpy as np

first_names = ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
last_names = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')

x = np.lexsort((first_names, last_names))
print(x)