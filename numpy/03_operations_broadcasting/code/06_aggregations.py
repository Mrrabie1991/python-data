# 03_operations_broadcasting/code/06_aggregations.py
# Aggregation functions and axis parameter

import numpy as np

arr = np.array([3, 8, 1, 6, 9, 2, 7, 4])
print(f"Array: {arr}")

# === Basic aggregations ===
print(f"\nsum:     {np.sum(arr)}")     # 40
print(f"mean:    {np.mean(arr)}")      # 5.0
print(f"std:     {np.std(arr):.4f}")   # standard deviation
print(f"var:     {np.var(arr):.4f}")   # variance
print(f"min:     {np.min(arr)}")       # 1
print(f"max:     {np.max(arr)}")       # 9
print(f"argmin:  {np.argmin(arr)}")    # 2 (index of 1)
print(f"argmax:  {np.argmax(arr)}")    # 4 (index of 9)
print(f"median:  {np.median(arr)}")    # 5.0

# === 2D aggregations ===
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\nMatrix:\n{matrix}")

print(f"\nTotal sum:       {np.sum(matrix)}")           # 45
print(f"Sum axis=0:      {np.sum(matrix, axis=0)}")    # [12 15 18] — per column
print(f"Sum axis=1:      {np.sum(matrix, axis=1)}")    # [6 15 24] — per row
print(f"\nMean axis=0:     {np.mean(matrix, axis=0)}") # [4. 5. 6.]
print(f"Mean axis=1:     {np.mean(matrix, axis=1)}")   # [2. 5. 8.]
print(f"\nMax axis=0:      {np.max(matrix, axis=0)}")  # [7 8 9]
print(f"Max axis=1:      {np.max(matrix, axis=1)}")    # [3 6 9]