# 01_intro_numpy/exercises/exercise_02.py
# Exercise 02: Array attributes
# Exercise 04: Reshape (combined)

import numpy as np

# === Exercise 02: Basic attributes ===

# 2D array 3x4
arr_2d = np.arange(12).reshape(3, 4)

print(f"shape: {arr_2d.shape}")    # Rows and columns
print(f"size: {arr_2d.size}")      # Total number of elements
print(f"ndim: {arr_2d.ndim}")      # Number of dimensions
print(f"dtype: {arr_2d.dtype}")    # Data type of all elements

print()

# === Exercise 04: Reshape ===

# Create 1D array of 24 elements
arr_1d = np.arange(24)

# Reshape to 4x6
arr_4x6 = arr_1d.reshape(4, 6)
print(f"shape: {arr_4x6.shape}")   # (4, 6)
print(f"size: {arr_4x6.size}")     # 24
print(f"ndim: {arr_4x6.ndim}")     # 2

print()

# Reshape to 3D: 2x3x4
arr_3d = arr_1d.reshape(2, 3, 4)
print(f"shape: {arr_3d.shape}")    # (2, 3, 4)
print(f"ndim: {arr_3d.ndim}")      # 3