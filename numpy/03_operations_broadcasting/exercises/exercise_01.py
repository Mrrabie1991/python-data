# 03_operations_broadcasting/exercises/exercise_01.py
# Exercise 01: Basic Mathematical Operations
#
# Requirements:
# 1. Create a = np.array([1, 2, 3, 4, 5]) and b = np.array([5, 4, 3, 2, 1])
# 2. Compute a + b, a - b, a * b, a / b
# 3. Compute a ** 2, np.sqrt(a), np.exp(a), np.log(a)
# 4. Compute a % 2 and a // 2
# 5. Compute boolean result of a > b

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print(f"a: {a}")
print(f"b: {b}")

# 2. Basic operations
print(f"\na + b: {a + b}")   # [6 6 6 6 6]
print(f"a - b: {a - b}")     # [-4 -2  0  2  4]
print(f"a * b: {a * b}")     # [5 8 9 8 5]
print(f"a / b: {a / b}")     # [0.2 0.5 1.  2.  5. ]

# 3. Ufuncs
print(f"\na ** 2:    {a ** 2}")          # [1 4 9 16 25]
print(f"np.sqrt(a): {np.sqrt(a)}")        # [1. 1.414 1.732 2. 2.236]
print(f"np.exp(a):  {np.exp(a)}")         # [e^1, e^2, ...]
print(f"np.log(a):  {np.log(a)}")         # [0. 0.693 1.099 1.386 1.609]

# 4. Modulo and integer division
print(f"\na % 2:  {a % 2}")               # [1 0 1 0 1]
print(f"a // 2: {a // 2}")                # [0 1 1 2 2]

# 5. Comparison
print(f"\na > b: {a > b}")                # [False False False True True]