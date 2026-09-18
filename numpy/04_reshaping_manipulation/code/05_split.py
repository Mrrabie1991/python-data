# 04_reshaping_manipulation/code/05_split.py
# split, hsplit, vsplit

import numpy as np

# === 1D split ===
arr = np.arange(12)
print(f"Array: {arr}")

parts = np.split(arr, 3)
print(f"\nSplit into 3 parts:")
for i, p in enumerate(parts):
    print(f"  Part {i}: {p}")

# === Split at specific indices ===
parts = np.split(arr, [3, 7])
print(f"\nSplit at [3, 7]:")
for i, p in enumerate(parts):
    print(f"  Part {i}: {p}")

# === 2D split ===
matrix = np.arange(16).reshape(4, 4)
print(f"\nMatrix:\n{matrix}")

# Vertical split (rows)
vparts = np.vsplit(matrix, 2)
print(f"\nvsplit into 2:")
for i, p in enumerate(vparts):
    print(f"  Part {i}:\n{p}")

# Horizontal split (columns)
hparts = np.hsplit(matrix, 2)
print(f"\nhsplit into 2:")
for i, p in enumerate(hparts):
    print(f"  Part {i}:\n{p}")