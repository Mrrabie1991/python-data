# 04_reshaping_manipulation/code/03_transpose.py
# transpose and .T

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"Matrix (shape {matrix.shape}):\n{matrix}")

# === .T ===
transposed = matrix.T
print(f"\nTransposed (shape {transposed.shape}):\n{transposed}")
# [[1 4]
#  [2 5]
#  [3 6]]

# === transpose is a view ===
transposed[0, 0] = 99
print(f"\nmatrix after change:\n{matrix}")
# matrix[0, 0] changed

# === 3D transpose ===
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"\n3D shape: {arr_3d.shape}")   # (2, 3, 4)

# Custom axis order
transposed_3d = arr_3d.transpose(2, 0, 1)
print(f"After transpose(2, 0, 1): shape {transposed_3d.shape}")   # (4, 2, 3)

# Default transpose reverses axes
default_3d = arr_3d.T
print(f"After .T: shape {default_3d.shape}")   # (4, 3, 2)

# === Application: sensor data ===
data = np.array([
    [1, 2, 3, 4],   # sensor 1: 4 time steps
    [5, 6, 7, 8],   # sensor 2
    [9, 10, 11, 12]  # sensor 3
])
print(f"\nSensor data (sensors x time):\n{data}")
print(f"\nTransposed (time x sensors):\n{data.T}")