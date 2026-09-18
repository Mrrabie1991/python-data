# 03_operations_broadcasting/exercises/exercise_04.py
# Exercise 04: Advanced Broadcasting
#
# Requirements:
# 1. Create a = np.array([1, 2, 3]) and b = np.array([10, 20, 30])
# 2. Compute outer product using a[:, np.newaxis] * b
# 3. Compute addition table using a[:, np.newaxis] + b
# 4. Explain shape of result in a comment
# 5. Compute multiplication table 1-9 using broadcasting

import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# 2. Outer product
outer = a[:, np.newaxis] * b
print(f"Outer product:\n{outer}")
# a[:, np.newaxis] shape: (3, 1)
# b shape: (3,)
# Broadcast to (3, 3)

# 3. Addition table
addition = a[:, np.newaxis] + b
print(f"\nAddition table:\n{addition}")

# 5. Multiplication table 1-9
table = np.arange(1, 10)[:, np.newaxis] * np.arange(1, 10)
print(f"\nMultiplication table 1-9:\n{table}")