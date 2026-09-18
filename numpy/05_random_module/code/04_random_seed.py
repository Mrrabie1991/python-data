# 05_random_module/code/04_random_seed.py
# Random seed for reproducibility

import numpy as np

# === Without seed — different every run ===
print("Without seed:")
print(np.random.rand(3))
print(np.random.rand(3))

# === With seed — same every time ===
print("\nWith seed=42:")
np.random.seed(42)
print(np.random.rand(3))

np.random.seed(42)
print(np.random.rand(3))   # Same as above

# === Different seed — different values ===
print("\nWith seed=100:")
np.random.seed(100)
print(np.random.rand(3))

# === Reset seed and reproduce exactly ===
print("\nReproducing exact sequence:")
np.random.seed(42)
print(np.random.rand(3))
print(np.random.rand(3))

np.random.seed(42)
print(np.random.rand(3))   # First one from previous
print(np.random.rand(3))   # Second one from previous

# === Best practice: use the new Generator API ===
rng = np.random.default_rng(seed=42)
print("\nUsing Generator:")
print(rng.random(3))
print(rng.random(3))

# === Why reproducibility matters ===
# 1. Debugging — reproduce exact error
# 2. Research — others can verify your results
# 3. Testing — tests should be deterministic