# 01_intro_numpy/exercises/exercise_03.py
# Exercise 03: Difference between list and array

import numpy as np

py_list = [1, 2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])

# List repeats — Python list is a sequence, not a numeric vector
print(py_list * 2)   # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Array multiplies each element — NumPy applies operation element-wise
print(arr * 2)       # [2, 4, 6, 8, 10]

# The difference: list * 2 repeats the sequence,
# while array * 2 performs element-wise multiplication.