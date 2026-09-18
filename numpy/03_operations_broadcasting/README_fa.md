# ۰۳ - عملیات، Broadcasting و Aggregation

## این فصل چیست؟

[فارسی] NumPy در پشت صحنه یک حلقه C سریع اجرا می‌کند. این فصل نشان می‌دهد چطور از این قدرت استفاده کنی: عملیات روی کل آرایه بدون حلقه، گسترش خودکار (broadcasting)، و تجمیع (aggregation). این سه مفهوم، ستون فقرات کار با داده در NumPy هستند.

## ۱. عملیات ریاضی پایه

### سناریو

سه خط تولید داری. دما هر خط رو در دو زمان مختلف ثبت کردی:

```
خط ۱ الان:   [20, 22, 25, 24]
خط ۱ دیروز:  [18, 20, 23, 22]
```

می‌خوای ببینی اختلاف دما چقدر بوده. در C++ باید حلقه بنویسی. در NumPy یک خط.

### کد

```python
import numpy as np

now = np.array([20, 22, 25, 24])
yesterday = np.array([18, 20, 23, 22])

# Element-wise difference
diff = now - yesterday
print(diff)   # [2 2 2 2]

# All math operations work element-wise
print(now + yesterday)   # [38 42 48 46]
print(now * 2)           # [40 44 50 48]
print(now / 2)           # [10. 11. 12.5 12.]
print(now ** 2)          # [400 484 625 576]
```

**مقایسه با C++:**
```cpp
std::vector<int> diff(4);
for (int i = 0; i < now.size(); i++) {
    diff[i] = now[i] - yesterday[i];
}
```
در NumPy: `now - yesterday` — یک خط.

## ۲.[فارسی]  ufuncs — توابع ریاضی برداری

### سناریو

یه سنسور دما مقادیر ولتاژ می‌دهد که باید به دما تبدیل شوند (رابطه خطی با لگاریتم). یا در پردازش سیگنال، باید سینوس و کسینوس روی هزاران نمونه حساب کنی.

### کد

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])

# Square root
print(np.sqrt(arr))   # [1. 2. 3. 4. 5.]

# Exponential and log
print(np.exp([0, 1, 2]))                 # [1. 2.718 7.389]
print(np.log([1, np.e, np.e**2]))        # [0. 1. 2.]

# Trig
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))   # [0. 1. 0.]
print(np.cos(angles))   # [1. 0. -1.]

# Rounding
floats = np.array([1.4, 2.6, -1.5, -2.5])
print(np.round(floats))   # [1. 3. -2. -2.]
print(np.floor(floats))   # [1. 2. -2. -3.]
print(np.ceil(floats))    # [2. 3. -1. -2.]
```

**مقایسه با C++:**
```cpp
std::vector<double> result;
for (double x : vec) {
    result.push_back(std::sqrt(x));
}
```
در NumPy: `np.sqrt(vec)` — یک خط.

## ۳. [فارسی]  Vectorization — چرا سریع‌تر است؟

### سناریو

می‌خوای ۱ میلیون داده سنسور رو در ۲ ضرب کنی (تبدیل واحد). با لیست پایتون ۵۰ ثانیه طول می‌کشه، با NumPy ۲ ثانیه.

### کد

```python
import numpy as np
import time

size = 1_000_000

# Python list
py_list = list(range(size))
start = time.time()
result_list = [x * 2 for x in py_list]
print(f"List: {time.time() - start:.4f}s")

# NumPy
np_array = np.arange(size)
start = time.time()
result_array = np_array * 2
print(f"NumPy: {time.time() - start:.4f}s")
```

**خروجی نمونه:**
```
List:  0.0842s
NumPy: 0.0031s
NumPy is 27x faster
```

**چرا؟** NumPy از یک حلقه C استفاده می‌کند، نه حلقه Python. علاوه بر این، حافظه کم‌مصرف‌تر است.

## ۴. [فارسی]  Broadcasting — گسترش خودکار

### سناریو ۱: تبدیل واحد (scalar + array)

داده‌ها درجه سانتی‌گراد هستند، می‌خوای به فارنهایت تبدیل کنی:

```python
celsius = np.array([20, 25, 30, 35, 40])
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)   # [68. 77. 86. 95. 104.]
```

عدد `9/5` و `32` به‌طور خودکار روی کل آرایه گسترش می‌یابند.

### سناریو ۲: کالیبراسیون (row + matrix)

سه سنسور داری، هر سنسور ۴ بار اندازه‌گیری کرده:

```python
data = np.array([
    [10, 11, 12, 13],   # sensor 1
    [20, 21, 22, 23],   # sensor 2
    [30, 31, 32, 33]    # sensor 3
])

# Every sensor has an offset (calibration)
offsets = np.array([1, 2, 3, 4])

calibrated = data + offsets
print(calibrated)
# [[11 13 15 17]
#  [21 23 25 27]
#  [31 33 35 37]]
```

[فارسی] `offsets` با shape `(4,)` به هر سطر `data` اضافه می‌شود.

### سناریو ۳: نرمال‌سازی (column + matrix)

```python
col = np.array([[100], [200], [300]])
result = data + col
# col به هر ستون اضافه می‌شود
```

### قوانین Broadcasting

۱. اگر دو آرایه ابعاد یکسان داشته باشند → element-wise.

۲. اگر یکی ابعاد کمتری داشته باشد، ابعادش از **چپ** با ۱ اضافه می‌شود.

۳. در هر بُعد: اگر اندازه‌ها یکسان باشند یا یکی **۱** باشد → broadcast ممکن است.

۴. اگر هیچ‌کدام ۱ نباشند و یکسان هم نباشند → خطا.

```
scalar + array       ()      + (5,)    → (5,)
row + 2D             (4,)    + (3, 4)  → (1, 4) + (3, 4) → (3, 4)
column + 2D          (3, 1)  + (3, 4)  → (3, 4)
incompatible         (4,)    + (3,)    → ValueError
```

## ۵. [فارسی]  np.newaxis — کنترل شکل broadcast

### سناریو

داری ۳ نقطه در فضای ۱بعدی. می‌خوای **ماتریس فاصله** بسازی — فاصله هر نقطه از هر نقطه دیگه.

```python
points = np.array([1, 5, 9])

# Element-wise (اشتباه برای ماتریس فاصله)
points - points   # [0 0 0] — نمی‌خوایم این

# Outer difference با np.newaxis
diff_matrix = points[:, np.newaxis] - points
print(diff_matrix)
# [[ 0 -4 -8]
#  [ 4  0 -4]
#  [ 8  4  0]]
```

| عبارت | Shape |
|---|---|
| `points` | `(3,)` |
| `points[:, np.newaxis]` | `(3, 1)` — ستونی |
| `points[np.newaxis, :]` | `(1, 3)` — سطری |

با `np.newaxis`، یک بُعد جدید اضافه می‌شود تا broadcasting بین دو بردار ممکن شود.

**کاربرد:** ماتریس فاصله، Kernel Methods در SVM، Attention در Transformerها (فاز ۴).

## ۶. [فارسی]  Aggregation — تجمیع

### سناریو ۱: آمار پایه

```python
sales = np.array([100, 250, 180, 300, 220, 150, 280])
print(f"Sum:     {np.sum(sales)}")        # 1480
print(f"Mean:    {np.mean(sales):.2f}")   # 211.43
print(f"Std:     {np.std(sales):.2f}")
print(f"Max:     {np.max(sales)}")        # 300
print(f"Argmax:  {np.argmax(sales)}")     # 3 (index)
print(f"Median:  {np.median(sales)}")     # 220
```

### سناریو ۲: axis — تجمیع روی یک بُعد

سه خط تولید، هر خط ۴ ساعت داده:

```python
data = np.array([
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]
])

# Sum per column (axis=0)
print(np.sum(data, axis=0))   # [60 63 66 69]

# Sum per row (axis=1)
print(np.sum(data, axis=1))   # [46 86 126]
```

**قانون:** `axis` یعنی "کدام بُعد را حذف کن."
- [فارسی]  `axis=0` → بُعد اول (سطرها) حذف → نتیجه جمع ستون‌ها.
- [فارسی]  `axis=1` → بُعد دوم (ستون‌ها) حذف → نتیجه جمع سطرها.

### سناریو ۳: keepdims — حفظ ابعاد

می‌خوای هر خط تولید رو نسبت به میانگین خودش نرمال کنی:

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Mean per row with keepdims
row_means = np.mean(data, axis=1, keepdims=True)
# shape (3, 1)

normalized = data - row_means
print(normalized)
# [[-10.   0.  10.]
#  [-10.   0.  10.]
#  [-10.   0.  10.]]
```

**چرا `keepdims`؟** بدون آن، `row_means` شکل `(3,)` می‌گیرد و نمی‌تواند مستقیم از `data` (با شکل `(3, 3)`) کم شود. با `keepdims=True`، شکل `(3, 1)` می‌ماند و broadcasting ممکن می‌شود.

### سناریو ۴: Aggregation با شرط

```python
sales = np.array([100, 500, 250, 800, 150, 1200, 300, 200])

# Sum of high sales (> 300)
print(np.sum(sales[sales > 300]))   # 2300

# Count of even sales
print(np.count_nonzero(sales % 2 == 0))   # 6

# Mean of low sales (< 200)
print(np.mean(sales[sales < 200]))   # 125.0
```

## ۷. [فارسی]  NaN Handling — داده‌های گمشده

### سناریو

سنسور دما هر دقیقه داده می‌فرسته، ولی گاهی قطع می‌شود. `NaN` یعنی "داده ندارم".

```python
temps = np.array([22.5, 23.1, np.nan, 24.3, np.nan, 25.0, 26.2])

# Regular mean → NaN
print(np.mean(temps))   # nan

# NaN-aware mean
print(np.nanmean(temps))   # 24.22

# Count NaN
print(np.sum(np.isnan(temps)))   # 2

# Remove NaN
clean = temps[~np.isnan(temps)]
print(clean)   # [22.5 23.1 24.3 25.0 26.2]
```

**نکته:** `NaN == NaN` همیشه `False` است — از `np.isnan()` استفاده کن.

## ۸. [فارسی] Cumulative — عملیات تجمعی

### سناریو

مصرف روزانه برق کارخونه:

```python
daily = np.array([100, 150, 200, 180, 220, 250, 300])

# Running total
total = np.cumsum(daily)
print(total)   # [100 250 450 630 850 1100 1400]
```

**پس `cumsum` یعنی:** جمع تجمعی — هر عنصر، مجموع همه عناصر قبلی + خودش.

### با axis

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.cumsum(matrix, axis=0))   # per column
# [[1 2 3]
#  [5 7 9]]

print(np.cumsum(matrix, axis=1))   # per row
# [[1 3 6]
#  [4 9 15]]
```

## جدول خلاصه عملیات

| عملیات | نتیجه | View/Copy |
|---|---|---|
| `a + b` | element-wise | — |
| `np.sqrt(arr)` | ufunc | Copy |
| `arr + 10` | scalar broadcast | Copy |
| `matrix + row` | row broadcast | Copy |
| `data - mean(axis=0, keepdims=True)` | normalization | Copy |
| `arr[arr > 5]` | boolean mask | Copy |
| `np.sum(arr, axis=0)` | column sum | — |
| `np.cumsum(arr)` | running total | — |

## نکات کلیدی این فصل

1. عملیات NumPy همیشه element-wise است (مگر broadcasting).
2. [فارسی] ufuncs توابع ریاضی عنصر‌به‌عنصر هستند — بدون حلقه.
3. [فارسی] Vectorization سرعت ۲۰ تا ۵۰ برابر بیشتر از حلقه Python است.
4. [فارسی] Broadcasting گسترش خودکار آرایه‌های کوچک‌تر است — بدون کپی.
5. قوانین broadcasting از راست به چپ: اگر ابعاد یکسان یا یکی ۱ باشد، ممکن است.
6. [فارسی] `np.newaxis` یک بُعد اضافه می‌کند — برای ماتریس فاصله و outer product.
7. [فارسی] `axis` یعنی "کدام بُعد را حذف کن."
8. [فارسی] `keepdims=True` ابعاد را حفظ می‌کند — برای broadcasting بعدی.
9. [فارسی] `np.nan*` functions داده‌های گمشده را نادیده می‌گیرند.
10. [فارسی] `cumsum` و `cumprod` عملیات تجمعی هستند.

## تمرین‌ها

| شماره | عنوان | فایل |
|---|---|---|
| ۰۱ | عملیات ریاضی | `exercise_01.py` |
| ۰۲ | ufuncs | `exercise_02.py` |
| ۰۳ | Broadcasting پایه | `exercise_03.py` |
| ۰۴ | Broadcasting پیشرفته | `exercise_04.py` |
| ۰۵ | Aggregations | `exercise_05.py` |
| ۰۶ | Aggregation + Broadcasting + NaN | `exercise_06.py` |

## پرسش و پاسخ (Q&A)

### سوال: چرا `a * b` (دو بردار shape یکسان) element-wise است، نه outer product؟
**پاسخ:** وقتی shapeها یکسان باشند، NumPy عنصر‌به‌عنصر عمل می‌کند. برای outer product باید یک بردار را با `a[:, np.newaxis]` به شکل ستونی تبدیل کنی.

### سوال: `np.newaxis` چه می‌کند؟
**پاسخ:** یک بُعد جدید با اندازه ۱ اضافه می‌کند. `a[:, np.newaxis]` بردار `(3,)` را به `(3, 1)` تبدیل می‌کند و `a[np.newaxis, :]` به `(1, 3)`. این بُعد اضافه broadcasting بین دو بردار را ممکن می‌کند.

### سوال: تفاوت `axis=0` و `axis=1` چیست؟
**پاسخ:** `axis=0` بُعد اول (سطرها) را حذف می‌کند — نتیجه جمع ستون‌ها. `axis=1` بُعد دوم (ستون‌ها) را حذف می‌کند — نتیجه جمع سطرها.

### سوال: `keepdims` چه کاربردی دارد؟
**پاسخ:** ابعاد حذف‌شده را با اندازه ۱ حفظ می‌کند. برای عملیاتی مثل نرمال‌سازی که نیاز به broadcasting بین نتیجه تجمیع و آرایه اصلی داری، لازم است. مثال: `matrix - np.mean(matrix, axis=0, keepdims=True)`.

### سوال: چرا `NaN == NaN` همیشه False است؟
**پاسخ:** طبق استاندارد IEEE 754، NaN یعنی "عدد نامعتبر" — نمی‌توان دو مقدار نامعتبر را با هم مقایسه کرد. برای بررسی از `np.isnan()` استفاده کن.

### سوال: `cumsum` چه کاربردی دارد؟
**پاسخ:** جمع تجمعی. هر عنصر، مجموع همه عناصر قبلی + خودش. برای محاسبه running total در سری زمانی (مثل مصرف تجمعی برق) کاربرد دارد.

### سوال: Broadcasting چه زمانی خطا می‌دهد؟
**پاسخ:** وقتی در یک بُعد، نه اندازه‌ها یکسان باشند و نه یکی از آن‌ها ۱ باشد. مثال: `(4,) + (3,)` خطا می‌دهد.