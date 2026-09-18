# 05_random_module/exercises/exercise_05.py
# Exercise 05: Random for ML
#
# Requirements:
# 1. Create 200 data points with np.arange(200)
# 2. Shuffle and split into train (80%) and test (20%)
# 3. Create mini-batches of size 16
# 4. Initialize a weight matrix of shape (100, 50) with He initialization
# 5. Verify the mean of the weights is close to 0

import numpy as np

np.random.seed(42)

# 1. Data
data = np.arange(200)
print(f"Total data: {len(data)}")

# 2. Train/test split
indices = np.random.permutation(len(data))

train_size = int(0.8 * len(data))   # 160
train_idx = indices[:train_size]
test_idx = indices[train_size:]

X_train = data[train_idx]
X_test = data[test_idx]

print(f"\nTrain size: {len(X_train)}")
print(f"Test size:  {len(X_test)}")
print(f"Train sample: {X_train[:5]}")
print(f"Test sample:  {X_test[:5]}")

# 3. Mini-batches
batch_size = 16
n_batches = len(X_train) // batch_size
print(f"\nMini-batches: {n_batches} batches of {batch_size}")

for i in range(n_batches):
    start = i * batch_size
    end = start + batch_size
    batch = X_train[start:end]
    print(f"  Batch {i}: size {len(batch)}, first value {batch[0]}")

# 4. He initialization for neural network weights
# He init: randn * sqrt(2 / n_inputs)
n_inputs = 100
n_outputs = 50

weights = np.random.randn(n_inputs, n_outputs) * np.sqrt(2.0 / n_inputs)
print(f"\nWeight matrix shape: {weights.shape}")
print(f"Weight mean:  {weights.mean():.6f}")   # ≈ 0
print(f"Weight std:   {weights.std():.6f}")    # ≈ sqrt(2/100) = 0.1414

# 5. Verify mean is close to zero
print(f"\nMean is close to 0? {abs(weights.mean()) < 0.01}")   # True