# ۰۱ - مبانی NumPy و ساخت آرایه

## این فصل چیست؟

[فارسی] `NumPy` کتابخانه اصلی محاسبات عددی در پایتون است. این فصل پایه‌ی کل فاز ۲ است — بدون درک NumPy، استفاده از Pandas و Matplotlib هم ممکن نیست.

مفاهیم این فصل: چرا NumPy؟ ndarray چیست؟ ساخت آرایه. ویژگی‌های آرایه. تغییر نوع. reshape. View vs Copy.

## ۱. چرا NumPy؟

لیست پایتون برای محاسبات عددی کند است. یک لیست، آرایه‌ای از اشاره‌گرها به اشیاء پراکنده در حافظه است. NumPy آرایه‌ای از اعداد خام در یک بلوک پیوسته حافظه می‌سازد.

| ویژگی | لیست پایتون | NumPy array |
|---|---|---|
| نوع عناصر | می‌تواند متفاوت باشد | همه یک نوع |
| حافظه | اشاره‌گر به اشیاء | بلوک پیوسته |
| سرعت عملیات | کند (حلقه Python) | سریع (پیاده‌سازی C) |

### [فارسی] Vectorization چیست؟

عملیات روی کل آرایه بدون حلقه. NumPy در پشت صحنه یک حلقه C سریع اجرا می‌کند.

```python
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

py_list * 2    # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] — repeats!
np_array * 2   # [2 4 6 8 10] — element-wise!
```

### [فارسی] ndarray چیست؟

[فارسی] `ndarray` مخفف N-dimensional array است. یک بلوک پیوسته حافظه از اعداد هم‌نوع. پایه‌ی کل NumPy.

**مقایسه با C++:**

| C++ | NumPy |
|---|---|
| `std::vector<int>` | `np.array([...], dtype=np.int64)` |
| `vec.size()` | `arr.size` |
| `vec[i]` | `arr[i]` |

## ۲. ساخت آرایه

| تابع | کاربرد | مثال | نتیجه |
|---|---|---|---|
| `np.array([...])` | از لیست | `np.array([1,2,3])` | `[1 2 3]` |
| `np.zeros(n)` | n صفر | `np.zeros(3)` | `[0. 0. 0.]` |
| `np.ones(n)` | n یک | `np.ones(3)` | `[1. 1. 1.]` |
| `np.full(n, v)` | n تا v | `np.full(3, 7)` | `[7 7 7]` |
| `np.eye(n)` | ماتریس همانی | `np.eye(3)` | `[[1. 0. 0.] ...]` |
| `np.arange(a, b, step)` | مثل range | `np.arange(0, 10, 2)` | `[0 2 4 6 8]` |
| `np.linspace(a, b, n)` | n عدد یکنواخت | `np.linspace(0, 1, 5)` | `[0. 0.25 0.5 0.75 1.]` |

```python
zeros = np.zeros(5)              # [0. 0. 0. 0. 0.]
ones = np.ones(5)                # [1. 1. 1. 1. 1.]
full = np.full(5, 7)             # [7 7 7 7 7]
identity = np.eye(3)             # Identity matrix
range_arr = np.arange(0, 10, 2)  # [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)  # [0. 0.25 0.5 0.75 1.]

np.random.seed(42)
random_uniform = np.random.rand(3)          # uniform [0, 1)
random_int = np.random.randint(0, 10, 5)    # random integers
```

**نکته:** `np.random.seed(42)` اعداد تصادفی را در هر اجرا یکسان می‌کند — برای تست و تکرارپذیری.

## ۳. ویژگی‌های آرایه

| ویژگی | معنی | برای `[[1,2,3],[4,5,6]]` |
|---|---|---|
| `shape` | ابعاد (tuple) | `(2, 3)` |
| `ndim` | تعداد ابعاد | `2` |
| `size` | تعداد کل عناصر | `6` |
| `dtype` | نوع داده | `int64` |
| `itemsize` | بایت هر عنصر | `8` |
| `nbytes` | کل بایت‌ها | `48` |

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.shape)     # (2, 3)
print(arr_2d.ndim)      # 2
print(arr_2d.size)      # 6
print(arr_2d.dtype)     # int64
print(arr_2d.itemsize)  # 8
print(arr_2d.nbytes)    # 48
```

## ۴. تغییر نوع — astype

[فارسی] `astype` نوع داده آرایه را تغییر می‌دهد. یک کپی جدید می‌سازد (نه view).

- تبدیل float به int، قسمت اعشاری را حذف می‌کند (truncate).
- تبدیل به نوع کوچکتر می‌تواند سرریز (overflow) کند.

```python
arr = np.array([1, 2, 3, 4, 5])
arr_float = arr.astype(np.float64)   # int64 → float64

arr_big = np.array([300, 400, 500])
arr_int8 = arr_big.astype(np.int8)   # overflow!

floats = np.array([1.7, 2.3, 3.9])
ints = floats.astype(np.int32)       # [1 2 3] — truncated
```

**مقایسه با C++:**
```cpp
int x = 300;
int8_t y = static_cast<int8_t>(x);  // Same overflow behavior
```

## ۵. مقدمه reshape

[فارسی] `reshape` ابعاد آرایه را بدون تغییر داده‌ها عوض می‌کند. تعداد کل عناصر باید ثابت بماند.

```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)   # 3 rows, 4 columns
auto = arr.reshape(2, -1)    # -1 = auto-calculate
flat = matrix.reshape(-1)    # flatten to 1D
```

**نکته:** `reshape` یک view برمی‌گرداند (نه کپی). عمیقش در فصل ۰۷.

## ۶. View vs Copy — معرفی مفهومی

- [فارسی] **View:** آرایه جدید، همون داده. تغییر در یکی، روی دیگری اثر می‌گذارد.
- [فارسی] **Copy:** داده جدا. تغییر در یکی، روی دیگری اثر نمی‌گذارد.

```python
arr = np.array([1, 2, 3, 4, 5])

view = arr[1:4]        # View — shares data
view[0] = 99
print(arr)             # [1, 99, 3, 4, 5]

copy = arr[1:4].copy()  # Copy — separate data
copy[0] = 77
print(arr)             # [1, 99, 3, 4, 5] — unchanged
```

**مقایسه با C++:**
- View مثل `std::span` (اشاره به داده، بدون مالکیت).
- Copy مثل `std::vector` جدید (داده مستقل).

**عمیقش در فصل ۰۷ (Views, Copies & Memory).**

## نکات کلیدی این فصل

1. [فارسی] NumPy معادل `std::vector` در C++ است، ولی با قابلیت‌های بسیار بیشتر.
2. [فارسی] `ndarray` یک بلوک پیوسته حافظه از اعداد هم‌نوع است.
3. [فارسی] Vectorization عملیات را بدون حلقه Python انجام می‌دهد.
4. [فارسی] `dtype` نوع داده عناصر را نشان می‌دهد؛ `itemsize` بایت هر عنصر.
5. [فارسی] `astype` یک کپی می‌سازد؛ ممکن است منجر به overflow یا truncate شود.
6. [فارسی] `reshape` ابعاد را عوض می‌کند — تعداد کل عناصر ثابت می‌ماند.
7. [فارسی] View داده مشترک دارد؛ Copy داده مستقل.
8. [فارسی] `reshape` و slicing به‌طور پیش‌فرض view برمی‌گردانند.

## تمرین‌ها

| شماره | عنوان | فایل |
|---|---|---|
| ۰۱ | ساخت آرایه‌های دلخواه | `exercise_01.py` |
| ۰۲ | تحلیل حافظه | `exercise_02.py` |
| ۰۳ | تبدیل نوع و سرریز | `exercise_03.py` |
| ۰۴ | reshape چند بعدی | `exercise_04.py` |
| ۰۵ | View vs Copy | `exercise_05.py` |

## پرسش و پاسخ (Q&A)

### سوال: View مثل `shared_ptr` است؟
**پاسخ:** از نظر اشتراک حافظه بله، ولی تفاوت کلیدی: `shared_ptr` مالکیت مشترک دارد (reference counting). View در NumPy مالکیت ندارد — فقط یک پنجره به حافظه اصلی است. معادل دقیق‌تر در C++، `std::span` است.

### سوال: Copy یک خانه حافظه جدید می‌سازد؟
**پاسخ:** بله. Copy یک بلوک حافظه جدید تخصیص می‌دهد و داده را کپی می‌کند. تغییر در copy روی آرایه اصلی اثر ندارد.

### سوال: چه عملیاتی view برمی‌گردانند و چه عملیاتی copy؟
**پاسخ:** slicing و `reshape` و `ravel` و `.T` → یک view.

**پاسخ:** `copy` و `astype` و boolean indexing و عملیات ریاضی → یک copy. عمیقش در فصل ۰۷.