# 01_numpy_basics/code/03_array_attributes.py
# Array attributes

import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("=== 1D ===")
print(f"shape:    {arr_1d.shape}")      # (5,)
print(f"ndim:     {arr_1d.ndim}")       # 1
print(f"size:     {arr_1d.size}")       # 5
print(f"dtype:    {arr_1d.dtype}")      # int64
print(f"itemsize: {arr_1d.itemsize}")   # 8
print(f"nbytes:   {arr_1d.nbytes}")     # 40

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n=== 2D ===")
print(f"shape:    {arr_2d.shape}")      # (2, 3)
print(f"ndim:     {arr_2d.ndim}")       # 2
print(f"size:     {arr_2d.size}")       # 6
print(f"nbytes:   {arr_2d.nbytes}")     # 48

# 3D array
arr_3d = np.zeros((2, 3, 4))
print("\n=== 3D ===")
print(f"shape:    {arr_3d.shape}")      # (2, 3, 4)
print(f"ndim:     {arr_3d.ndim}")       # 3
print(f"size:     {arr_3d.size}")       # 24