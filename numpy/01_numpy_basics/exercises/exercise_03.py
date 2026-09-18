# 01_numpy_basics/exercises/exercise_03.py
# Exercise 03: Type conversion and overflow
#
# Requirements:
# 1. Create an array of [200, 250, 300, 350] with default dtype
# 2. Convert it to int8
# 3. Print values before and after
# 4. Explain in a comment why values changed

import numpy as np

arr = np.array([200, 250, 300, 350])
print(f"Original dtype: {arr.dtype}")
print(f"Original:       {arr}")

arr_int8 = arr.astype(np.int8)
print(f"\nConverted dtype: {arr_int8.dtype}")
print(f"Converted:       {arr_int8}")

# int8 can only hold values from -128 to 127.
# Values above 127 wrap around (overflow).
# 200 -> -56, 250 -> -6, 300 -> 44, 350 -> 94