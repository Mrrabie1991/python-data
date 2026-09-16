# 01_numpy_basics/code/06_view_vs_copy.py
# View vs Copy — conceptual introduction

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Original: {arr}")

# View — shares data
view = arr[1:4]
view[0] = 99
print(f"\nAfter changing view[0] to 99:")
print(f"  arr:  {arr}")    # [1, 99, 3, 4, 5]
print(f"  view: {view}")   # [99 3 4]

# Reset
arr = np.array([1, 2, 3, 4, 5])

# Copy — separate data
copy = arr[1:4].copy()
copy[0] = 77
print(f"\nAfter changing copy[0] to 77:")
print(f"  arr:  {arr}")    # [1, 2, 3, 4, 5]
print(f"  copy: {copy}")   # [77 3 4]

# Check if array owns its data
print(f"\narr owns data:  {arr.base is None}")   # True
print(f"view owns data: {view.base is not None}") # True — it's a view
print(f"copy owns data: {copy.base is None}")     # True