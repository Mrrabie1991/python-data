# 04_reshaping_manipulation/exercises/exercise_02.py
# Exercise 02: transpose
#
# Requirements:
# 1. Create a 3x4 matrix with np.arange(12).reshape(3, 4)
# 2. Compute .T and print the shape
# 3. Create a 3D array (2, 3, 4)
# 4. Transpose with transpose(2, 0, 1) and print new shape
# 5. Explain the axis permutation in a comment

import numpy as np

# 1. Create 3x4 matrix
matrix = np.arange(12).reshape(3, 4)
print(f"Matrix (shape {matrix.shape}):")
print(matrix)

# 2. Transpose (swaps axes)
transposed = matrix.T
print(f"\nTransposed (shape {transposed.shape}):")
print(transposed)
# Original: (3, 4) → Transposed: (4, 3)

# 3. Create 3D array
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"\n3D array (shape {arr_3d.shape})")

# 4. Custom transpose
# transpose(2, 0, 1) means:
#   new axis 0 = old axis 2 (size 4)
#   new axis 1 = old axis 0 (size 2)
#   new axis 2 = old axis 1 (size 3)
# Result shape: (4, 2, 3)
transposed_3d = arr_3d.transpose(2, 0, 1)
print(f"\nAfter transpose(2, 0, 1): shape {transposed_3d.shape}")
# (4, 2, 3)

# 5. Default .T reverses all axes
default_T = arr_3d.T
print(f"After .T: shape {default_T.shape}")
# (4, 3, 2)