# 03_operations_broadcasting/code/05_broadcasting_rules.py
# Broadcasting rules in action

import numpy as np

# === Same shapes: element-wise ===
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(f"Same shapes: {a + b}")   # [11 22 33]

# === One shape is 1 ===
a = np.array([[1, 2, 3]])       # shape (1, 3)
b = np.array([[10], [20], [30]]) # shape (3, 1)
result = a + b
print(f"\n(1,3) + (3,1):\n{result}")
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]
# a broadcast to (3,3), b broadcast to (3,3)

# === Outer product via broadcasting ===
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
outer = a[:, np.newaxis] * b
print(f"\nOuter product:\n{outer}")
# [[ 10  20  30]
#  [ 20  40  60]
#  [ 30  60  90]]

# === Incompatible shapes ===
try:
    x = np.array([1, 2, 3, 4])   # shape (4,)
    y = np.array([1, 2, 3])      # shape (3,)
    print(x + y)
except ValueError as e:
    print(f"\nError: {e}")
    # operands could not be broadcast together with shapes (4,) (3,)