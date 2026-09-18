# 04_reshaping_manipulation/code/02_ravel_flatten.py
# ravel vs flatten

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"Matrix:\n{matrix}")

# === ravel — returns view if possible ===
raveled = matrix.ravel()
raveled[0] = 99
print(f"\nraveled: {raveled}")
print(f"matrix after change:\n{matrix}")
# matrix[0, 0] changed to 99 — raveled is a view

# === Reset ===
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# === flatten — always returns copy ===
flattened = matrix.flatten()
flattened[0] = 99
print(f"\nflattened: {flattened}")
print(f"matrix after change:\n{matrix}")
# matrix unchanged — flattened is a copy

# === Check ownership ===
print(f"\nraveled.base is matrix:  {matrix.ravel().base is not None}")
print(f"flattened.base is matrix: {matrix.flatten().base is not None}")