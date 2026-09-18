# 03_operations_broadcasting/exercises/exercise_06.py
# Exercise 06: Aggregation, Broadcasting, and Edge Cases
#
# Requirements:
# 1. Create a 3x4 matrix with random values between 1 and 100
# 2. Compute sum, mean, std per row (axis=1) and per column (axis=0)
# 3. Compute the column means with keepdims=True and normalize the matrix
# 4. Create an array with NaN values, compute nanmean and nansum
# 5. Compute cumsum of a 1D array

import numpy as np

np.random.seed(42)

# 1. Random matrix
matrix = np.random.randint(1, 100, (3, 4))
print(f"Matrix:\n{matrix}")

# 2. Aggregations per axis
print(f"\nSum per row:  {np.sum(matrix, axis=1)}")
print(f"Sum per col:  {np.sum(matrix, axis=0)}")
print(f"Mean per row: {np.mean(matrix, axis=1)}")
print(f"Mean per col: {np.mean(matrix, axis=0)}")
print(f"Std per row:  {np.std(matrix, axis=1)}")
print(f"Std per col:  {np.std(matrix, axis=0)}")

# 3. Normalize with keepdims
col_means = np.mean(matrix, axis=0, keepdims=True)
normalized = matrix - col_means
print(f"\nNormalized (each column mean 0):\n{normalized}")
print(f"Column means after normalization: {np.mean(normalized, axis=0)}")

# 4. NaN handling
arr_with_nan = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])
print(f"\nArray with NaN: {arr_with_nan}")
print(f"nanmean: {np.nanmean(arr_with_nan):.2f}")
print(f"nansum:  {np.nansum(arr_with_nan)}")
print(f"Count NaN: {np.sum(np.isnan(arr_with_nan))}")

# 5. Cumulative sum
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"\nArray: {arr}")
print(f"Cumsum: {np.cumsum(arr)}")