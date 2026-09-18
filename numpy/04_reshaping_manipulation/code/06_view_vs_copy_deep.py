# 04_reshaping_manipulation/code/06_view_vs_copy_deep.py
# Views vs Copies — deep dive

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Original: {arr}")
print(f"arr.base is None: {arr.base is None}")   # True — owns data

# === View examples ===
print("\n=== Views ===")

view_slice = arr[1:4]
print(f"slice base is not None: {view_slice.base is not None}")   # True

view_reshape = arr.reshape(5, 1)
print(f"reshape base is not None: {view_reshape.base is not None}")  # True

# === Copy examples ===
print("\n=== Copies ===")

copy_flatten = arr.reshape(5, 1).flatten()
print(f"flatten base is None: {copy_flatten.base is None}")   # True

copy_astype = arr.astype(np.float64)
print(f"astype base is None: {copy_astype.base is None}")   # True

copy_math = arr + 1
print(f"math op base is None: {copy_math.base is None}")   # True

# === Practical tip: avoid accidental modifications ===
arr = np.array([1, 2, 3, 4, 5])

# BAD: view will modify original
view = arr[1:4]
view[0] = 99
print(f"\nAfter modifying view: {arr}")   # [1 99 3 4 5]

# GOOD: copy protects original
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()
copy[0] = 99
print(f"After modifying copy: {arr}")     # [1 2 3 4 5]