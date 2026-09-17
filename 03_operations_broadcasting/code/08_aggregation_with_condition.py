# 03_operations_broadcasting/code/08_aggregation_with_condition.py
# Aggregation with conditions

import numpy as np

arr = np.array([1, 5, 8, 3, 10, 2, 7, 4])
print(f"Array: {arr}")

# === Aggregation on filtered data ===
print(f"\nSum > 5:     {np.sum(arr[arr > 5])}")        # 25
print(f"Mean > 5:    {np.mean(arr[arr > 5]):.2f}")     # 8.33
print(f"Max even:    {np.max(arr[arr % 2 == 0])}")     # 10
print(f"Min odd:     {np.min(arr[arr % 2 == 1])}")     # 1

# === Count with condition ===
print(f"\nCount > 5:   {np.count_nonzero(arr > 5)}")    # 3
print(f"Count even:  {np.count_nonzero(arr % 2 == 0)}") # 4

# Alternative: sum on boolean array
print(f"Count > 5 (via sum): {np.sum(arr > 5)}")        # 3

# === Multiple conditions ===
between = arr[(arr > 3) & (arr < 8)]
print(f"\nBetween 3 and 8: {between}")                  # [5 7 4]
print(f"Sum:             {np.sum(between)}")            # 16

# === Percentile on filtered data ===
above_5 = arr[arr > 5]
print(f"\nValues > 5:           {above_5}")
print(f"Median of them:       {np.median(above_5)}")
print(f"75th percentile:      {np.percentile(above_5, 75)}")

# === 2D aggregation with condition ===
matrix = np.array([
    [1, 8, 3],
    [5, 2, 9],
    [4, 7, 6]
])
print(f"\n=== 2D ===\n{matrix}")
print(f"\nSum elements > 5:    {np.sum(matrix[matrix > 5])}")
print(f"Count elements > 5:  {np.count_nonzero(matrix > 5)}")
print(f"Mean elements > 5:   {np.mean(matrix[matrix > 5]):.2f}")