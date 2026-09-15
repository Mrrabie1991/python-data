# 01_intro_numpy/code/01_first_array.py
# First steps with NumPy

import numpy as np

# %% Cell 1: Create array from a list
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Type: {type(arr)}")
print(f"Data type: {arr.dtype}")

# %% Cell 2: Compare with a Python list
py_list = [1, 2, 3, 4, 5]
print(f"\nPython list * 2: {py_list * 2}")    # Repeats the list!
print(f"NumPy array * 2: {arr * 2}")           # Multiplies each element!

