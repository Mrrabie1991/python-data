# 05_random_module/exercises/exercise_01.py
# Exercise 01: Random Basics
#
# Requirements:
# 1. Generate 1000 samples from np.random.rand(1000). Compute mean and std.
# 2. Generate 1000 samples from np.random.randn(1000). Compare with (1).
# 3. Generate 100 random integers between 1 and 6 (dice rolls). Count frequencies.
# 4. Generate 1000 uniform values between 50 and 100.

import numpy as np

np.random.seed(42)

# 1. Uniform [0, 1)
uniform_01 = np.random.rand(1000)
print(f"Uniform [0, 1):")
print(f"  Mean: {uniform_01.mean():.4f}")   # ≈ 0.5
print(f"  Std:  {uniform_01.std():.4f}")    # ≈ 0.289
print(f"  Min:  {uniform_01.min():.4f}")   # near 0
print(f"  Max:  {uniform_01.max():.4f}")   # near 1

# 2. Standard normal
normal_std = np.random.randn(1000)
print(f"\nStandard normal (randn):")
print(f"  Mean: {normal_std.mean():.4f}")   # ≈ 0
print(f"  Std:  {normal_std.std():.4f}")    # ≈ 1
print(f"  Min:  {normal_std.min():.4f}")   # can be < -3
print(f"  Max:  {normal_std.max():.4f}")   # can be > 3

# 3. Dice rolls — count frequencies
dice = np.random.randint(1, 7, 100)
print(f"\nDice rolls (100 throws):")
for face in range(1, 7):
    count = np.sum(dice == face)
    print(f"  Face {face}: {count} times")

# 4. Uniform in custom range
custom_uniform = np.random.uniform(50, 100, 1000)
print(f"\nUniform [50, 100):")
print(f"  Mean: {custom_uniform.mean():.4f}")   # ≈ 75
print(f"  Min:  {custom_uniform.min():.4f}")   # ≥ 50
print(f"  Max:  {custom_uniform.max():.4f}")   # < 100