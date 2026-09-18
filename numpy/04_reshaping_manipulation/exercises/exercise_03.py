# 04_reshaping_manipulation/exercises/exercise_03.py
# Exercise 03: Concatenate and Stack
#
# Requirements:
# 1. Create two 2D arrays a and b of shape (2, 3)
# 2. Concatenate along axis=0 and axis=1
# 3. Use vstack and hstack and compare
# 4. Use stack with axis=0 and axis=2
# 5. Print all shapes

import numpy as np

# 1. Create two 2D arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(f"a (shape {a.shape}):\n{a}")
print(f"\nb (shape {b.shape}):\n{b}")

# 2. Concatenate along axis=0 (stack vertically)
concat_0 = np.concatenate([a, b], axis=0)
print(f"\nconcatenate axis=0 (shape {concat_0.shape}):")
print(concat_0)

# Concatenate along axis=1 (stack horizontally)
concat_1 = np.concatenate([a, b], axis=1)
print(f"\nconcatenate axis=1 (shape {concat_1.shape}):")
print(concat_1)

# 3. vstack and hstack (shortcuts)
v = np.vstack([a, b])
h = np.hstack([a, b])
print(f"\nvstack (shape {v.shape}):\n{v}")
print(f"\nhstack (shape {h.shape}):\n{h}")

# 4. stack — adds a NEW dimension
stacked_0 = np.stack([a, b], axis=0)
stacked_2 = np.stack([a, b], axis=2)
print(f"\nstack axis=0 (shape {stacked_0.shape})")
print(f"stack axis=2 (shape {stacked_2.shape})")

# stack creates a NEW axis, concatenate uses an EXISTING one