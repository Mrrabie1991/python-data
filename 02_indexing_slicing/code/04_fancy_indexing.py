# 02_indexing_slicing/code/04_fancy_indexing.py
# Fancy indexing — indexing with arrays

import numpy as np

# === 1D fancy indexing ===
arr = np.array([10, 20, 30, 40, 50])

print(f"Original: {arr}")
print(f"arr[[0, 2, 4]]: {arr[[0, 2, 4]]}")   # [10 30 50]
print(f"arr[[4, 3, 2]]: {arr[[4, 3, 2]]}")   # [50 40 30] — reorder

# === Repeating indices ===
print(f"\narr[[0, 0, 1, 1]]: {arr[[0, 0, 1, 1]]}")  # [10 10 20 20]

# === 2D fancy indexing ===
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\n=== 2D ===\n{matrix}")

# Select rows
rows = [0, 2]
print(f"\nmatrix[[0, 2]]:\n{matrix[[0, 2]]}")

# Select specific elements (row, col) pairs
print(f"\nmatrix[[0, 1, 2], [0, 1, 2]]: {matrix[[0, 1, 2], [0, 1, 2]]}")
# [1 5 9] — diagonal

# === Fancy indexing returns a COPY ===
arr = np.array([1, 2, 3, 4, 5])
selected = arr[[0, 2, 4]]
selected[0] = 99
print(f"\nAfter selected[0] = 99:")
print(f"  arr:      {arr}")        # [1 2 3 4 5] — unchanged
print(f"  selected: {selected}")   # [99 3 5]