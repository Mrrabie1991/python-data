# 01_intro_numpy/code/04_reshape_intro.py
# Introduction to reshape

import numpy as np

# Create 1D array of 12 elements
arr = np.arange(12)
print(f"Original: {arr}")
print(f"Shape: {arr.shape}")

# Reshape to 3x4
matrix = arr.reshape(3, 4)
print(f"\nReshaped to 3x4:\n{matrix}")
print(f"Shape: {matrix.shape}")

# Reshape to 2x6
matrix2 = arr.reshape(2, 6)
print(f"\nReshaped to 2x6:\n{matrix2}")

# Can also use -1 for auto-calculate
auto = arr.reshape(2, -1)  # -1 means "calculate this dimension"
print(f"\nReshaped with -1 (2x6):\n{auto}")