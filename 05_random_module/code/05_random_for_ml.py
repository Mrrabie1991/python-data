# 05_random_module/code/05_random_for_ml.py
# Random operations used in ML

import numpy as np

# === 1. Train/Test Split ===
data = np.arange(100)
labels = np.random.randint(0, 2, 100)   # binary labels

# Shuffle indices
indices = np.random.permutation(len(data))

# Split
train_idx = indices[:80]
test_idx = indices[80:]

X_train, y_train = data[train_idx], labels[train_idx]
X_test, y_test = data[test_idx], labels[test_idx]

print(f"Train size: {len(X_train)}")
print(f"Test size:  {len(X_test)}")

# === 2. Mini-batch Sampling ===
batch_size = 8
n_batches = len(X_train) // batch_size

print(f"\nMini-batches ({n_batches} batches of {batch_size}):")
for i in range(n_batches):
    start = i * batch_size
    end = start + batch_size
    batch = X_train[start:end]
    print(f"  Batch {i}: {batch}")

# === 3. Weight Initialization ===
# He initialization for neural networks
n_inputs = 100
n_outputs = 50
weights = np.random.randn(n_inputs, n_outputs) * np.sqrt(2.0 / n_inputs)
print(f"\nWeight shape: {weights.shape}")
print(f"Weight mean:  {weights.mean():.4f}")   # ≈ 0
print(f"Weight std:   {weights.std():.4f}")    # small

# === 4. Data Augmentation (concept) ===
# Add random noise to signal
signal = np.sin(np.linspace(0, 4*np.pi, 100))
noise = np.random.normal(0, 0.1, 100)
noisy_signal = signal + noise
print(f"\nOriginal signal std: {signal.std():.4f}")
print(f"Noisy signal std:    {noisy_signal.std():.4f}")

# === 5. Dropout (concept) ===
# Randomly zero out some values
activations = np.random.rand(10)
dropout_mask = np.random.rand(10) > 0.3   # keep 70%
dropped = activations * dropout_mask
print(f"\nActivations: {activations}")
print(f"Dropout mask: {dropout_mask}")
print(f"After dropout: {dropped}")