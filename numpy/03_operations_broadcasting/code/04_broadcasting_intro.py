# 03_operations_broadcasting/code/04_broadcasting_intro.py
# Broadcasting — concept and examples

import numpy as np

# === Scalar + Array ===
arr = np.array([1, 2, 3, 4, 5])
print(f"arr + 10: {arr + 10}")     # [11 12 13 14 15]
print(f"arr * 2:  {arr * 2}")      # [2 4 6 8 10]

# === 1D + 2D ===
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])

print(f"\nmatrix:\n{matrix}")
print(f"\nrow: {row}")

result = matrix + row
print(f"\nmatrix + row:\n{result}")
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]
# row broadcast to each row of matrix

# === Column vector broadcast ===
col = np.array([[100], [200], [300]])
print(f"\ncol:\n{col}")

result2 = matrix + col
print(f"\nmatrix + col:\n{result2}")
# [[101 102 103]
#  [204 205 206]
#  [307 308 309]]
# col broadcast to each column of matrix

# === Shape inspection ===
print(f"\nmatrix.shape: {matrix.shape}")   # (3, 3)
print(f"row.shape:    {row.shape}")        # (3,)
print(f"col.shape:    {col.shape}")        # (3, 1)