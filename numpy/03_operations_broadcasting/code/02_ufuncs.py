# 03_operations_broadcasting/code/02_ufuncs.py
# Universal functions (ufuncs)

import numpy as np

arr = np.array([1, 4, 9, 16, 25])

# Square root
print(f"sqrt:    {np.sqrt(arr)}")     # [1. 2. 3. 4. 5.]

# Exponential and log
print(f"exp:     {np.exp([0, 1, 2])}")          # [1. 2.71828183 7.3890561]
print(f"log:     {np.log([1, np.e, np.e**2])}") # [0. 1. 2.]

# Trigonometric
angles = np.array([0, np.pi/2, np.pi])
print(f"sin:     {np.sin(angles)}")    # [0. 1. 0.]
print(f"cos:     {np.cos(angles)}")    # [1. 0. -1.]

# Rounding
floats = np.array([1.4, 2.6, -1.5, -2.5])
print(f"\nround:   {np.round(floats)}")   # [1. 3. -2. -2.]
print(f"floor:   {np.floor(floats)}")     # [1. 2. -2. -3.]
print(f"ceil:    {np.ceil(floats)}")      # [2. 3. -1. -2.]
print(f"abs:     {np.abs(floats)}")       # [1.4 2.6 1.5 2.5]

# ufuncs on 2D arrays
matrix = np.array([[1, 4], [9, 16]])
print(f"\nsqrt of 2D:\n{np.sqrt(matrix)}")

# ufuncs are element-wise
print(f"\nAdding two ufuncs: {np.sqrt(arr) + np.log(arr)}")