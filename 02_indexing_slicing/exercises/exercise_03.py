# 02_indexing_slicing/exercises/exercise_03.py
# Exercise 03: Boolean Masking
#
# Requirements:
# 1. Create np.array([15, 8, 23, 4, 42, 16, 7, 30, 11, 25])
# 2. Filter elements greater than 15
# 3. Filter elements between 10 and 25
# 4. Count how many elements are even
# 5. Replace all elements less than 10 with 0

import numpy as np

arr = np.array([15, 8, 23, 4, 42, 16, 7, 30, 11, 25])
print(f"Original: {arr}")

# 2. Filter > 15
greater_15 = arr[arr > 15]
print(f"\nGreater than 15: {greater_15}")
# [23 42 16 30 25]

# 3. Between 10 and 25
between = arr[(arr >= 10) & (arr <= 25)]
print(f"Between 10-25:   {between}")
# [15 23 16 11 25]

# 4. Count evens
even_count = np.sum(arr % 2 == 0)
print(f"\nEven count: {even_count}")   # 5 (8, 4, 42, 16, 30)

# 5. Replace < 10 with 0
arr_modified = arr.copy()          # Copy so we don't modify original
arr_modified[arr_modified < 10] = 0
print(f"\nAfter replacing < 10 with 0: {arr_modified}")
# [15 0 23 0 42 16 0 30 11 25]