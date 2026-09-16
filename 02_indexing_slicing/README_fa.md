# ۰۲ -[فارسی] Indexing و Slicing و روش‌های پیشرفته دسترسی

## این فصل چیست؟

این فصل روش‌های دسترسی به عناصر آرایه NumPy را پوشش می‌دهد. دسترسی ساده (indexing)، برش (slicing)، فیلتر با شرط (boolean masking)، انتخاب چندتایی (fancy indexing)، و انتخاب شرطی (np.where).

بدون این فصل، نمی‌توانی از داده‌های واقعی استفاده کنی — چون هر تحلیل داده با دسترسی و فیلتر شروع می‌شود.

## ۱.[فارسی]  Indexing — دسترسی به عناصر

در NumPy، برخلاف لیست‌های تو در تو، از یک براکت با کاما استفاده می‌کنی: `[row, col]`.

```python
import numpy as np

# 1D
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d[0])     # 10
print(arr_1d[-1])    # 50 — negative index from end

# 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 2])   # 6 — row 1, col 2
print(arr_2d[-1, -1]) # 9 — bottom-right
print(arr_2d[0])      # [1 2 3] — entire first row
```

**نکته:** `arr_2d[0]` یک آرایه (سطر) برمی‌گرداند، ولی `arr_2d[0, 0]` یک عدد (خونه مشخص).

**مقایسه با C++:**
```cpp
std::vector<std::vector<int>> matrix = {{1,2,3},{4,5,6}};
int val = matrix[1][0];   // row 1, col 0
```
در NumPy، `matrix[1, 0]` سریع‌تر از `matrix[1][0]` است — چون یک عملیات است، نه دو.

## ۲.[فارسی]  Slicing — برش

سینتکس: `arr[start:stop:step]` — مثل لیست پایتون، ولی روی آرایه‌های چندبعدی هم کار می‌کند.

```python
arr = np.arange(10)

arr[2:5]     # [2 3 4]
arr[:4]      # [0 1 2 3]
arr[6:]      # [6 7 8 9]
arr[::2]     # [0 2 4 6 8]
arr[::-1]    # [9 8 7 6 5 4 3 2 1 0] — reversed

# 2D
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

matrix[0:2, 1:3]   # rows 0-1, cols 1-2
matrix[:, 0]        # all rows, column 0
matrix[1, :]        # row 1, all columns
matrix[::2, ::2]    # every 2nd row and column
```

### نکته حیاتی: Slicing یک View برمی‌گرداند

[فارسی] Slicing یک view می‌سازد، نه یک copy. تغییر در برش، روی آرایه اصلی هم اثر می‌گذارد.

```python
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
view[0] = 99
print(original)   # [1 99 3 4 5] — original changed!
```

## ۳.[فارسی]  Boolean Masking

فیلتر کردن آرایه با شرط. بدون حلقه، همه عناصر منطبق را برمی‌گرداند.

```python
arr = np.array([1, 5, 8, 3, 10, 2, 7, 4])

# Basic mask
arr[arr > 5]                # [8 10 7]

# Combined conditions
arr[(arr > 3) & (arr < 8)]  # [5 7 4]
arr[(arr < 3) | (arr > 8)]  # [1 10 2]

# NOT
arr[~(arr > 5)]             # [1 5 3 2 4]

# Count matching
np.sum(arr > 5)             # 3
```

**نکته:** برای ترکیب شرط‌ها از `&` (and)، `|` (or)، `~` (not) استفاده کن — نه `and`، `or`، `not` پایتونی.

[فارسی] **Boolean masking یک Copy برمی‌گرداند** (برخلاف slicing).

**مقایسه با C++:**
```cpp
std::vector<int> result;
for (int x : vec) {
    if (x > 5) result.push_back(x);
}
```
در NumPy، یک خط: `arr[arr > 5]`

## ۴.[فارسی]  Fancy Indexing

دسترسی با آرایه‌ای از ایندکس‌ها.

```python
arr = np.array([10, 20, 30, 40, 50])

arr[[0, 2, 4]]         # [10 30 50]
arr[[4, 3, 2, 1, 0]]   # [50 40 30 20 10] — reorder
arr[[0, 0, 0]]         # [10 10 10] — duplicate

# 2D
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix[[0, 2]]                      # rows 0 and 2
matrix[[0, 1, 2], [0, 1, 2]]        # diagonal [1 5 9]
```

**نکته:** Fancy indexing **همیشه یک Copy برمی‌گرداند** — نه view. تغییر در نتیجه، روی آرایه اصلی اثر ندارد.

## ۵.[فارسی]  np.where — انتخاب شرطی

[فارسی] `np.where(condition, x, y)` معادل برداری `x if condition else y` است.

```python
arr = np.array([1, 5, 8, 3, 10, 2, 7, 4])

# Replace: where > 5, use 100; else 0
np.where(arr > 5, 100, 0)
# [0 0 100 0 100 0 100 0]

# Keep original or replace
np.where(arr > 5, arr, 0)
# [0 0 8 0 10 0 7 0]

# Find indices
np.where(arr > 5)
# (array([2, 4, 6]),)
```

### [فارسی]  np.where در 2D — یافتن مختصات

```python
matrix = np.array([[1, 5, 2],
                   [8, 3, 9],
                   [4, 7, 6]])

rows, cols = np.where(matrix > 5)
# rows: [1 1 2 2]
# cols: [0 2 1 2]

# هر جفت (row, col) یک عنصر منطبق را مشخص می‌کند:
# (1, 0) = 8, (1, 2) = 9, (2, 1) = 7, (2, 2) = 6
```

**نکته:** `np.where(condition)` برای آرایه‌های چندبعدی یک tuple از آرایه‌های ایندکس برمی‌گرداند — به ترتیب ابعاد (سطر، ستون).

**مقایسه با C++:**
```cpp
std::vector<int> result;
for (int x : vec) {
    result.push_back(x > 5 ? 100 : 0);
}
```
در NumPy: `np.where(arr > 5, 100, 0)` — یک خط.

## جدول خلاصه

| عملیات | نتیجه | View یا Copy |
|---|---|---|
| `arr[2]` | یک عنصر | — |
| `arr[1:4]` | زیرآرایه | View |
| `arr[arr > 5]` | عناصر منطبق | Copy |
| `arr[[0, 2, 4]]` | عناصر انتخابی | Copy |
| `np.where(cond, x, y)` | آرایه جدید | Copy |

## نکات کلیدی این فصل

1. در NumPy از `[row, col]` استفاده کن، نه `[row][col]` — سریع‌تر و پایتونیک‌تر.
2. [فارسی] Slicing یک view برمی‌گرداند؛ Boolean masking و Fancy indexing یک copy.
3. برای ترکیب شرط‌ها از `&`، `|`، `~` استفاده کن (نه `and`، `or`، `not`).
4. [فارسی] Fancy indexing می‌تواند عناصر را تکرار، بازچینش، یا انتخاب کند.
5. [فارسی] `np.where(condition)` برای یافتن مختصات عناصر منطبق استفاده می‌شود.
6. [فارسی] Boolean masking روی آرایه‌های ۲D، عناصر را flatten می‌کند.

## تمرین‌ها

| شماره | عنوان | فایل |
|---|---|---|
| ۰۱ | Indexing و Slicing پایه | `exercise_01.py` |
| ۰۲ | 2D Indexing | `exercise_02.py` |
| ۰۳ | Boolean Masking | `exercise_03.py` |
| ۰۴ | Fancy Indexing | `exercise_04.py` |
| ۰۵ | np.where | `exercise_05.py` |

## پرسش و پاسخ (Q&A)

### سوال: تفاوت `[row, col]` و `[row][col]` چیست؟
**پاسخ:** `[row, col]` یک عملیات است — مستقیم به خونه دسترسی می‌گیرد. `[row][col]` دو عملیات است — اول یک آرایه (سطر) می‌سازد، بعد از آن ایندکس می‌گیرد. در NumPy، فرم اول سریع‌تر و پایتونیک‌تر است.

### سوال: چرا در Boolean masking باید از `&` استفاده کنم نه `and`؟
**پاسخ:** `and` و `or` پایتونی روی مقادیر boolean کار می‌کنند، نه روی آرایه. NumPy نیاز دارد که عملیات bitwise (`&`، `|`، `~`) روی کل آرایه اعمال شود.

### سوال: چرا `matrix[matrix > 5]` یک آرایه 1D برمی‌گرداند؟
**پاسخ:** Boolean masking عناصر منطبق را از کل ماتریس استخراج و flatten می‌کند. مختصات اصلی را می‌توانی با `np.where` پیدا کنی.

### سوال: Slicing view برمی‌گرداند، چطور یک copy بگیرم؟
**پاسخ:** از `.copy()` استفاده کن: `arr[1:4].copy()`. یا در 2D: `arr[0:2, 1:3].copy()`.

### سوال: `np.where` با یک پارامتر چه می‌کند؟
**پاسخ:** وقتی فقط شرط بدهی، `np.where` ایندکس عناصری که شرط را برآورده می‌کنند برمی‌گرداند (به صورت tuple از آرایه‌ها — یکی برای هر بُعد).