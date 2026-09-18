# 01_numpy_basics/code/01_why_numpy.py
# Why NumPy?

import numpy as np

# Compare list and array
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

# List * 2 repeats the sequence
print(f"List * 2:  {py_list * 2}")     # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Array * 2 multiplies each element
print(f"Array * 2: {np_array * 2}")    # [2 4 6 8 10]

# Check types
print(f"\nList type:  {type(py_list)}")     # <class 'list'>
print(f"Array type: {type(np_array)}")      # <class 'numpy.ndarray'>

# Check dtype
print(f"\nArray dtype: {np_array.dtype}")   # int64