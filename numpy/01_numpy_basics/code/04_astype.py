# 01_numpy_basics/code/04_astype.py
# Changing array dtype

import numpy as np

# Convert int to float
arr = np.array([1, 2, 3, 4, 5])
arr_float = arr.astype(np.float64)
print(f"Original dtype: {arr.dtype}")       # int64
print(f"After astype:   {arr_float.dtype}") # float64

# Convert to smaller int — overflow risk
arr_big = np.array([300, 400, 500])
arr_int8 = arr_big.astype(np.int8)
print(f"\nOriginal: {arr_big}")             # [300 400 500]
print(f"As int8:  {arr_int8}")              # wrong values — overflow!

# Float to int — truncation
floats = np.array([1.7, 2.3, 3.9])
ints = floats.astype(np.int32)
print(f"\nFloats: {floats}")   # [1.7 2.3 3.9]
print(f"As int: {ints}")       # [1 2 3] — truncated, not rounded

# Check memory difference
arr_float32 = np.zeros(1000, dtype=np.float32)
arr_float64 = np.zeros(1000, dtype=np.float64)
print(f"\nfloat32 nbytes: {arr_float32.nbytes}")  # 4000
print(f"float64 nbytes: {arr_float64.nbytes}")    # 8000