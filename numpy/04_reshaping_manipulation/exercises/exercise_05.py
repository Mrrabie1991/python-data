# 04_reshaping_manipulation/exercises/exercise_05.py
# Exercise 05: View vs Copy
#
# Requirements:
# 1. Create arr = np.arange(10)
# 2. Create a view via slicing and modify it. Print original
# 3. Create a copy via .copy() and modify it. Print original
# 4. Check .base for view, copy, reshape, flatten, astype
# 5. Summarize which operations return views vs copies in a comment

import numpy as np

arr = np.arange(10)
print(f"Original: {arr}")

# 2. View via slicing
view = arr[2:7]
view[0] = 99
print(f"\nAfter view[0] = 99:")
print(f"arr: {arr}")
# arr[2] changed — view shares data

# 3. Copy
arr = np.arange(10)  # Reset
copy = arr[2:7].copy()
copy[0] = 99
print(f"\nAfter copy[0] = 99:")
print(f"arr: {arr}")
# arr unchanged — copy has own data

# 4. Check .base
print(f"\n=== .base checks ===")
print(f"slice view: base is not None → {arr[2:7].base is not None}")     # True
print(f"copy: base is None → {arr[2:7].copy().base is None}")           # True
print(f"reshape: base is not None → {arr.reshape(2, 5).base is not None}")  # True
print(f"flatten: base is None → {arr.reshape(2, 5).flatten().base is None}")  # True
print(f"astype: base is None → {arr.astype(np.float64).base is None}")   # True

# 5. Summary:
# Views: slicing, reshape, ravel, transpose, .T
# Copies: copy(), flatten(), astype(), arithmetic operations (+, *), boolean masking, fancy indexing