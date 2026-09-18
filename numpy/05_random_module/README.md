# 05 - Random Module

## What Is This Chapter?

NumPy has a complete module for generating random numbers. This chapter is the foundation of all ML and Deep Learning techniques — train/test split, mini-batch, weight initialization, data augmentation, dropout. Without Random, ML is impossible.

## 1. Basic Random Functions

### Scenario

You want to initialize 5 sensors with random values (calibration). Or in ML, initialize neural network weights randomly.

### Functions

| Function | Output | Range |
|---|---|---|
| `np.random.rand(n)` | n floats | [0, 1) — uniform |
| `np.random.randn(n)` | n floats | Standard normal |
| `np.random.randint(low, high, n)` | n integers | [low, high) |
| `np.random.uniform(low, high, n)` | n floats | [low, high) |

### Code

```python
import numpy as np

rand_arr = np.random.rand(5)
randn_arr = np.random.randn(5)
randint_arr = np.random.randint(1, 10, 5)
uniform_arr = np.random.uniform(10, 20, 5)

initial_offsets = np.random.uniform(-0.5, 0.5, 5)
```

## 2. Probability Distributions

### Simple Concepts

- **Uniform:** All values equally likely. Example: dice.
- **Normal:** Most values near mean. Example: human height, sensor temperature.
- **Binomial:** Number of successes in n trials. Example: 10 coin flips.
- **Poisson:** Event count per time interval. Example: emails per hour.

### Code

```python
import numpy as np

# Normal
temps = np.random.normal(25, 3, 1000)

# Uniform
uniform = np.random.uniform(0, 100, 1000)

# Binomial
flips = np.random.binomial(10, 0.5, 1000)

# Poisson
events = np.random.poisson(5, 1000)
```

### Applications in Intelligent Systems

- **Sensor noise:** `np.random.normal(0, sensor_noise, n)`
- **Monte Carlo:** thousands of scenarios
- **Data Augmentation:** random noise on images

## 3. Shuffle and Choice

### Scenario

- **Shuffle:** before training, mix the data so the model doesn't learn order.
- **Choice:** random sample from data.

### Functions

| Function | Purpose |
|---|---|
| `np.random.shuffle(arr)` | Shuffles in-place (returns None) |
| `np.random.permutation(arr)` | Returns shuffled copy |
| `np.random.choice(arr, size, replace)` | Random sample |

### Code

```python
import numpy as np

data = np.arange(10)
np.random.shuffle(data)

data = np.arange(10)
perm = np.random.permutation(data)

sample = np.random.choice(np.arange(100), size=5, replace=False)

colors = np.array(["A", "B", "C"])
probs = [0.7, 0.2, 0.1]
choices = np.random.choice(colors, size=100, p=probs)
```

**Note:** `shuffle` works in-place. To keep the original, use `permutation`.

## 4. Random Seed — Reproducibility

### Scenario

You want your experiment results to be **reproducible**. Each time you run the code, the same random numbers are generated.

### Concept

`np.random.seed(n)` sets a starting point. With the same seed, always the same numbers.

### Code

```python
import numpy as np

# Without seed — different every run
print(np.random.rand(3))

# With seed — same every time
np.random.seed(42)
print(np.random.rand(3))

np.random.seed(42)
print(np.random.rand(3))   # same as above

# Modern API — recommended
rng = np.random.default_rng(seed=42)
print(rng.random(3))
```

**Why important?**

- **Debugging:** reproduce exact error
- **Research:** others can verify results
- **Testing:** deterministic tests
- **Comparison:** fair model comparison on same data split

## 5. Random in ML

### Real Scenarios

Five main uses of Random in ML:

1. **Train/Test Split:** separate training and test data
2. **Mini-batch Sampling:** random sample selection in SGD
3. **Weight Initialization:** initial weights (He init)
4. **Data Augmentation:** random data transformation
5. **Dropout:** randomly disable neurons

### Code

```python
import numpy as np

# 1. Train/Test split
data = np.arange(100)
indices = np.random.permutation(len(data))
train_idx = indices[:80]
test_idx = indices[80:]

# 2. Mini-batch
batch_size = 16
for i in range(0, len(train_idx), batch_size):
    batch = data[train_idx[i:i + batch_size]]

# 3. He init
n_inputs, n_outputs = 100, 50
weights = np.random.randn(n_inputs, n_outputs) * np.sqrt(2.0 / n_inputs)

# 4. Data augmentation
signal = np.sin(np.linspace(0, 4*np.pi, 100))
noisy_signal = signal + np.random.normal(0, 0.1, 100)

# 5. Dropout
activations = np.random.rand(10)
dropout_mask = np.random.rand(10) > 0.3
dropped = activations * dropout_mask
```

## Key Takeaways

1. `np.random.rand` for uniform [0, 1), `randn` for standard normal.
2. `randint` for integers, `uniform` for custom range.
3. Distributions: Normal (mean + std), Binomial (n + p), Poisson (lambda).
4. `shuffle` in-place, `permutation` copy, `choice` sampling.
5. `np.random.seed(n)` for reproducibility.
6. `default_rng(seed)` is the modern approach.
7. Random is fundamental to ML — train/test, mini-batch, init, augmentation.

## Exercises

| Number | Title | File |
|---|---|---|
| 01 | Random Basics | `exercise_01.py` |
| 02 | Distributions | `exercise_02.py` |
| 03 | Shuffle & Choice | `exercise_03.py` |
| 04 | Seed & Reproducibility | `exercise_04.py` |
| 05 | Random for ML | `exercise_05.py` |

## Q&A / Key Insights

### Q: Difference between `rand` and `randn`?
**A:** `rand` produces uniform values in [0, 1). `randn` produces values from standard normal distribution (mean 0, std 1). For noise simulation, `randn` is more appropriate.

### Q: Difference between `shuffle` and `permutation`?
**A:** `shuffle` works **in-place** on the array. `permutation` returns a shuffled copy. To keep the original, use `permutation`.

### Q: Why is `np.random.seed` important?
**A:** Reproducibility. For debugging, fair model comparison, and deterministic tests. With a specific seed, results are always identical.

### Q: What's the difference between `default_rng` and `np.random.seed`?
**A:** `default_rng` is the modern approach (NumPy 1.17+) and returns a Generator object. Better API and isolation. For new code, use `default_rng`.

### Q: What is He initialization?
**A:** A method for initializing neural network weights. `randn * sqrt(2 / n_inputs)` — standard deviation proportional to input count. Improves training.