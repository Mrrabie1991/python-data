# 04_reshaping_manipulation/code/04_concatenate.py
# Concatenate, vstack, hstack, stack

import numpy as np

# === 1D concatenate ===
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"a: {a}")
print(f"b: {b}")

# Concatenate (default axis=0)
c = np.concatenate([a, b])
print(f"\nconcatenate: {c}")   # [1 2 3 4 5 6]

# === 2D concatenate ===
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(f"\nm1:\n{m1}")
print(f"m2:\n{m2}")

# Vertical (default axis=0 for 2D)
v = np.concatenate([m1, m2])
print(f"\nconcatenate axis=0:\n{v}")

# Horizontal (axis=1)
h = np.concatenate([m1, m2], axis=1)
print(f"\nconcatenate axis=1:\n{h}")

# === vstack and hstack ===
print(f"\nvstack:\n{np.vstack([m1, m2])}")
print(f"\nhstack:\n{np.hstack([m1, m2])}")

# === stack — adds new dimension ===
print(f"\nstack (new axis=0):\n{np.stack([m1, m2])}")
print(f"Shape: {np.stack([m1, m2]).shape}")   # (2, 2, 2)

print(f"\nstack (new axis=2):\n{np.stack([m1, m2], axis=2)}")
print(f"Shape: {np.stack([m1, m2], axis=2).shape}")   # (2, 2, 2)