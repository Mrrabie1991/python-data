# ۰۳ - عملیات و Broadcasting

## این فصل چیست؟

این فصل نشان می‌دهد NumPy چطور عملیات ریاضی را روی آرایه‌ها انجام می‌دهد — بدون حلقه، سریع‌تر و خواناتر. شامل عملیات پایه، توابع ریاضی (ufuncs)، broadcasting، و توابع تجمیع (aggregation).

## ۱. عملیات ریاضی پایه

[فارسی] NumPy عملیات را **عنصر‌به‌عنصر (element-wise)** انجام می‌دهد.

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

a + b    # [11 22 33 44 55]
a - b    # [-9 -18 -27 -36 -45]
a * b    # [10 40 90 160 250]
b / a    # [10. 10. 10. 10. 10.]
a ** 2   # [1 4 9 16 25]
b % a    # [0 0 0 0 0]
b // a   # [10 10 10 10 10]

# Scalar broadcast
a + 10   # [11 12 13 14 15]
a * 3    # [3 6 9 12 15]

# Comparison (returns boolean array)
a > 2    # [False False  True  True  True]
```

**مقایسه با C++:**
```cpp
std::vector<int> result(5);
for (int i = 0; i < a.size(); i++) {
    result[i] = a[i] + b[i];
}
```
در NumPy: یک خط - `a + b`.

## ۲. [فارسی] Universal Functions (ufuncs)

[فارسی] ufuncs توابع ریاضی هستند که مستقیماً روی کل آرایه اعمال می‌شوند.

| ufunc | کار | مثال |
|---|---|---|
| `np.sqrt` | جذر | `np.sqrt([4, 9])` → `[2. 3.]` |
| `np.exp` | e^x | `np.exp([0, 1])` → `[1. 2.718]` |
| `np.log` | لگاریتم طبیعی | `np.log([1, np.e])` → `[0. 1.]` |
| `np.sin` / `np.cos` | مثلثاتی | `np.sin([0, np.pi/2])` → `[0. 1.]` |
| `np.abs` | قدر مطلق | `np.abs([-3, -5])` → `[3 5]` |
| `np.round` | گرد کردن | `np.round([1.4, 2.6])` → `[1. 3.]` |
| `np.floor` / `np.ceil` | کف/سقف | `np.floor([1.9, -1.1])` → `[1. -2.]` |

```python
arr = np.array([1, 4, 9, 16, 25])
np.sqrt(arr)                          # [1. 2. 3. 4. 5.]
np.exp([0, 1, 2])                     # [1. 2.718 7.389]
np.log([1, np.e, np.e**2])            # [0. 1. 2.]
np.sin([0, np.pi/2, np.pi])           # [0. 1. 0.]
```

## ۳. [فارسی] Vectorization — سرعت

[فارسی] NumPy در پشت صحنه از حلقه C استفاده می‌کند. نتیجه: سرعت ۱۰ تا ۱۰۰ برابر بیشتر از حلقه Python.

```python
import time

size = 1_000_000

# Python list
py_list = list(range(size))
start = time.time()
result_list = [x * 2 for x in py_list]
list_time = time.time() - start

# NumPy
np_array = np.arange(size)
start = time.time()
result_array = np_array * 2
numpy_time = time.time() - start

# NumPy is typically 20-50x faster
```

## ۴. [فارسی] Broadcasting — مفهوم

[فارسی] Broadcasting یعنی: گسترش خودکار آرایه‌های کوچک‌تر برای هم‌شکل شدن با بزرگ‌تر — **بدون کپی داده**.

```python
arr = np.array([1, 2, 3, 4, 5])
result = arr + 10   # [11 12 13 14 15]
# scalar 10 broadcast to shape (5,)
```

### قوانین Broadcasting

۱. اگر دو آرایه ابعاد یکسان داشته باشند → element-wise.

۲. اگر یکی ابعاد کمتری داشته باشد، ابعادش از **چپ** با ۱ اضافه می‌شود.

۳. در هر بُعد: اگر اندازه‌ها یکسان باشند یا یکی **۱** باشد → broadcast ممکن است.

۴. اگر هیچ‌کدام ۱ نباشند و یکسان هم نباشند → خطا.

```python
# scalar + array
() + (5,) → (5,)

# row + 2D
(3, 4) + (4,) → (3, 4) + (1, 4) → (3, 4)

# column + 2D
(3, 4) + (3, 1) → (3, 4)

# incompatible
(4,) + (3,) → ValueError
```

### مثال: بردار سطری در ماتریس

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row = np.array([10, 20, 30])

matrix + row
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]
# row به هر سطر اضافه می‌شود
```

### مثال: بردار ستونی در ماتریس

```python
col = np.array([[100], [200], [300]])

matrix + col
# [[101 102 103]
#  [204 205 206]
#  [307 308 309]]
# col به هر ستون اضافه می‌شود
```

## ۵. [فارسی] np.newaxis — اضافه کردن بُعد

[فارسی] `np.newaxis` یک بُعد جدید با اندازه ۱ اضافه می‌کند — برای کنترل broadcasting.

| عبارت | shape |
|---|---|
| `a` | `(3,)` |
| `a[:, np.newaxis]` | `(3, 1)` — ستونی |
| `a[np.newaxis, :]` | `(1, 3)` — سطری |

### چرا مهم است؟

بدون `np.newaxis`، ضرب دو بردار shape یکسان، element-wise است — نه outer product.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Element-wise (نه outer product)
a * b
# [10 40 90]

# Outer product با np.newaxis
a[:, np.newaxis] * b
# [[10 20 30]
#  [20 40 60]
#  [30 60 90]]
# a[:, np.newaxis] shape (3, 1), b shape (3,)
# Broadcast to (3, 3)
```

### کاربرد در Intelligent Systems

- **ماتریس فاصله:** فاصله هر نقطه از هر نقطه دیگر.
- **[فارسی] Kernel Methods:** در SVM و Gaussian Processes.
- **[فارسی] Attention:** در Transformerها (فاز ۴).

## ۶. [فارسی] Aggregations

توابعی که یک آرایه را به یک عدد (یا آرایه کوچک‌تر) کاهش می‌دهند.

| تابع | کار |
|---|---|
| `np.sum(arr)` | جمع کل |
| `np.mean(arr)` | میانگین |
| `np.std(arr)` | انحراف معیار |
| `np.var(arr)` | واریانس |
| `np.min(arr)` / `np.max(arr)` | کمینه / بیشینه |
| `np.argmin(arr)` / `np.argmax(arr)` | ایندکس کمینه / بیشینه |
| `np.median(arr)` | میانه |

### پارامتر axis

- `axis=None` (پیش‌فرض) → روی کل آرایه
- `axis=0` → ستون‌ها را جمع می‌کند (خروجی به اندازه ستون‌ها)
- `axis=1` → سطرها را جمع می‌کند (خروجی به اندازه سطرها)

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

np.sum(matrix)              # 45
np.sum(matrix, axis=0)      # [12 15 18] — per column
np.sum(matrix, axis=1)      # [6 15 24] — per row
np.mean(matrix, axis=0)     # [4. 5. 6.]
np.max(matrix, axis=0)      # [7 8 9]
```

**تشبیه:** `axis` یعنی "کدام بُعد را حذف کن." `axis=0` یعنی بُعد صفر (سطرها) حذف شود → نتیجه یک آرایه از جمع ستون‌ها.

## نکات کلیدی این فصل

1. عملیات NumPy همیشه element-wise است (مگر با broadcasting).
2. [فارسی] ufuncs توابع ریاضی عنصر‌به‌عنصر هستند — بدون حلقه.
3. [فارسی] Vectorization سرعت ۱۰ تا ۱۰۰ برابر بیشتر از حلقه Python است.
4. [فارسی] Broadcasting گسترش خودکار آرایه‌های کوچک‌تر است — بدون کپی داده.
5. قوانین broadcasting از راست به چپ: اگر ابعاد یکسان یا یکی ۱ باشد، امکان‌پذیر است.
6. [فارسی] `np.newaxis` یک بُعد اضافه می‌کند — برای کنترل شکل broadcast.
7. [فارسی] `axis` یعنی "کدام بُعد را حذف کن."
8. [فارسی] `axis=0` برای ستون‌ها، `axis=1` برای سطرها.

## تمرین‌ها

| شماره | عنوان | فایل |
|---|---|---|
| ۰۱ | عملیات ریاضی | `exercise_01.py` |
| ۰۲ | ufuncs | `exercise_02.py` |
| ۰۳ | Broadcasting پایه | `exercise_03.py` |
| ۰۴ | Broadcasting پیشرفته | `exercise_04.py` |
| ۰۵ | Aggregations | `exercise_05.py` |

## پرسش و پاسخ (Q&A)

### سوال: چرا `a * b` (دو بردار shape یکسان) نتیجه element-wise می‌دهد، نه outer product؟
**پاسخ:** NumPy وقتی shapeها یکسان باشند، عنصر‌به‌عنصر عمل می‌کند. برای outer product باید یک بردار را به شکل ستونی (`a[:, np.newaxis]`) تبدیل کنی تا broadcast اتفاق بیفتد و ماتریس ۲D ساخته شود.

### سوال: `np.newaxis` دقیقاً چه می‌کند؟
**پاسخ:** یک بُعد جدید با اندازه ۱ اضافه می‌کند. `a[:, np.newaxis]` بردار `(3,)` را به `(3, 1)` تبدیل می‌کند (ستونی) و `a[np.newaxis, :]` به `(1, 3)` (سطری). این بُعد اضافه باعث می‌شود broadcasting بین دو بردار ممکن شود و outer product ساخته شود.

### سوال: تفاوت `axis=0` و `axis=1` چیست؟
**پاسخ:** `axis=0` یعنی بُعد اول (سطرها) حذف شود — نتیجه از جمع ستون‌ها می‌آید. `axis=1` یعنی بُعد دوم (ستون‌ها) حذف شود — نتیجه از جمع سطرها می‌آید. به‌طور خلاصه: `axis` یعنی "کدام بُعد را حذف کنم."

### سوال: Broadcasting چه زمانی خطا می‌دهد؟
**پاسخ:** وقتی در یک بُعد، نه اندازه‌ها یکسان باشند، نه یکی از آن‌ها ۱ باشد. مثلاً `(4,) + (3,)` خطا می‌دهد چون ۴ و ۳ ناسازگارند.