# 05_random_module/exercises/exercise_03.py
# Exercise 03: Shuffle & Choice
#
# Requirements:
# 1. Create np.arange(50) and shuffle it
# 2. Use permutation and compare with shuffle
# 3. Sample 10 elements without replacement from arange(100)
# 4. Sample 10 elements with replacement
# 5. Use weighted choice with p=[0.7, 0.2, 0.1] for ["A", "B", "C"]

import numpy as np

np.random.seed(42)

# 1. Shuffle — in-place
data = np.arange(50)
print(f"Original (first 10): {data[:10]}")
np.random.shuffle(data)
print(f"After shuffle (first 10): {data[:10]}")

# 2. Permutation — returns copy
original = np.arange(50)
permuted = np.random.permutation(original)
print(f"\nOriginal unchanged: {original[:10]}")
print(f"Permuted (copy):    {permuted[:10]}")

# 3. Sample without replacement
sample_no_rep = np.random.choice(np.arange(100), size=10, replace=False)
print(f"\nSample without replacement: {sample_no_rep}")
print(f"All unique: {len(set(sample_no_rep)) == 10}")

# 4. Sample with replacement
sample_wr = np.random.choice(np.arange(10), size=20, replace=True)
print(f"\nSample with replacement (size 20): {sample_wr}")
print(f"All unique: {len(set(sample_wr)) == 20}")   # likely False

# 5. Weighted choice
colors = np.array(["A", "B", "C"])
probs = [0.7, 0.2, 0.1]
choices = np.random.choice(colors, size=100, p=probs)

# Count occurrences
for color in colors:
    count = np.sum(choices == color)
    print(f"\n{color}: {count} times ({count}%)")
# Expected: A ~70, B ~20, C ~10