# 01_numpy_basics/exercises/exercise_05.py
# Exercise 05: View vs Copy
#
# Requirements:
# 1. Create np.arange(10)
# 2. Create a view of elements 3 to 7
# 3. Create a copy of the same elements
# 4. Change view[0] to 99 — what happens to original?
# 5. Change copy[0] to 77 — what happens to original?
# 6. Explain in a comment why behavior differs

import numpy as np

arr = np.arange(10)
print(f"Original: {arr}")

# View — shares data
view = arr[3:7]
print(f"\nView: {view}")

# Copy — separate data
copy = arr[3:7].copy()
print(f"Copy: {copy}")

# Change view[0]
view[0] = 99
print(f"\nAfter view[0] = 99:")
print(f"  arr:  {arr}")   # [0 1 2 99 4 5 6 7 8 9]
print(f"  view: {view}")  # [99 4 5 6]

# Change copy[0]
copy[0] = 77
print(f"\nAfter copy[0] = 77:")
print(f"  arr:  {arr}")   # [0 1 2 99 4 5 6 7 8 9] — unchanged
print(f"  copy: {copy}")  # [77 4 5 6]

# View shares memory with the original array, so changes affect both.
# Copy has its own memory, so changes are independent.