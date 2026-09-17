# 03_operations_broadcasting/exercises/exercise_05.py
# Exercise 05: Aggregations and axis
#
# Requirements:
# 1. Create data = np.random.randint(1, 100, (5, 4))
# 2. Compute total sum, mean, min, max
# 3. Compute sum per column (axis=0) and per row (axis=1)
# 4. Find index of max value in each row
# 5. Compute standard deviation per row

import numpy as np

np.random.seed(42)
data = np.random.randint(1, 100, (5, 4))
print(f"Data:\n{data}")

# 2. Global statistics
print(f"\nTotal sum: {np.sum(data)}")
print(f"Mean:      {np.mean(data):.2f}")
print(f"Min:       {np.min(data)}")
print(f"Max:       {np.max(data)}")

# 3. Sums per axis
print(f"\nSum axis=0 (per column): {np.sum(data, axis=0)}")
print(f"Sum axis=1 (per row):    {np.sum(data, axis=1)}")

# 4. Argmax per row
print(f"\nArgmax per row: {np.argmax(data, axis=1)}")

# 5. Std per row
print(f"Std per row:    {np.std(data, axis=1)}")