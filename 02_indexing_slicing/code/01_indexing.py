# 02_indexing_slicing/code/01_indexing.py
# Indexing — accessing array elements

import numpy as np

# === 1D array ===
arr_1d = np.array([10, 20, 30, 40, 50])

print("=== 1D ===")
print(f"arr_1d[0]:  {arr_1d[0]}")      # 10 — first element
print(f"arr_1d[2]:  {arr_1d[2]}")      # 30
print(f"arr_1d[-1]: {arr_1d[-1]}")     # 50 — last element
print(f"arr_1d[-2]: {arr_1d[-2]}")     # 40 — second to last

# === 2D array ===
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n=== 2D ===")
print(f"arr_2d[0, 0]: {arr_2d[0, 0]}")    # 1 — top-left
print(f"arr_2d[1, 2]: {arr_2d[1, 2]}")    # 6 — row 1, col 2
print(f"arr_2d[-1, -1]: {arr_2d[-1, -1]}") # 9 — bottom-right

# Row-wise access
print(f"\narr_2d[0] (first row):   {arr_2d[0]}")     # [1 2 3]
print(f"arr_2d[1] (second row):  {arr_2d[1]}")       # [4 5 6]