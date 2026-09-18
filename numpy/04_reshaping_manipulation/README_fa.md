# ۰۴ - تغییر شکل و دستکاری آرایه

## این فصل چیست؟

این فصل درباره تغییر شکل و ترکیب آرایه‌هاست. reshape، transpose، concatenate، split، و تفاوت عمیق view/copy. این مفاهیم در Deep Learning (فاز ۴) و پردازش تصویر (فاز ۵) حیاتی هستند — هرجا با tensor یا ماتریس چندبعدی کار کنی، از این‌ها استفاده می‌کنی.

## ۱.[فارسی] reshape — تغییر شکل

### سناریو

داده سنسور رو به صورت یک بردار طولانی ذخیره کردی. می‌خوای به شکل ماتریس ببینی (۳ سنسور × ۴ زمان).

### قانون طلایی

تعداد کل عناصر باید ثابت بماند. `12 = 3 × 4 = 2 × 3 × 2`

```python
import numpy as np

arr = np.arange(12)

# Reshape to 3x4
matrix = arr.reshape(3, 4)
print(matrix)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Using -1 for auto-calculate
auto = arr.reshape(2, -1)   # -1 = 6
print(auto.shape)   # (2, 6)

# 3D reshape
tensor = arr.reshape(2, 3, 2)
print(tensor.shape)   # (2, 3, 2)

# Flatten back to 1D
flat = tensor.reshape(-1)
print(flat)   # [0 1 2 ... 11]
```

**نکته:** `reshape` در صورت امکان یک **view** برمی‌گرداند (نه copy). تغییر در نتیجه، روی آرایه اصلی اثر می‌گذارد.

```python
view = arr.reshape(3, 4)
view[0, 0] = 99
print(arr)   # [99 1 2 3 ...] — arr changed
```

## ۲.[فارسی]  ravel vs flatten

### تفاوت کلیدی

- **[فارسی] `ravel()`** — بردار ۱D برمی‌گرداند. اگر ممکن باشد، **view** می‌سازد.
- **[فارسی] `flatten()`** — همیشه **copy** برمی‌گرداند.

### کدام استفاده کنیم؟

- فقط خواندن → `ravel()` (سریع‌تر، حافظه کمتر)
- تغییر بدون تأثیر روی اصلی → `flatten()`

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# ravel — view
raveled = matrix.ravel()
raveled[0] = 99
print(matrix)   # [[99 2 3] [4 5 6]] — matrix changed

# Reset
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# flatten — copy
flattened = matrix.flatten()
flattened[0] = 99
print(matrix)   # [[1 2 3] [4 5 6]] — unchanged
```

## ۳.[فارسی]  transpose و .T

### سناریو

داده‌ها رو به شکل (سنسور، زمان) ذخیره کردی. حالا می‌خواهی (زمان، سنسور).

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"Shape: {matrix.shape}")   # (2, 3)

# .T reverses axes
transposed = matrix.T
print(f"Shape: {transposed.shape}")   # (3, 2)
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]
```

### [فارسی]  3D transpose با محورهای سفارشی

```python
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"Original shape: {arr_3d.shape}")   # (2, 3, 4)

# transpose(2, 0, 1) — new axes order
# new axis 0 = old axis 2 (size 4)
# new axis 1 = old axis 0 (size 2)
# new axis 2 = old axis 1 (size 3)
transposed = arr_3d.transpose(2, 0, 1)
print(f"After transpose(2, 0, 1): {transposed.shape}")   # (4, 2, 3)

# Default .T reverses all axes
print(f"After .T: {arr_3d.T.shape}")   # (4, 3, 2)
```

### کاربرد در Intelligent Systems

- [فارسی]  **Sensor data:** تبدیل (sensors × time) به (time × sensors)
- [فارسی]  **Image processing:** تبدیل (height × width × channels) به (channels × height × width) برای PyTorch
- [فارسی]  **Deep Learning:** transpose در Attention و Matrix Multiplication

## ۴. [فارسی]  Concatenate — اتصال

### سناریو

سه خط تولید داری. هر خط یک بردار داده فرستاده. می‌خواهی همه رو به یک بردار بزرگ وصل کنی.

### توابع

| تابع | کار |
|---|---|
| `np.concatenate([a, b])` | اتصال روی محور موجود |
| `np.vstack([a, b])` | اتصال عمودی (روی سطرها) |
| `np.hstack([a, b])` | اتصال افقی (روی ستون‌ها) |
| `np.stack([a, b])` | روی **بُعد جدید** |

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 1D concatenate
print(np.concatenate([a, b]))   # [1 2 3 4 5 6]

# 2D
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# Vertical (axis=0)
print(np.concatenate([m1, m2], axis=0))
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Horizontal (axis=1)
print(np.concatenate([m1, m2], axis=1))
# [[1 2 5 6]
#  [3 4 7 8]]

# Shortcuts
print(np.vstack([m1, m2]))   # same as concatenate axis=0
print(np.hstack([m1, m2]))   # same as concatenate axis=1

# stack — adds a NEW dimension
stacked = np.stack([m1, m2], axis=0)
print(stacked.shape)   # (2, 2, 2)
```

**تفاوت concatenate و stack:**
- [فارسی]  `concatenate`: اتصال روی محور **موجود**
- [فارسی]  `stack`: روی یک **محور جدید** (بُعد جدید)

## ۵. [فارسی]  Split — جداسازی

### سناریو

یک داده طولانی داری. می‌خواهی به بخش‌های مساوی تقسیم کنی (مثلاً split train/test).

```python
arr = np.arange(12)

# Split into 3 equal parts
parts = np.split(arr, 3)
# [array([0, 1, 2, 3]), array([4, 5, 6, 7]), array([8, 9, 10, 11])]

# Split at specific indices
parts = np.split(arr, [3, 7])
# [array([0, 1, 2]), array([3, 4, 5, 6]), array([7, 8, 9, 10, 11])]

# 2D split
matrix = np.arange(16).reshape(4, 4)

# vsplit — by rows
vparts = np.vsplit(matrix, 2)
# 2 arrays of shape (2, 4)

# hsplit — by columns
hparts = np.hsplit(matrix, 2)
# 2 arrays of shape (4, 2)
```

## ۶. [فارسی]  View vs Copy — نگاه عمیق

### قانون کلی

| عملیات | نتیجه |
|---|---|
| Slicing (`arr[1:4]`) | **View** |
| `reshape`, `ravel` | **View** (اگر ممکن) |
| `.T`, `transpose` | **View** |
| `flatten()` | **Copy** |
| `copy()` | **Copy** |
| `astype()` | **Copy** |
| عملیات ریاضی (`+`, `*`) | **Copy** |
| Boolean masking (`arr[arr > 5]`) | **Copy** |
| Fancy indexing (`arr[[0, 2]]`) | **Copy** |
| `concatenate`, `stack` | **Copy** |

### [فارسی] `.base`

اگر آرایه یک view باشد، `.base` به آرایه اصلی اشاره می‌کند. اگر `.base is None` باشد، آرایه مالک داده است.

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr.base is None)                       # True — owns data
print(arr[1:4].base is not None)              # True — view
print(arr.reshape(5, 1).base is not None)     # True — view
print(arr[1:4].copy().base is None)           # True — copy
print(arr.flatten().base is None)             # True — copy
```

### تله رایج

```python
# BAD: view will modify original
arr = np.array([1, 2, 3, 4, 5])
view = arr[1:4]
view[0] = 99
print(arr)   # [1 99 3 4 5] — arr changed!

# GOOD: copy protects original
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()
copy[0] = 99
print(arr)   # [1 2 3 4 5] — arr unchanged
```

## جدول خلاصه

| عملیات | معنی | View/Copy |
|---|---|---|
| `arr.reshape(3, 4)` | تغییر شکل | View |
| `arr.ravel()` | صاف کردن | View |
| `arr.flatten()` | صاف کردن | Copy |
| `arr.T` | جابجایی | View |
| `np.concatenate([a, b])` | اتصال | Copy |
| `np.stack([a, b])` | اتصال روی بُعد جدید | Copy |
| `np.split(arr, n)` | تقسیم | View |

## نکات کلیدی این فصل

1. [فارسی]  `reshape` شکل را تغییر می‌دهد — تعداد عناصر باید ثابت بماند.
2. [فارسی]  `-1` در reshape یعنی "خودت حساب کن".
3. [فارسی]  `ravel` view برمی‌گرداند (اگر ممکن)، `flatten` همیشه copy.
4. [فارسی]  `transpose` و `.T` view برمی‌گردانند.
5. [فارسی]  `transpose(2, 0, 1)` برای تغییر ترتیب محورها.
6. [فارسی]  `concatenate` روی محور موجود، `stack` روی محور جدید.
7. [فارسی]  `vstack` (عمودی) و `hstack` (افقی) shortcut هستند.
8. [فارسی]  `split`, `vsplit`, `hsplit` برای جداسازی.
9. [فارسی]  `.base is None` نشان می‌دهد آرایه مالک داده است.
10. برای امنیت، وقتی می‌خواهی نسخه مستقل داشته باشی از `.copy()` استفاده کن.

## تمرین‌ها

| شماره | عنوان | فایل |
|---|---|---|
| ۰۱ | reshape و ravel | `exercise_01.py` |
| ۰۲ | transpose | `exercise_02.py` |
| ۰۳ | Concatenate و Stack | `exercise_03.py` |
| ۰۴ | Split | `exercise_04.py` |
| ۰۵ | View vs Copy | `exercise_05.py` |

## پرسش و پاسخ (Q&A)

### سوال: `reshape` یک view است یا copy؟
**پاسخ:** اگر ممکن باشد، view. یعنی داده مشترک است و تغییر در یکی روی دیگری اثر می‌گذارد. برای copy صریح، از `.reshape(...).copy()` استفاده کن.

### سوال: تفاوت `ravel` و `flatten` چیست؟
**پاسخ:** `ravel` در صورت امکان view برمی‌گرداند (بدون کپی داده). `flatten` همیشه copy برمی‌گرداند. برای خواندن، `ravel` سریع‌تر است؛ برای استقلال، `flatten`.

### سوال: تفاوت `concatenate` و `stack` چیست؟
**پاسخ:** `concatenate` روی یک محور **موجود** اتصال می‌دهد (مثلاً چسباندن دو ماتریس روی سطرها). `stack` روی یک محور **جدید** — یعنی یک بُعد اضافه می‌کند.

### سوال: چه زمانی `.copy()` استفاده کنم؟
**پاسخ:** وقتی می‌خواهی از داده اصلی محافظت کنی. اگر نتیجه view باشد و آن را تغییر بدهی، آرایه اصلی هم تغییر می‌کند.

### سوال: `transpose(2, 0, 1)` یعنی چه؟
**پاسخ:** ترتیب محورهای جدید را مشخص می‌کند. `transpose(2, 0, 1)` یعنی: محور ۰ جدید = محور ۲ قدیم، محور ۱ جدید = محور ۰ قدیم، محور ۲ جدید = محور ۱ قدیم.