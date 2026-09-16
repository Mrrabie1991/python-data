# 02_indexing_slicing/code/03_boolean_masking.py
# Boolean masking — filtering arrays with conditions

import numpy as np

arr = np.array([1, 5, 8, 3, 10, 2, 7, 4])

print(f"Original: {arr}")

# === Basic mask ===
mask = arr > 5
print(f"\nMask (arr > 5): {mask}")
print(f"Filtered:       {arr[mask]}")   # [8 10 7]

# === Direct syntax ===
print(f"\narr[arr > 5]: {arr[arr > 5]}")   # [8 10 7]

# === Even numbers ===
evens = arr[arr % 2 == 0]
print(f"Evens:        {evens}")   # [8 10 2 4]

# === Combined conditions ===
between = arr[(arr > 3) & (arr < 8)]
print(f"\nBetween 3 and 8: {between}")   # [5 7 4]

outside = arr[(arr < 3) | (arr > 8)]
print(f"Outside 3-8:     {outside}")      # [1 10 2]

# === NOT ===
not_greater = arr[~(arr > 5)]
print(f"\nNOT greater than 5: {not_greater}")   # [1 5 3 2 4]

# === 2D boolean masking ===
matrix = np.array([
    [1, 5, 2],
    [8, 3, 9],
    [4, 7, 6]
])
print(f"\n=== 2D ===\n{matrix}")
print(f"Elements > 4: {matrix[matrix > 4]}")
# [5 8 9 7 6] — flattened!

# === Count elements matching ===
print(f"\nCount > 5: {np.sum(arr > 5)}")     # 3
print(f"Count even: {np.sum(arr % 2 == 0)}") # 4