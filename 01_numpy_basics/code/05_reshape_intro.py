# 01_numpy_basics/code/05_reshape_intro.py
# Introduction to reshape

import numpy as np

# Create 1D array of 12 elements
arr = np.arange(12)
print(f"Original: {arr}")           # [0 1 2 ... 11]
print(f"Shape:    {arr.shape}")     # (12,)

# Reshape to 3x4
matrix = arr.reshape(3, 4)
print(f"\nReshaped to 3x4:\n{matrix}")
print(f"Shape: {matrix.shape}")     # (3, 4)

# Use -1 for auto-calculate
auto = arr.reshape(2, -1)
print(f"\nReshaped to 2 rows (auto cols):\n{auto}")
print(f"Shape: {auto.shape}")       # (2, 6)

# Flatten back to 1D
flat = matrix.reshape(-1)
print(f"\nFlattened: {flat}")
print(f"Shape: {flat.shape}")       # (12,)