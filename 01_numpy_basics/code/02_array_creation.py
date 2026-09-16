# 01_numpy_basics/code/02_array_creation.py
# Array creation functions

import numpy as np

# From list
arr = np.array([1, 2, 3, 4, 5])
print(f"From list: {arr}")

# Zeros, ones, full
zeros = np.zeros(5)
ones = np.ones(5)
full = np.full(5, 7)
print(f"\nZeros: {zeros}")     # [0. 0. 0. 0. 0.]
print(f"Ones:  {ones}")        # [1. 1. 1. 1. 1.]
print(f"Full:  {full}")        # [7 7 7 7 7]

# Identity matrix
identity = np.eye(3)
print(f"\nIdentity:\n{identity}")

# Arange — like range but returns array
range_arr = np.arange(0, 10, 2)
print(f"\nArange(0, 10, 2): {range_arr}")   # [0 2 4 6 8]

# Linspace — evenly spaced
linspace = np.linspace(0, 1, 5)
print(f"Linspace(0, 1, 5): {linspace}")     # [0. 0.25 0.5 0.75 1.]

# Random
np.random.seed(42)  # For reproducibility
random_uniform = np.random.rand(3)
random_int = np.random.randint(0, 10, 5)
print(f"\nRandom uniform (3): {random_uniform}")
print(f"Random int (0-10, 5): {random_int}")