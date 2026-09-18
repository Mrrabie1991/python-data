# 05_random_module/code/02_distributions.py
# Probability distributions

import numpy as np

# === Normal (Gaussian) — most important ===
# mean=25 (temperature), std=2
temps = np.random.normal(25, 2, 1000)
print(f"Normal distribution (mean=25, std=2):")
print(f"  Sample mean: {temps.mean():.2f}")
print(f"  Sample std:  {temps.std():.2f}")
print(f"  Min:         {temps.min():.2f}")
print(f"  Max:         {temps.max():.2f}")

# === Uniform ===
uniform = np.random.uniform(0, 100, 1000)
print(f"\nUniform distribution (0, 100):")
print(f"  Sample mean: {uniform.mean():.2f}")   # ≈ 50
print(f"  Sample std:  {uniform.std():.2f}")    # ≈ 28.87

# === Binomial — coin flips ===
# 10 coin flips, 1000 experiments
flips = np.random.binomial(10, 0.5, 1000)
print(f"\nBinomial (10 flips, p=0.5):")
print(f"  Mean: {flips.mean():.2f}")           # ≈ 5
print(f"  Std:  {flips.std():.2f}")            # ≈ 1.58

# === Poisson — event counts ===
# Average 3 events per minute
events = np.random.poisson(3, 1000)
print(f"\nPoisson (lambda=3):")
print(f"  Mean: {events.mean():.2f}")          # ≈ 3