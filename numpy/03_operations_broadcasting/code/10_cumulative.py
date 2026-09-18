# 03_operations_broadcasting/code/10_cumulative.py
# Cumulative operations

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")

# === Cumulative sum ===
cumsum = np.cumsum(arr)
print(f"\ncumsum:  {cumsum}")   # [1 3 6 10 15]
# Each element is the sum of all previous + itself

# === Cumulative product ===
cumprod = np.cumprod(arr)
print(f"cumprod: {cumprod}")    # [1 2 6 24 120]

# === With axis ===
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"\nMatrix:\n{matrix}")

print(f"\ncumsum axis=0 (per column):\n{np.cumsum(matrix, axis=0)}")
# [[1 2 3]
#  [5 7 9]]

print(f"\ncumsum axis=1 (per row):\n{np.cumsum(matrix, axis=1)}")
# [[1 3 6]
#  [4 9 15]]

# === Application: running total ===
daily_sales = np.array([100, 150, 200, 180, 220, 250, 300])
total = np.cumsum(daily_sales)
print(f"\nDaily sales:    {daily_sales}")
print(f"Running total:  {total}")