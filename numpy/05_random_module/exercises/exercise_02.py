# 05_random_module/exercises/exercise_02.py
# Exercise 02: Distributions
#
# Requirements:
# 1. Simulate 1000 temperature readings with normal(mean=25, std=3)
# 2. Print sample mean, std, min, max
# 3. Count how many readings are above 28
# 4. Simulate 1000 coin flips (10 flips each) with binomial(10, 0.5)
# 5. Simulate 1000 Poisson events with poisson(5)

import numpy as np

np.random.seed(42)

# 1. Temperature readings — Normal distribution
temps = np.random.normal(25, 3, 1000)
print("Temperature simulation (normal, mean=25, std=3):")
print(f"  Sample mean: {temps.mean():.2f}")
print(f"  Sample std:  {temps.std():.2f}")
print(f"  Min:         {temps.min():.2f}")
print(f"  Max:         {temps.max():.2f}")

# 2. Count readings above 28
above_28 = np.sum(temps > 28)
print(f"\nReadings above 28: {above_28} ({100 * above_28 / len(temps):.1f}%)")
# Expected ~16% (one std above mean)

# 3. Coin flips — Binomial
flips = np.random.binomial(n=10, p=0.5, size=1000)
print(f"\nCoin flips (10 flips per experiment, 1000 experiments):")
print(f"  Mean: {flips.mean():.2f}")   # ≈ 5
print(f"  Std:  {flips.std():.2f}")    # ≈ 1.58
print(f"  Min:  {flips.min()}")
print(f"  Max:  {flips.max()}")

# Distribution of results
print(f"\n  Frequency of each count:")
for k in range(11):
    count = np.sum(flips == k)
    print(f"    {k} heads: {count} times")

# 4. Poisson events
events = np.random.poisson(lam=5, size=1000)
print(f"\nPoisson events (lambda=5):")
print(f"  Mean: {events.mean():.2f}")   # ≈ 5
print(f"  Std:  {events.std():.2f}")    # ≈ √5 ≈ 2.24
print(f"  Min:  {events.min()}")
print(f"  Max:  {events.max()}")