# 04_reshaping_manipulation/exercises/exercise_04.py
# Exercise 04: Split
#
# Requirements:
# 1. Create np.arange(20)
# 2. Split into 4 equal parts using np.split
# 3. Split at indices [5, 10, 15]
# 4. Create a 4x4 matrix and use vsplit and hsplit to divide in half
# 5. Print all parts

import numpy as np

# 1. Create 1D array
arr = np.arange(20)
print(f"Array: {arr}")

# 2. Split into 4 equal parts
parts = np.split(arr, 4)
print(f"\nSplit into 4 equal parts:")
for i, p in enumerate(parts):
    print(f"  Part {i}: {p}")

# 3. Split at specific indices
parts = np.split(arr, [5, 10, 15])
print(f"\nSplit at [5, 10, 15]:")
for i, p in enumerate(parts):
    print(f"  Part {i}: {p}")

# 4. Create 4x4 matrix
matrix = np.arange(16).reshape(4, 4)
print(f"\nMatrix:\n{matrix}")

# vsplit — divide by rows
vparts = np.vsplit(matrix, 2)
print(f"\nvsplit into 2:")
for i, p in enumerate(vparts):
    print(f"  Part {i}:\n{p}")

# hsplit — divide by columns
hparts = np.hsplit(matrix, 2)
print(f"\nhsplit into 2:")
for i, p in enumerate(hparts):
    print(f"  Part {i}:\n{p}")