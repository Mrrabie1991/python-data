# 05_random_module/exercises/exercise_04.py
# Exercise 04: Seed & Reproducibility
#
# Requirements:
# 1. Set seed 42, generate 5 random numbers
# 2. Reset seed 42, generate 5 random numbers. Compare.
# 3. Set seed 100, generate 5 random numbers. Compare with (1).
# 4. Use default_rng with seed 42 and generate 5 random numbers.
# 5. Explain why reproducibility matters in ML in a comment

import numpy as np

# 1. Seed 42 — first run
np.random.seed(42)
run1 = np.random.rand(5)
print(f"Seed 42 (first run):  {run1}")

# 2. Seed 42 — second run (must be identical)
np.random.seed(42)
run2 = np.random.rand(5)
print(f"Seed 42 (second run): {run2}")
print(f"Identical? {np.array_equal(run1, run2)}")   # True

# 3. Different seed — different results
np.random.seed(100)
run3 = np.random.rand(5)
print(f"\nSeed 100: {run3}")
print(f"Same as seed 42? {np.array_equal(run1, run3)}")   # False

# 4. Modern API — default_rng
rng = np.random.default_rng(seed=42)
run4 = rng.random(5)
print(f"\nUsing default_rng(42): {run4}")

rng2 = np.random.default_rng(seed=42)
run5 = rng2.random(5)
print(f"Same again:            {run5}")
print(f"Identical? {np.array_equal(run4, run5)}")   # True

# 5. Why reproducibility matters:
# - Debugging: reproduce exact error conditions
# - Research: others can verify your results
# - Testing: deterministic tests (pytest with fixed seed)
# - Comparison: compare two models fairly (same data split)