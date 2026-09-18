# 04_reshaping_manipulation/code/01_reshape.py
# reshape — changing array shape

import numpy as np

# === From 1D to 2D ===
arr = np.arange(12)
print(f"Original: {arr}")
print(f"Shape:    {arr.shape}")

# Reshape to 3x4
matrix = arr.reshape(3, 4)
print(f"\nReshaped (3, 4):\n{matrix}")
print(f"Shape: {matrix.shape}")

# Reshape to 4x3
matrix2 = arr.reshape(4, 3)
print(f"\nReshaped (4, 3):\n{matrix2}")

# === Using -1 for auto-calculate ===
auto = arr.reshape(2, -1)
print(f"\nReshape (2, -1):\n{auto}")
print(f"Shape: {auto.shape}")   # (2, 6)

# === 3D reshape ===
arr_3d = arr.reshape(2, 3, 2)
print(f"\nReshape (2, 3, 2):\n{arr_3d}")
print(f"Shape: {arr_3d.shape}")

# === Flatten back to 1D ===
back = arr_3d.reshape(-1)
print(f"\nBack to 1D: {back}")

# === reshape returns a view ===
view = arr.reshape(3, 4)
view[0, 0] = 99
print(f"\nAfter view[0, 0] = 99:")
print(f"arr: {arr}")   # first element changed