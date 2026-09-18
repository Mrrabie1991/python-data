# 02_indexing_slicing/exercises/exercise_02.py
# Exercise 02: 2D Indexing
#
# Requirements:
# 1. Create a 4x4 matrix using np.arange(16).reshape(4, 4)
# 2. Access element at row 2, column 3
# 3. Extract the second row
# 4. Extract the third column
# 5. Extract the top-left 2x2 sub-matrix
# 6. Extract the bottom-right 2x2 sub-matrix

import numpy as np

matrix = np.arange(16).reshape(4, 4)
print(f"Matrix:\n{matrix}")

# 2. Element at (2, 3)
print(f"\nmatrix[2, 3]: {matrix[2, 3]}")   # 11

# 3. Second row (index 1)
print(f"matrix[1]:    {matrix[1]}")        # [4 5 6 7]

# 4. Third column (index 2)
print(f"matrix[:, 2]: {matrix[:, 2]}")     # [2 6 10 14]

# 5. Top-left 2x2
print(f"\nTop-left 2x2:\n{matrix[:2, :2]}")
# [[0 1]
#  [4 5]]

# 6. Bottom-right 2x2
print(f"\nBottom-right 2x2:\n{matrix[2:, 2:]}")
# [[10 11]
#  [14 15]]