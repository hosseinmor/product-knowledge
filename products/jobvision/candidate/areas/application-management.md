---
id: jobvision.candidate.application-management
kind: product-area
group: jobvision
product: candidate
title: مدیریت درخواست‌ها
summary: توضیح می‌دهد کارجو چگونه درخواست‌های ارسال‌شده را می‌بیند، فیلتر، بررسی، ویرایش، اولویت‌بندی، withdraw و دنبال می‌کند.
status: draft
owner: تیم محصول کارجو
last_reviewed:
related:
  - jobvision.candidate.overview
  - shared.application
  - shared.job-post
  - shared.resume
  - jobvision.candidate.job-post-experience
  - jobvision.candidate.resume-management
topics:
  - application
  - application-status
  - withdrawal
  - my-priority
  - resume
  - candidate
---

# مدیریت درخواست‌ها

## نمای کلی

مدیریت درخواست‌ها Product Area سمت کارجو برای پیگیری و مدیریت applicationها بعد از apply روی Job Postها است.

این نسخه بر اساس evidence پذیرفته‌شده walkthroughها برای prototype فعلی نوشته شده است. این سند عمداً flow کامل submission، قواعد پردازش سمت Employer یا معنای canonical lifecycle را قطعی فرض نمی‌کند.

## چرا این Area وجود دارد

- کمک به کارجو برای فهمیدن اتفاقات بعد از apply
- امکان فیلتر و بررسی history درخواست‌ها
- نمایش activity کارفرما و پیشرفت status
- پشتیبانی از actionهای سمت کارجو مثل ویرایش رزومه ارسال‌شده یا withdrawal، در صورت دسترسی
- هم‌راستا نگه داشتن رفتار application سمت کارجو با مفهوم shared Application

## کاربران و نقش‌ها

- کارجوی واردشده با applicationهای ارسال‌شده
- کارجویی که status و activity کارفرما را بررسی می‌کند
- کارجویی که در صورت امکان actionهای بعد از submission انجام می‌دهد

کاربران Employer و workflowهای recruiter خارج از مالکیت این Product Area هستند.

## خروجی‌های کاربر

- مشاهده درخواست‌های ارسال‌شده
- فیلتر کردن درخواست‌ها بر اساس گروه status
- sort یا pagination روی history درخواست‌ها
- بررسی جزئیات یک application
- فهمیدن signalهای مشاهده کارفرما و activity کارفرما
- ویرایش اطلاعات رزومه ارسال‌شده در صورت مجاز بودن
- withdraw کردن application در صورت مجاز بودن
- فهمیدن وضعیت‌های rejected، withdrawn، closed و in-progress

## نقاط ورود

نقاط ورود مشاهده‌شده یا محتمل:

- مقصد درخواست‌های کارجو
- navigation حساب کارجو
- جزئیات Job Post بعد از apply
- لینک‌های status application
- notification یا campaign link

مجموعه کامل entryهای بعد از apply، email و mobile نیاز به review دارد.

## مفاهیم اصلی

### درخواست

ارسال یا اعلام علاقه کارجو برای یک Job Post که در سطح shared با `shared.application` تعریف می‌شود.

### وضعیت درخواست

status یا گروه status قابل مشاهده برای کارجو. فیلترهای مشاهده‌شده شامل همه، دریافت‌شده، بررسی اولیه، بررسی نهایی، ردشده، انصراف‌داده‌شده و بسته‌شده است.

### Signal مشاهده کارفرما

نشانه‌ای برای کارجو که می‌گوید کارفرما رزومه یا application ارسال‌شده را دیده است.

### Activity کارفرما

اطلاعات قابل مشاهده برای کارجو درباره آخرین activity کارفرما روی application. در walkthrough مشاهده‌شده این مفهوم از signal ساده مشاهده رزومه جدا بود.

### رزومه ارسال‌شده

اطلاعات رزومه‌ای که به application وصل یا با آن associated شده است. در جزئیات application مشاهده‌شده، کنترل ویرایش رزومه ارسال‌شده وجود داشت.

### My Priority

یک action یا قابلیت quota-limited مشاهده‌شده برای اولویت‌دادن به application. در حساب تست‌شده quota پنج استفاده در ۳۰ روز دیده شد، اما eligibility و اثر سمت Employer هنوز نامشخص است.

## جریان‌های اصلی

### مشاهده و فیلتر درخواست‌ها

1. کارجو مقصد applicationها را باز می‌کند.
2. محصول فهرست applicationهای ارسال‌شده را با اطلاعات خلاصه نشان می‌دهد.
3. کارجو بر اساس گروه status فیلتر می‌کند.
4. محصول فهرست و URL state را به‌روزرسانی می‌کند.
5. اگر application مطابق فیلتر وجود نداشته باشد، کارجو empty filtered state را می‌بیند.

خلاصه‌های مشاهده‌شده شامل Job Post، شرکت، status، زمان submission و در صورت وجود زمان مشاهده توسط کارفرما بود.

### مرتب‌سازی و صفحه‌بندی درخواست‌ها

1. کارجو گزینه sort را انتخاب می‌کند.
2. محصول فهرست applicationها را به‌روزرسانی می‌کند.
3. اگر نتایج بیشتر وجود داشته باشد، کارجو pagination انجام می‌دهد.

گزینه‌های sort مشاهده‌شده شامل تاریخ application و تاریخ تصمیم status بود. برای applicationهای closed، pagination مشاهده شد.

### بررسی جزئیات application

1. کارجو یک application را باز یا expand می‌کند.
2. محصول اطلاعاتی مثل آخرین activity کارفرما، introduction letter، رزومه ارسال‌شده و کنترل‌های موجود را نشان می‌دهد.
3. کارجو در صورت مجاز بودن می‌تواند رزومه ارسال‌شده را ویرایش یا application را withdraw کند.

hierarchy canonical جزئیات و مرزهای edit نیاز به review دارد.

### Withdraw کردن application

1. کارجو applicationی را باز می‌کند که withdrawal برای آن در دسترس است.
2. کارجو action withdraw را انتخاب می‌کند.
3. محصول بر اساس قواعد فعلی وضعیت را تغییر می‌دهد یا confirmation می‌خواهد.
4. در صورت موفقیت، application به‌عنوان withdrawn در نظر گرفته می‌شود.

محتوای FAQ مشاهده‌شده می‌گفت withdrawal قبل از دیده‌شدن رزومه توسط کارفرما در دسترس است. این مورد در این سند به‌عنوان claim قابل مشاهده در UI ثبت شده، نه enforcement تأییدشده backend.

### فهمیدن rejection یا راهنمای status

1. کارجو applicationی با statusهایی مثل rejected را می‌بیند.
2. محصول ممکن است context مثل مرحله یا مصاحبه را بپرسد.
3. FAQ یا help content معنای status و انتظار درباره feedback را توضیح می‌دهد.

FAQ مشاهده‌شده نشان می‌داد feedback ممکن است optional باشد؛ تعهدات canonical سمت Employer هنوز نیاز به review دارد.

## قواعد

- Candidate Application Management مالک tracking و کنترل‌های post-submission سمت کارجو است.
- `shared.application` مالک تعریف cross-product application است.
- در تجربه مشاهده‌شده، filter state درخواست‌ها در URL منعکس می‌شود.
- زمان مشاهده توسط کارفرما و آخرین activity کارفرما دو signal جدا در تجربه مشاهده‌شده هستند.
- فیلترهای status مشاهده‌شده شامل همه، دریافت‌شده، بررسی اولیه، بررسی نهایی، ردشده، انصراف‌داده‌شده و بسته‌شده است.
- قواعد withdrawal فراتر از claimهای UI تأیید نشده‌اند.
- رفتار My Priority مشاهده شده اما هنوز کامل فهمیده نشده است.

این قواعد evidence مربوط به prototype هستند و نیاز به review مالک محصول دارند.

## دسترسی‌ها

تفاوت‌های محتمل یا مشاهده‌شده:

- کارجو فقط applicationهای خودش را می‌بیند.
- ویرایش رزومه ارسال‌شده ممکن است به وضعیت application وابسته باشد.
- withdrawal ممکن است به employer view state یا application state وابسته باشد.
- My Priority ممکن است به quota، eligibility، وضعیت حساب یا plan وابسته باشد.
- دسترسی و واکنش سمت Employer خارج از این Product Area است.

## وضعیت‌ها و گذارها

گروه‌های status مشاهده‌شده:

```text
دریافت‌شده
بررسی اولیه
بررسی نهایی
ردشده
انصراف‌داده‌شده
بسته‌شده
```

گذارهای محتمل سمت کارجو:

```text
Applied
-> Received
-> Initial review یا Final review
-> Rejected، Closed یا final state دیگر
```

withdrawal به‌عنوان action سمت کارجو در صورت مجاز بودن دیده می‌شود:

```text
Application فعال
-> Withdraw
-> Withdrawn
```

نام canonical stateها، terminal stateها و triggerهای سمت Employer هنوز تأیید نشده‌اند.

## اعتبارسنجی‌ها

اعتبارسنجی‌های محتمل:

- مالکیت application توسط کارجو
- وضعیت application قبل از edit یا withdrawal
- در دسترس بودن رزومه قبل از ویرایش submitted resume
- quota و eligibility برای My Priority
- اطلاعات الزامی برای promptهای rejection-context
- معتبر بودن optionهای sort و filter

## حالت‌های مرزی

- نبود application
- نبود application در یک status فیلترشده
- دیده‌شدن قبلی رزومه توسط Employer
- بسته شدن Job Post بعد از application
- تلاش کارجو برای withdraw کردن application بسته یا rejected
- ویرایش رزومه بعد از activity کارفرما
- unavailable یا stale بودن activity کارفرما
- تمام شدن quota My Priority
- تغییر status application هنگام مشاهده جزئیات توسط کارجو

## Product Areaهای مرتبط

- Job Details & Evaluation
- Resume Management
- Job Search
- Recommended Jobs & Preferences

## Variationهای شناخته‌شده

- actionهای در دسترس ممکن است بر اساس status application فرق کنند.
- signalهای employer view و activity ممکن است برای همه applicationها نمایش داده نشوند.
- availability My Priority ممکن است بر اساس حساب یا quota فرق کند.
- متن status و FAQ ممکن است با release محصول تغییر کند.
- layoutهای mobile و desktop ممکن است متفاوت باشند.

## Unknownها و رفتارهای تست‌نشده

- lifecycle و تعریف canonical statusهای application
- flow کامل submission
- اینکه withdrawal بعد از دیده‌شدن رزومه توسط کارفرما واقعاً از نظر فنی block می‌شود یا نه
- محدودیت دقیق ویرایش submitted resume
- پیامدهای actionهای کارجو در سمت Employer
- eligibility، زمان reset و اثر Employer-side قابلیت My Priority
- رفتار notification برای تغییر status
- نیازمندی‌های feedback در rejection
- متن و actionهای empty state در همه statusها
- accessibility و رفتار keyboard

## منابع

- `product-walkthrough/walkthroughs/products/jobvision/candidate/WT-2026-006/evidence.md` (برای reconciliation prototype به‌عنوان accepted در نظر گرفته شده است)
