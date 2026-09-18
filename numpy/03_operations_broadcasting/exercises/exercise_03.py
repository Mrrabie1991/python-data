# 03_operations_broadcasting/exercises/exercise_03.py
# Exercise 03: Basic Broadcasting
#
# Requirements:
# 1. Create matrix = np.arange(1, 13).reshape(3, 4)
# 2. Create row = np.array([10, 20, 30, 40])
# 3. Add row to each row of matrix (broadcast)
# 4. Create col = np.array([[100], [200], [300]])
# 5. Add col to each column of matrix
# 6. Multiply matrix by scalar 5

import numpy as np

# 1. Matrix
matrix = np.arange(1, 13).reshape(3, 4)
print(f"matrix:\n{matrix}")

# 2-3. Add row (broadcast across rows)
row = np.array([10, 20, 30, 40])
result_row = matrix + row
print(f"\nmatrix + row:\n{result_row}")
# row shape (4,) broadcast to (3, 4)

# 4-5. Add column (broadcast across columns)
col = np.array([[100], [200], [300]])
result_col = matrix + col
print(f"\nmatrix + col:\n{result_col}")
# col shape (3, 1) broadcast to (3, 4)

# 6. Scalar multiply
result_scalar = matrix * 5
print(f"\nmatrix * 5:\n{result_scalar}")