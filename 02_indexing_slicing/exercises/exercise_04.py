# 02_indexing_slicing/exercises/exercise_04.py
# Exercise 04: Fancy Indexing
#
# Requirements:
# 1. Create np.array([100, 200, 300, 400, 500])
# 2. Select elements at indices [0, 2, 4]
# 3. Reorder as [4, 3, 2, 1, 0]
# 4. Duplicate the first element 3 times
# 5. Show that fancy indexing returns a copy

import numpy as np

arr = np.array([100, 200, 300, 400, 500])
print(f"Original: {arr}")

# 2. Select specific indices
print(f"\narr[[0, 2, 4]]: {arr[[0, 2, 4]]}")
# [100 300 500]

# 3. Reorder (reverse)
print(f"arr[[4, 3, 2, 1, 0]]: {arr[[4, 3, 2, 1, 0]]}")
# [500 400 300 200 100]

# 4. Duplicate first element 3 times
print(f"arr[[0, 0, 0]]: {arr[[0, 0, 0]]}")
# [100 100 100]

# 5. Copy behavior
selected = arr[[0, 2, 4]]
selected[0] = 999
print(f"\nAfter selected[0] = 999:")
print(f"  Original: {arr}")        # [100 200 300 400 500] — unchanged
print(f"  Selected: {selected}")   # [999 300 500]