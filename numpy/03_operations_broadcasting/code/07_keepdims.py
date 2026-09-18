# 03_operations_broadcasting/code/07_keepdims.py
# keepdims — preserving dimensions after aggregation

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"Matrix (shape {matrix.shape}):\n{matrix}")

# === Without keepdims ===
mean_axis0 = np.mean(matrix, axis=0)
print(f"\nWithout keepdims (shape {mean_axis0.shape}):")
print(mean_axis0)   # [4. 5. 6.]

# === With keepdims ===
mean_axis0_keep = np.mean(matrix, axis=0, keepdims=True)
print(f"\nWith keepdims (shape {mean_axis0_keep.shape}):")
print(mean_axis0_keep)   # [[4. 5. 6.]]

# === Practical use case: normalize by column mean ===
normalized = matrix - np.mean(matrix, axis=0, keepdims=True)
print(f"\nNormalized (each column mean-subtracted):\n{normalized}")
# Each column has mean 0 now

# === 3D example ===
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"\n=== 3D (shape {arr_3d.shape}) ===")

sum_no_keep = np.sum(arr_3d, axis=1)
print(f"Without keepdims: shape {sum_no_keep.shape}")   # (2, 4)

sum_keep = np.sum(arr_3d, axis=1, keepdims=True)
print(f"With keepdims:    shape {sum_keep.shape}")      # (2, 1, 4)