# 04_reshaping_manipulation/exercises/exercise_01.py
# Exercise 01: reshape and ravel
#
# Requirements:
# 1. Create np.arange(24)
# 2. Reshape to (4, 6), print shape
# 3. Reshape to (2, 3, 4), print shape
# 4. Use ravel() on the 3D array and print the result
# 5. Use flatten() and compare

import numpy as np

# 1. Original 1D array
arr = np.arange(24)
print(f"Original: {arr}")
print(f"Shape:    {arr.shape}")

# 2. Reshape to (4, 6)
matrix_4x6 = arr.reshape(4, 6)
print(f"\nReshaped (4, 6):")
print(matrix_4x6)
print(f"Shape: {matrix_4x6.shape}")

# 3. Reshape to (2, 3, 4)
tensor_2_3_4 = arr.reshape(2, 3, 4)
print(f"\nReshaped (2, 3, 4):")
print(tensor_2_3_4)
print(f"Shape: {tensor_2_3_4.shape}")

# 4. ravel — back to 1D
raveled = tensor_2_3_4.ravel()
print(f"\nRaveled: {raveled}")
print(f"Shape:   {raveled.shape}")

# 5. flatten — always a copy
flattened = tensor_2_3_4.flatten()
print(f"\nFlattened: {flattened}")
print(f"Shape:     {flattened.shape}")

# Compare view vs copy
raveled[0] = 999
flattened[0] = 777
print(f"\nAfter modifying raveled[0] = 999 and flattened[0] = 777:")
print(f"Original arr[0]: {arr[0]}")           # 999 — raveled was a view
print(f"Original arr remains same: {arr[0] == 999}")