# 05_random_module/code/03_shuffle_choice.py
# Shuffle and choice

import numpy as np

# === shuffle — in-place ===
data = np.arange(10)
print(f"Original: {data}")

np.random.shuffle(data)
print(f"After shuffle: {data}")

# === permutation — returns copy ===
data = np.arange(10)
perm = np.random.permutation(data)
print(f"\nOriginal: {data}")
print(f"Permuted: {perm}")

# === choice — random sampling ===
# Sample 3 elements without replacement
data = np.arange(100)
sample = np.random.choice(data, size=5, replace=False)
print(f"\nSample without replacement: {sample}")

# With replacement
sample_wr = np.random.choice(data, size=5, replace=True)
print(f"Sample with replacement:    {sample_wr}")

# With probabilities
colors = np.array(["red", "green", "blue"])
probs = [0.5, 0.3, 0.2]
choices = np.random.choice(colors, size=10, p=probs)
print(f"\nWeighted choice: {choices}")

# === Train/Test split application ===
data = np.arange(100)
np.random.shuffle(data)

train = data[:80]
test = data[80:]

print(f"\nTrain size: {len(train)}")
print(f"Test size:  {len(test)}")
print(f"Train: {train[:10]}...")
print(f"Test:  {test}")