# 02_indexing_slicing/exercises/exercise_05.py
# Exercise 05: np.where
#
# Requirements:
# 1. Create np.array([3, 8, 1, 6, 9, 2, 7, 4])
# 2. Replace all values > 5 with 50
# 3. Replace all even numbers with -1
# 4. Find all indices where value < 5
# 5. Label: "high" for values > 5, "low" otherwise

import numpy as np

arr = np.array([3, 8, 1, 6, 9, 2, 7, 4])
print(f"Original: {arr}")

# 2. Replace > 5 with 50
result_50 = np.where(arr > 5, 50, arr)
print(f"\nnp.where(arr > 5, 50, arr): {result_50}")
# [3 50 1 50 50 2 50 4]

# 3. Replace evens with -1
result_even = np.where(arr % 2 == 0, -1, arr)
print(f"np.where(even, -1, arr):   {result_even}")
# [3 -1 1 -1 9 -1 7 -1]

# 4. Find indices < 5
indices = np.where(arr < 5)
print(f"\nIndices where arr < 5: {indices[0]}")
# [0 2 5 7]

# 5. Label high/low
labels = np.where(arr > 5, "high", "low")
print(f"\nLabels: {labels}")
# ['low' 'high' 'low' 'high' 'high' 'low' 'high' 'low']