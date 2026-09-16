# 01_numpy_basics/exercises/exercise_01.py
# Exercise 01: Create various arrays
#
# Requirements:
# 1. Create an array of numbers 1 to 10 using np.array
# 2. Create an array of 8 zeros
# 3. Create an array of 6 elements filled with 5
# 4. Create an array from 50 to 100 with step 10
# 5. Create an array of 10 evenly spaced numbers between -1 and 1

import numpy as np

# 1. Array from 1 to 10
arr_1_to_10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"1 to 10:     {arr_1_to_10}")

# 2. Array of 8 zeros
arr_zeros = np.zeros(8)
print(f"8 zeros:     {arr_zeros}")

# 3. Array of 6 elements filled with 5
arr_full = np.full(6, 5)
print(f"6 fives:     {arr_full}")

# 4. Array from 50 to 100 with step 10
arr_range = np.arange(50, 100, 10)
print(f"50 to 100:   {arr_range}")

# 5. Array of 10 evenly spaced numbers between -1 and 1
arr_linspace = np.linspace(-1, 1, 10)
print(f"-1 to 1:     {arr_linspace}")