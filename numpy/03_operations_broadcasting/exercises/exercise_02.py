# 03_operations_broadcasting/exercises/exercise_02.py
# Exercise 02: Universal Functions (ufuncs)
#
# Requirements:
# 1. Create angles = np.linspace(0, np.pi, 5)
# 2. Compute np.sin(angles) and np.cos(angles)
# 3. Create an array of random values between -10 and 10
# 4. Compute np.abs(), np.floor(), np.ceil(), np.round() on them
# 5. Compute np.sqrt(np.abs(arr)) — combine ufuncs

import numpy as np

# 1. Angles
angles = np.linspace(0, np.pi, 5)
print(f"angles: {angles}")

# 2. Trig
print(f"\nsin: {np.sin(angles)}")   # [0. 0.707 1. 0.707 0.]
print(f"cos: {np.cos(angles)}")     # [1. 0.707 0. -0.707 -1.]

# 3. Random values
np.random.seed(42)
random_arr = np.random.uniform(-10, 10, 8)
print(f"\nrandom: {random_arr}")

# 4. Rounding and abs
print(f"\nabs:   {np.abs(random_arr)}")
print(f"floor: {np.floor(random_arr)}")
print(f"ceil:  {np.ceil(random_arr)}")
print(f"round: {np.round(random_arr)}")

# 5. Combine ufuncs
combined = np.sqrt(np.abs(random_arr))
print(f"\nsqrt(abs): {combined}")