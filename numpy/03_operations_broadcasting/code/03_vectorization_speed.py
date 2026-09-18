# 03_operations_broadcasting/code/03_vectorization_speed.py
# Vectorization speed comparison

import numpy as np
import time

size = 1_000_000

# Python list approach
py_list = list(range(size))

start = time.time()
result_list = [x * 2 for x in py_list]
list_time = time.time() - start
print(f"Python list comprehension: {list_time:.4f} seconds")

# NumPy approach
np_array = np.arange(size)

start = time.time()
result_array = np_array * 2
numpy_time = time.time() - start
print(f"NumPy vectorization:       {numpy_time:.4f} seconds")

# Speedup
speedup = list_time / numpy_time
print(f"\nNumPy is {speedup:.1f}x faster")

# Memory comparison
import sys
list_memory = sys.getsizeof(py_list) + sum(sys.getsizeof(x) for x in py_list[:1000]) * 1000
array_memory = np_array.nbytes
print(f"\nList memory (approx): {list_memory / 1_000_000:.1f} MB")
print(f"Array memory:         {array_memory / 1_000_000:.1f} MB")