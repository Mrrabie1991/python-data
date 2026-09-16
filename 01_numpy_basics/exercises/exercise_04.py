# 01_numpy_basics/exercises/exercise_04.py
# Exercise 04: Multi-dimensional reshape
#
# Requirements:
# 1. Create np.arange(24)
# 2. Reshape to (4, 6)
# 3. Print shape, ndim, size
# 4. Reshape to (2, 3, 4)
# 5. Print shape and ndim

import numpy as np

arr = np.arange(24)
print(f"Original: {arr}")
print(f"Shape:    {arr.shape}")

# Reshape to (4, 6)
arr_4x6 = arr.reshape(4, 6)
print(f"\nReshaped to (4, 6):")
print(arr_4x6)
print(f"shape: {arr_4x6.shape}")   # (4, 6)
print(f"ndim:  {arr_4x6.ndim}")    # 2
print(f"size:  {arr_4x6.size}")    # 24

# Reshape to (2, 3, 4)
arr_3d = arr.reshape(2, 3, 4)
print(f"\nReshaped to (2, 3, 4):")
print(arr_3d)
print(f"shape: {arr_3d.shape}")    # (2, 3, 4)
print(f"ndim:  {arr_3d.ndim}")     # 3