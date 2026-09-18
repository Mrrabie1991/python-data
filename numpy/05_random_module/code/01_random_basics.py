# 05_random_module/code/01_random_basics.py
# Random basics

import numpy as np

# === rand — uniform [0, 1) ===
rand_arr = np.random.rand(5)
print(f"np.random.rand(5): {rand_arr}")

# 2D
rand_2d = np.random.rand(2, 3)
print(f"\nnp.random.rand(2, 3):\n{rand_2d}")

# === randn — standard normal (mean=0, std=1) ===
randn_arr = np.random.randn(5)
print(f"\nnp.random.randn(5): {randn_arr}")
# Values can be negative — around 0

# === randint — integers in [low, high) ===
randint_arr = np.random.randint(1, 10, 5)
print(f"\nnp.random.randint(1, 10, 5): {randint_arr}")
# 5 integers between 1 and 9

# === uniform — custom range ===
uniform_arr = np.random.uniform(10, 20, 5)
print(f"\nnp.random.uniform(10, 20, 5): {uniform_arr}")
# 5 values between 10 and 20

# === Sensor calibration example ===
initial_offsets = np.random.uniform(-0.5, 0.5, 5)
print(f"\nSensor offsets: {initial_offsets}")