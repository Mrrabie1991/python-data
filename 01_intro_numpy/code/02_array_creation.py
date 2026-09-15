# 01_intro_numpy/code/02_array_creation.py
# Array creation functions

import numpy as np

# %% Zeros, ones, full
zeros = np.zeros(5)
ones = np.ones(5)
full = np.full(5, 7)

print(f"Zeros: {zeros}")
print(f"Ones: {ones}")
print(f"Full: {full}")

# %% Identity matrix
identity = np.eye(3)
print(f"\nIdentity:\n{identity}")

# %% Range and linspace
range_arr = np.arange(0, 10, 2)      # start, stop, step
linspace = np.linspace(0, 1, 5)      # start, stop, count

print(f"\nArange: {range_arr}")
print(f"Linspace: {linspace}")

# %% Random
random_uniform = np.random.rand(3, 3)         # uniform [0, 1)
random_int = np.random.randint(0, 10, (3, 3))  # random integers

print(f"\nRandom uniform:\n{random_uniform}")
print(f"Random integers:\n{random_int}")
# %%
