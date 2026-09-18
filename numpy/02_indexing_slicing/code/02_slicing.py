# 02_indexing_slicing/code/02_slicing.py
# Slicing — extracting parts of arrays

import numpy as np

# === 1D slicing ===
arr_1d = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(f"Original: {arr_1d}")

print("\n=== 1D Slicing ===")
print(f"arr[2:5]:   {arr_1d[2:5]}")     # [2 3 4]
print(f"arr[:4]:    {arr_1d[:4]}")      # [0 1 2 3]
print(f"arr[6:]:    {arr_1d[6:]}")      # [6 7 8 9]
print(f"arr[::2]:   {arr_1d[::2]}")     # [0 2 4 6 8] — step 2
print(f"arr[::-1]:  {arr_1d[::-1]}")    # [9 8 7 6 5 4 3 2 1 0] — reversed

# === 2D slicing ===
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(f"\n=== 2D Array ===\n{arr_2d}")

print("\n=== 2D Slicing ===")
print(f"arr[0:2, 1:3]:\n{arr_2d[0:2, 1:3]}")   # rows 0-1, cols 1-2
print(f"\narr[:, 0]:  {arr_2d[:, 0]}")         # all rows, col 0
print(f"arr[1, :]:  {arr_2d[1, :]}")           # row 1, all columns
print(f"\narr[::2, ::2]:\n{arr_2d[::2, ::2]}") # every 2nd row and column

# === Slicing returns a VIEW ===
print("\n=== Slicing returns a view ===")
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
view[0] = 99
print(f"After view[0] = 99:")
print(f"  original: {original}")   # [1 99 3 4 5]
print(f"  view:     {view}")        # [99 3 4]