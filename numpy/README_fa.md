# [فارسی] NumPy — برای Intelligent Systems

## هدف این بخش

بعد از NumPy لازم نیست NumPy Developer باشی. باید بتوانی:

> داده‌ی عددی را به شکل آرایه‌ای نمایش بدهی، ساختارش را بفهمی، قسمت موردنیازت را انتخاب کنی، روی آن محاسبه انجام دهی، فیلترش کنی و برای مرحله‌ی بعدی آماده کنی.

مثلاً اگر چنین داده‌ای داشته باشی:

```python
sensor_data = np.array([
    [23.4, 101.2, 45.1],
    [24.1, 100.8, 46.0],
    [25.7, 101.5, 44.3],
    [26.2, 102.1, 47.2],
])
```

باید بتوانی بفهمی: shape = `(4, 3)`, هر سطر یک measurement، هر ستون یک sensor feature. و بتوانی: دماها را بدهی، میانگین فشار را حساب کنی، نمونه‌های بالای ۲۵ درجه را پیدا کنی، داده را reshape کنی، offset به تمام اندازه‌گیری‌ها اضافه کنی.

## مسیر یادگیری

```
NumPy/
│
├── 01. Basics & Array Creation
│   ├── ndarray چیست؟
│   ├── توابع ساخت آرایه
│   ├── ویژگی‌ها (shape, ndim, size, dtype)
│   └── astype — تغییر نوع
│
├── 02. Indexing & Slicing
│   ├── Indexing (1D, 2D)
│   ├── Slicing
│   ├── Boolean Masking
│   ├── Fancy Indexing
│   └── np.where
│
├── 03. Operations & Broadcasting
│   ├── عملیات ریاضی element-wise
│   ├── ufuncs
│   ├── Broadcasting
│   ├── Aggregation (sum, mean, axis)
│   ├── keepdims
│   ├── Aggregation با شرط
│   ├── NaN handling
│   └── Cumulative (cumsum)
│
├── 04. Reshaping & Manipulation
│   ├── reshape, ravel, flatten
│   ├── transpose و .T
│   ├── Concatenate, stack, split
│   └── View vs Copy (عمیق)
│
└── 05. Random Module
    ├── توابع پایه (rand, randn, randint, uniform)
    ├── توزیع‌ها (normal, binomial, poisson)
    ├── Shuffle و Choice
    ├── Seed و تکرارپذیری
    └── کاربرد در ML
```

## [فارسی] Cheatsheet — مفاهیم کلیدی

### ساخت آرایه

| تابع | کاربرد |
|---|---|
| `np.array([...])` | از لیست |
| `np.zeros(n)` | n صفر |
| `np.ones(n)` | n یک |
| `np.full(n, v)` | n تا v |
| `np.arange(a, b, step)` | مثل range |
| `np.linspace(a, b, n)` | n عدد یکنواخت |
| `np.eye(n)` | ماتریس همانی |

### دسترسی و فیلتر

```python
arr[0]                    # 1D — عنصر اول
arr[1, 2]                 # 2D — سطر 1، ستون 2
arr[:, 0]                 # همه سطرها، ستون 0
arr[1:4]                  # برش
arr[::2]                  # گام ۲
arr[::-1]                 # معکوس

arr[arr > 5]              # فیلتر با شرط
arr[(arr > 3) & (arr < 8)]  # ترکیب شرط‌ها
arr[[0, 2, 4]]            # fancy indexing

np.where(arr > 5, 100, 0)   # انتخاب شرطی
np.where(arr > 5)            # یافتن ایندکس‌ها
```

### عملیات و Broadcasting

```python
arr + 10                  # scalar broadcast
matrix + row              # (4,) + (3, 4) → (3, 4)
matrix + col              # (3, 1) + (3, 4) → (3, 4)
a[:, np.newaxis] * b      # outer product

np.sqrt(arr)              # ufunc
np.exp(arr)
np.log(arr)
```

### [فارسی] Aggregation و axis

```python
np.sum(arr)
np.mean(arr)
np.std(arr)
np.min(arr) / np.max(arr)
np.argmin(arr) / np.argmax(arr)
np.median(arr)

np.sum(matrix, axis=0)              # per column
np.sum(matrix, axis=1)              # per row
np.mean(matrix, axis=1, keepdims=True)   # حفظ ابعاد
```

### [فارسی] Reshaping

```python
arr.reshape(3, 4)         # به شکل دلخواه
arr.reshape(2, -1)        # -1 = خودت حساب کن
arr.ravel()               # صاف کردن (view)
arr.flatten()             # صاف کردن (copy)
arr.T                     # transpose
arr.transpose(2, 0, 1)    # محور سفارشی
```

### [فارسی] Concatenate و Split

```python
np.concatenate([a, b], axis=0)
np.vstack([a, b])         # عمودی
np.hstack([a, b])         # افقی
np.stack([a, b])          # بُعد جدید

np.split(arr, 3)
np.vsplit(matrix, 2)
np.hsplit(matrix, 2)
```

### [فارسی] View vs Copy

| عملیات | نتیجه |
|---|---|
| Slicing, reshape, ravel, .T | **View** |
| copy, flatten, astype, عملیات ریاضی, boolean mask, fancy | **Copy** |

```python
arr.base is None    # True → owns data
arr[1:4].base       # not None → view
```

### [فارسی] Random

```python
np.random.rand(5)              # uniform [0, 1)
np.random.randn(5)             # standard normal
np.random.randint(1, 10, 5)    # اعداد صحیح
np.random.uniform(10, 20, 5)   # بازه دلخواه

np.random.normal(25, 3, 1000)  # توزیع نرمال
np.random.binomial(10, 0.5)    # پرتاب سکه
np.random.poisson(5)           # تعداد رویداد

np.random.shuffle(arr)         # قاطی کردن درجا
np.random.permutation(arr)     # کپی قاطی‌شده
np.random.choice(arr, size=5)  # نمونه‌گیری

np.random.seed(42)             # تکرارپذیری
np.random.default_rng(42)      # روش مدرن
```

## چه چیزی لازم نیست (فعلاً)

این‌ها در NumPy وجود دارند، ولی برای مسیر Intelligent Systems در این مرحله لازم نیستند:

- [فارسی] `strides`
- [فارسی] `C API`, `F2PY`
- [فارسی] `memory layout internals`
- [فارسی] `ufunc internals`
- [فارسی] `advanced performance optimization`
- [فارسی] `as_strided`
- [فارسی] NumPy internals

اگر روزی در Deep Learning یا CV به این‌ها برخوردی، همان‌جا یاد می‌گیری.

## معیار پایان NumPy

اگر بتوانی بدون نگاه کردن به جواب، این تمرین را حل کنی و بتوانی توضیح دهی: shape چیست، indexing چگونه کار می‌کند، axis چه کاربردی دارد، vectorization و broadcasting چه مسئله‌ای را حل می‌کنند، و چگونه داده را filter/reshape می‌کنیم — **NumPy برای تو تمام است.**

تمرین: `exercises/sensor_data.ipynb`

## کاربرد در Intelligent Systems

| مفهوم | کاربرد |
|---|---|
| Broadcasting | Attention در Transformer، Distance Matrix |
| reshape / transpose | Image processing (HWC → CHW)، Deep Learning |
| Random | Train/Test split، Mini-batch، Weight Init، Augmentation |
| Aggregation (axis, keepdims) | Loss functions، Batch Normalization |
| NaN handling | داده سنسور گمشده، پاکسازی داده |
| cumsum | سری زمانی، مصرف تجمعی |
| View vs Copy | بهینه‌سازی حافظه، جلوگیری از باگ‌های ناخواسته |

## ساختار پوشه

```
numpy/
├── 01_numpy_basics/
├── 02_indexing_slicing/
├── 03_operations_broadcasting/
├── 04_reshaping_manipulation/
├── 05_random_module/
├── exercises/
│   └── sensor_data.ipynb
├── README.md
└── README_fa.md
```