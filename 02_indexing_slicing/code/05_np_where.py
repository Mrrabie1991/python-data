# 02_indexing_slicing/code/05_np_where.py
# np.where — conditional selection

import numpy as np

arr = np.array([1, 5, 8, 3, 10, 2, 7, 4])
print(f"Original: {arr}")

# === Select values ===
# Where arr > 5, take 100. Else take 0.
result = np.where(arr > 5, 100, 0)
print(f"\nnp.where(arr > 5, 100, 0):\n{result}")
# [0 0 100 0 100 0 100 0]

# === Keep original or replace ===
result2 = np.where(arr > 5, arr, 0)
print(f"\nnp.where(arr > 5, arr, 0):\n{result2}")
# [0 0 8 0 10 0 7 0]

# === Find indices ===
indices = np.where(arr > 5)
print(f"\nIndices where arr > 5: {indices}")
# (array([2, 4, 6]),)

# Direct access to indices array
print(f"Indices: {indices[0]}")   # [2 4 6]

# === 2D np.where ===
matrix = np.array([
    [1, 5, 2],
    [8, 3, 9],
    [4, 7, 6]
])
print(f"\n=== 2D ===\n{matrix}")

where_result = np.where(matrix > 5, "big", "small")
print(f"\nnp.where(matrix > 5, 'big', 'small'):\n{where_result}")

# Find 2D indices
indices_2d = np.where(matrix > 5)
print(f"\nIndices of elements > 5:")
print(f"  rows: {indices_2d[0]}")
print(f"  cols: {indices_2d[1]}")