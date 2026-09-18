# 01_numpy_basics/exercises/exercise_02.py
# Exercise 02: Memory analysis
#
# Requirements:
# 1. Create three arrays of np.zeros(100) with dtypes int8, int32, float64
# 2. Print itemsize and nbytes for each
# 3. Explain in a comment why int8 uses the least memory

import numpy as np

arr_int8 = np.zeros(100, dtype=np.int8)
arr_int32 = np.zeros(100, dtype=np.int32)
arr_float64 = np.zeros(100, dtype=np.float64)

print("=== int8 ===")
print(f"itemsize: {arr_int8.itemsize} bytes")   # 1
print(f"nbytes:   {arr_int8.nbytes} bytes")     # 100

print("\n=== int32 ===")
print(f"itemsize: {arr_int32.itemsize} bytes")  # 4
print(f"nbytes:   {arr_int32.nbytes} bytes")    # 400

print("\n=== float64 ===")
print(f"itemsize: {arr_float64.itemsize} bytes")  # 8
print(f"nbytes:   {arr_float64.nbytes} bytes")    # 800

# int8 uses 1 byte per element, while int32 uses 4 and float64 uses 8.
# With 100 elements, int8 needs only 100 bytes, while float64 needs 800.