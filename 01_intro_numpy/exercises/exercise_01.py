# 01_intro_numpy/exercises/exercise_01.py
# Exercise 01: Create various arrays

import numpy as np

# Array of numbers 1 to 10
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Array of 10 zeros
zero_arr = np.zeros(10)

# Array of 5 elements filled with 3
arr_of_three = np.full(5, 3)

# Array from 0 to 100 with step 10
arr_0_to_100 = np.arange(0, 100, 10)

# Array of 5 evenly spaced numbers between 1 and 2
arr_linspace = np.linspace(1, 2, 5)

print(arr)
print(zero_arr)
print(arr_of_three)
print(arr_0_to_100)
print(arr_linspace)