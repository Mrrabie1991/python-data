# 02_indexing_slicing/exercises/exercise_01.py
# Exercise 01: Basic Indexing and Slicing
#
# Requirements:
# 1. Create np.arange(20)
# 2. Access elements at index 5, -1, and -5
# 3. Slice elements from index 5 to 15
# 4. Slice every 3rd element
# 5. Reverse the array

import numpy as np

arr = np.arange(20)
print(f"Original: {arr}")

# 2. Indexing
print(f"\narr[5]:  {arr[5]}")     # 5
print(f"arr[-1]: {arr[-1]}")     # 19
print(f"arr[-5]: {arr[-5]}")     # 15

# 3. Slice from index 5 to 15
print(f"\narr[5:15]: {arr[5:15]}")
# [5 6 7 8 9 10 11 12 13 14]

# 4. Every 3rd element
print(f"arr[::3]:  {arr[::3]}")
# [0 3 6 9 12 15 18]

# 5. Reverse
print(f"arr[::-1]: {arr[::-1]}")
# [19 18 17 ... 1 0]