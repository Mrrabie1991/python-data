# 03_operations_broadcasting/code/09_nan_handling.py
# NaN handling — dealing with missing data

import numpy as np

arr = np.array([1.0, 2.0, np.nan, 4.0, 5.0, np.nan, 7.0])
print(f"Array: {arr}")

# === Regular aggregations return NaN ===
print(f"\nsum:   {np.sum(arr)}")       # nan
print(f"mean:  {np.mean(arr)}")        # nan
print(f"max:   {np.max(arr)}")         # nan

# === NaN-aware aggregations ===
print(f"\nnansum:   {np.nansum(arr)}")       # 19.0
print(f"nanmean:  {np.nanmean(arr)}")        # 3.8
print(f"nanmax:   {np.nanmax(arr)}")         # 7.0
print(f"nanmin:   {np.nanmin(arr)}")         # 1.0
print(f"nanstd:   {np.nanstd(arr):.4f}")     # std ignoring NaN

# === Check for NaN ===
print(f"\nIs NaN?          {np.isnan(arr)}")
print(f"Any NaN?         {np.any(np.isnan(arr))}")    # True
print(f"Count NaN:       {np.sum(np.isnan(arr))}")    # 2
print(f"Count not NaN:   {np.sum(~np.isnan(arr))}")   # 5

# === Remove NaN ===
clean = arr[~np.isnan(arr)]
print(f"\nCleaned array: {clean}")
print(f"Mean:          {np.mean(clean):.2f}")

# === Special NaN behavior ===
print(f"\nnp.nan == np.nan:  {np.nan == np.nan}")    # False!
print(f"np.isnan(np.nan):  {np.isnan(np.nan)}")      # True

# NaN comparison is always False — must use np.isnan()