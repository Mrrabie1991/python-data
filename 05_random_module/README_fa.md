# ۰۵ - ماژول Random

## این فصل چیست؟

[فارسی] NumPy یک ماژول کامل برای تولید اعداد تصادفی داره. این فصل پایه‌ی تمام تکنیک‌های ML و Deep Learning است — train/test split، mini-batch، weight initialization، data augmentation، dropout. بدون Random، ML ممکن نیست.

## ۱. توابع پایه Random

### سناریو

می‌خواهی ۵ سنسور را با مقدار اولیه تصادفی راه‌اندازی کنی (کالیبراسیون). یا در ML، وزن‌های اولیه شبکه عصبی را تصادفی بگذاری.

### توابع

| تابع | خروجی | محدوده |
|---|---|---|
| `np.random.rand(n)` | n عدد اعشاری | [0, 1) — یکنواخت |
| `np.random.randn(n)` | n عدد اعشاری | توزیع نرمال استاندارد |
| `np.random.randint(low, high, n)` | n عدد صحیح | [low, high) |
| `np.random.uniform(low, high, n)` | n عدد اعشاری | [low, high) |

### کد

```python
import numpy as np

# Uniform [0, 1)
rand_arr = np.random.rand(5)

# Standard normal (mean=0, std=1)
randn_arr = np.random.randn(5)

# Integers
randint_arr = np.random.randint(1, 10, 5)

# Custom range
uniform_arr = np.random.uniform(10, 20, 5)

# Sensor calibration example
initial_offsets = np.random.uniform(-0.5, 0.5, 5)
```

## ۲. توزیع‌های احتمال

### مفهوم ساده

- **توزیع یکنواخت (Uniform):** همه اعداد شانس برابر. مثال: تاس.
- **توزیع نرمال (Normal):** بیشتر اعداد نزدیک میانگین، هرچه دورتر کمتر. مثال: قد مردم، دمای سنسور.
- **توزیع دوجمله‌ای (Binomial):** تعداد موفقیت در n آزمایش. مثال: پرتاب ۱۰ سکه، تعداد شیرها.
- **توزیع پواسون (Poisson):** تعداد رویداد در بازه زمانی. مثال: ایمیل‌های دریافتی در یک ساعت.

### کد

```python
import numpy as np

# Normal — mean=25, std=3
temps = np.random.normal(25, 3, 1000)
print(f"Mean: {temps.mean():.2f}")   # ≈ 25
print(f"Std:  {temps.std():.2f}")    # ≈ 3

# Uniform — 0 to 100
uniform = np.random.uniform(0, 100, 1000)
print(f"Mean: {uniform.mean():.2f}")   # ≈ 50

# Binomial — 10 flips, p=0.5
flips = np.random.binomial(10, 0.5, 1000)
print(f"Mean: {flips.mean():.2f}")   # ≈ 5

# Poisson — lambda=5
events = np.random.poisson(5, 1000)
print(f"Mean: {events.mean():.2f}")   # ≈ 5
```

### کاربرد در Intelligent Systems

- **نویز سنسور:** `np.random.normal(0, sensor_noise, n)` — شبیه‌سازی نویز.
- [فارسی] **Monte Carlo:** شبیه‌سازی هزاران سناریو.
- [فارسی] **Data Augmentation:** نویز تصادفی به تصاویر.

## ۳. [فارسی] Shuffle و Choice

### سناریو

- [فارسی]  **Shuffle:** قبل از آموزش مدل، داده‌ها را قاطی می‌کنی که مدل ترتیب یاد نگیرد.
- [فارسی]  **Choice:** انتخاب تصادفی نمونه از داده.

### توابع

| تابع | کار |
|---|---|
| `np.random.shuffle(arr)` | arr را **درجا** قاطی می‌کند (None برمی‌گرداند) |
| `np.random.permutation(arr)` | یک کپی قاطی‌شده برمی‌گرداند |
| `np.random.choice(arr, size, replace)` | نمونه تصادفی انتخاب می‌کند |

### کد

```python
import numpy as np

# shuffle — in-place
data = np.arange(10)
np.random.shuffle(data)

# permutation — copy
data = np.arange(10)
perm = np.random.permutation(data)

# choice — sample
sample = np.random.choice(np.arange(100), size=5, replace=False)

# Weighted choice
colors = np.array(["A", "B", "C"])
probs = [0.7, 0.2, 0.1]
choices = np.random.choice(colors, size=100, p=probs)
```

**نکته:** `shuffle` درجا کار می‌کند. برای نگه‌داشتن اصلی، از `permutation` استفاده کن.

## ۴. [فارسی] Random Seed — تکرارپذیری

### سناریو

می‌خواهی نتیجه آزمایشت **قابل بازتولید** باشد. هر بار که کد را اجرا می‌کنی، همان اعداد تصادفی تولید شوند.

### مفهوم

[فارسی] `np.random.seed(n)` یک نقطه شروع تعیین می‌کند. با همان seed، همیشه همان اعداد تولید می‌شوند.

### کد

```python
import numpy as np

# Without seed — different every run
print(np.random.rand(3))

# With seed — same every time
np.random.seed(42)
print(np.random.rand(3))

np.random.seed(42)
print(np.random.rand(3))   # same as above

# Modern API — recommended
rng = np.random.default_rng(seed=42)
print(rng.random(3))
```

**چرا مهم است؟**

- [فارسی] **Debugging:** بازتولید دقیق یک خطا.
- [فارسی] **Research:** دیگران می‌توانند نتایج را تأیید کنند.
- [فارسی] **Testing:** تست‌ها باید deterministic باشند.
- [فارسی] **Comparison:** مقایسه دو مدل روی همان data split.

## ۵. [فارسی] Random در ML

### سناریوهای واقعی

پنج کاربرد اصلی Random در ML:

1. [فارسی] **Train/Test Split:** جدا کردن داده آموزش و تست.
2. [فارسی] **Mini-batch Sampling:** انتخاب تصادفی نمونه‌ها در SGD.
3. [فارسی] **Weight Initialization:** مقدار اولیه وزن‌ها (He init).
4. [فارسی] **Data Augmentation:** تغییر تصادفی داده.
5. [فارسی] **Dropout:** خاموش کردن تصادفی neuronها.

### کد

```python
import numpy as np

# 1. Train/Test split
data = np.arange(100)
indices = np.random.permutation(len(data))
train_idx = indices[:80]
test_idx = indices[80:]

# 2. Mini-batch sampling
batch_size = 16
for i in range(0, len(train_idx), batch_size):
    batch = data[train_idx[i:i + batch_size]]
    # process batch

# 3. He initialization for neural networks
n_inputs, n_outputs = 100, 50
weights = np.random.randn(n_inputs, n_outputs) * np.sqrt(2.0 / n_inputs)

# 4. Data augmentation — add noise
signal = np.sin(np.linspace(0, 4*np.pi, 100))
noisy_signal = signal + np.random.normal(0, 0.1, 100)

# 5. Dropout — random mask
activations = np.random.rand(10)
dropout_mask = np.random.rand(10) > 0.3   # keep 70%
dropped = activations * dropout_mask
```

## نکات کلیدی این فصل

1. [فارسی] `np.random.rand` برای uniform [0, 1)، `randn` برای normal استاندارد.
2. [فارسی] `randint` برای اعداد صحیح، `uniform` برای بازه دلخواه.
3. توزیع‌ها: Normal (میانگین + انحراف)، Binomial (n + p)، Poisson (lambda).
4. [فارسی] `shuffle` درجا، `permutation` کپی، `choice` نمونه‌گیری.
5. [فارسی] `np.random.seed(n)` برای تکرارپذیری.
6. [فارسی] `default_rng(seed)` روش مدرن‌تر است.
7. [فارسی] Random پایه ML است — train/test, mini-batch, init, augmentation.

## تمرین‌ها

| شماره | عنوان | فایل |
|---|---|---|
| ۰۱ | Random Basics | `exercise_01.py` |
| ۰۲ | Distributions | `exercise_02.py` |
| ۰۳ | Shuffle & Choice | `exercise_03.py` |
| ۰۴ | Seed & Reproducibility | `exercise_04.py` |
| ۰۵ | Random for ML | `exercise_05.py` |

## پرسش و پاسخ (Q&A)

### سوال: فرق `rand` و `randn` چیست؟
**پاسخ:** `rand` اعداد یکنواخت در بازه [0, 1) تولید می‌کند. `randn` اعداد از توزیع نرمال استاندارد (میانگین 0، انحراف 1). برای شبیه‌سازی نویز، `randn` مناسب‌تر است.

### سوال: فرق `shuffle` و `permutation` چیست؟
**پاسخ:** `shuffle` آرایه را **درجا** قاطی می‌کند (بدون بازگشت). `permutation` یک کپی قاطی‌شده برمی‌گرداند. برای نگه‌داشتن آرایه اصلی، `permutation`.

### سوال: چرا `np.random.seed` مهم است؟
**پاسخ:** تکرارپذیری. برای debugging، مقایسه منصفانه مدل‌ها، و تست deterministic. با یک seed مشخص، همیشه نتایج یکسان.

### سوال: `default_rng` چه فرقی با `np.random.seed` دارد؟
**پاسخ:** `default_rng` روش مدرن (NumPy 1.17+) است و Generator object برمی‌گرداند. مزایا: جداسازی حالت‌ها، API بهتر. برای کد جدید، از `default_rng` استفاده کن.

### سوال: He initialization چیست؟
**پاسخ:** روش مقدارگذاری اولیه وزن‌های شبکه عصبی. `randn * sqrt(2 / n_inputs)` — انحراف استاندارد متناسب با تعداد ورودی‌ها. باعث آموزش بهتر می‌شود.