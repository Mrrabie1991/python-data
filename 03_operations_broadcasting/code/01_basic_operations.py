# 03_operations_broadcasting/code/01_basic_operations.py
# Basic mathematical operations on arrays

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Element-wise operations
print(f"a + b:  {a + b}")      # [11 22 33 44 55]
print(f"a - b:  {a - b}")      # [-9 -18 -27 -36 -45]
print(f"a * b:  {a * b}")      # [10 40 90 160 250]
print(f"b / a:  {b / a}")      # [10. 10. 10. 10. 10.]
print(f"b // a: {b // a}")     # [10 10 10 10 10]
print(f"b % a:  {b % a}")      # [0 0 0 0 0]
print(f"a ** 2: {a ** 2}")     # [1 4 9 16 25]

# Operations with a scalar
print(f"\na + 10: {a + 10}")   # [11 12 13 14 15] — scalar broadcast
print(f"a * 3:  {a * 3}")      # [3 6 9 12 15]

# Comparison (returns boolean array)
print(f"\na > 2:  {a > 2}")    # [False False  True  True  True]
print(f"a == 3: {a == 3}")     # [False False  True False False]