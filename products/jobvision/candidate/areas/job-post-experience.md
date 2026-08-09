---
id: jobvision.candidate.job-post-experience
kind: product-area
group: jobvision
product: candidate
title: جزئیات و ارزیابی آگهی
summary: توضیح می‌دهد کارجو چگونه یک Job Post مشخص را می‌فهمد و ارزیابی می‌کند، از اطلاعات و actionهای پشتیبان استفاده می‌کند و تصمیم می‌گیرد آن را ذخیره، share یا برای apply شروع کند.
status: draft
owner: تیم محصول کارجو
last_reviewed:
related:
  - jobvision.candidate.overview
  - shared.job-post
  - jobvision.candidate.job-search
  - jobvision.candidate.recommended-jobs
  - jobvision.candidate.application-management
  - jobvision.employer.job-post-management
topics:
  - job-post
  - job-discovery
  - save-job
  - share-job
  - apply
  - candidate
---

# جزئیات و ارزیابی آگهی

## نمای کلی

جزئیات و ارزیابی آگهی Product Area سمت کارجو برای فهمیدن و ارزیابی یک فرصت شغلی مشخص و تصمیم‌گیری درباره ذخیره، share یا شروع apply است.

این draft شامل evidence مشاهده‌شده برای ذخیره کردن Job Post و بازبینی آن از مسیر Saved Jobs است. رفتار کامل جزئیات، ارزیابی، share، report و apply هنوز کامل نیست.

## رابطه با مفهوم shared Job Post

`shared.job-post` مالک تعریف، attributeهای shared، relationshipها و lifecycle مشترک Job Post بین محصولات Candidate و Employer است.

این Product Area مالک outcomeها، presentation، permissionها، stateها و flowهای Candidate-specific برای فهمیدن و ارزیابی یک Job Post است. actionهایی مثل save، share، report یا شروع application ممکن است در این Area ظاهر شوند، اما submission کامل و journeyهای بعد از submission در Product Areaهای جداگانه کارجو مستند می‌شوند.

ساخت، انتشار، ویرایش و مدیریت سمت Employer در `jobvision.employer.job-post-management` باقی می‌ماند.

## چرا این Area وجود دارد

- کمک به کارجو برای فهمیدن یک فرصت شغلی
- نمایش اطلاعات لازم برای ارزیابی relevance و fit
- فراهم کردن actionهایی مثل ذخیره، share و apply
- اتصال discovery آگهی به journey درخواست شغلی

## کاربران و نقش‌ها

- کارجو یا jobseeker که یک Job Post را می‌بیند
- کارجوی واردشده که از actionهای شخصی‌سازی‌شده یا application-related استفاده می‌کند
- بازدیدکننده واردنشده، در صورتی که Job Post عمومی قابل مشاهده باشد

تفاوت‌های authentication و permission نیاز به بررسی دارد.

## خروجی‌های کاربر

- فهمیدن نقش، کارفرما، نیازمندی‌ها و context فرصت شغلی
- تصمیم‌گیری درباره مرتبط بودن فرصت
- ذخیره یا share کردن Job Post در صورت نیاز
- apply کردن در صورت eligibility و تمایل
- فهمیدن اتفاقات بعد از apply

## نقاط ورود

نقاط ورود مشاهده‌شده یا محتمل:

- نتایج جستجوی شغل
- شغل‌های پیشنهادی
- آگهی‌های ذخیره‌شده
- لینک‌های share شده یا external
- history درخواست‌ها
- notification یا campaign

فهرست کامل entryها و رفتار deep linkها نیاز به review دارد.

## مفاهیم اصلی

### Job Post

فرصت شغلی shared که در `shared.job-post` تعریف می‌شود.

### Action سمت کارجو

actionهایی مثل ذخیره، share یا apply که به تجربه کارجو مربوط‌اند.

### Application

ارسال یا اعلام علاقه کارجو برای یک Job Post. مفهوم کامل Application در `shared.application` و Product Areaهای مرتبط مستند می‌شود.

### Saved Job

Job Postی که کارجو برای بازبینی بعدی ذخیره کرده است. Saved Job از Saved Search جداست.

## جریان‌های اصلی

### مشاهده و فهم Job Post

1. کارجو یک Job Post را باز می‌کند.
2. محصول اطلاعات فرصت و کارفرما را نشان می‌دهد.
3. کارجو نیازمندی‌ها، context و actionهای موجود را بررسی می‌کند.
4. کارجو تصمیم می‌گیرد خارج شود، ذخیره کند، share کند یا apply را شروع کند.

hierarchy دقیق اطلاعات و فیلدهای required هنوز مستند نشده است.

### ذخیره کردن Job Post

1. کارجوی واردشده کنترل bookmark را روی کارت یا جزئیات Job Post فعال می‌کند.
2. کنترل از حالت bookmark خالی به bookmark پر تغییر می‌کند.
3. Job Post در مقصد Saved Jobs نمایش داده می‌شود.
4. آیتم ذخیره‌شده بعد از refresh همان مقصد در همان session همچنان دیده شد.

وقتی هیچ آیتم ذخیره‌شده‌ای وجود ندارد، Saved Jobs collection را توضیح می‌دهد و کارجو را به کنترل save روی Job Post راهنمایی می‌کند. Saved Jobs از Saved Searches جداست و در navigation فعالیت‌های کارجو قرار دارد. حذف، action تکراری، persistence بلندمدت، failure recovery و رفتار Job Post ناموجود هنوز نیاز به بررسی دارد.

### Share کردن Job Post

1. کارجو action Share را انتخاب می‌کند.
2. محصول یک یا چند روش share را ارائه می‌کند.
3. لینک share شده باید در صورت در دسترس بودن، به همان Job Post resolve شود.

روش‌های دقیق share و رفتار لینک ناموجود هنوز نامشخص است.

### شروع apply روی Job Post

1. کارجوی واردشده action «ارسال رزومه» را انتخاب می‌کند.
2. محصول eligibility، authentication و readiness رزومه را بررسی می‌کند.
3. در walkthrough WT-2026-002، رزومه‌ای با completion کلی ۶۵٪ به gate «رزومه شما تکمیل نیست!» رسید و application ایجاد نشد.
4. کارجو می‌تواند flow تکمیل رزومه را شروع کند یا آن را ببندد؛ نتیجه submission و مسیر upload شخصی تست نشده‌اند.
5. در صورت رفع شرط‌ها، محصول باید نتیجه apply را اعلام کند؛ رفتار موفقیت در این walkthrough مشاهده نشد.

جزئیات gate و recovery در Product Area مدیریت درخواست‌ها و مدیریت رزومه مستند می‌شود.

## قواعد

- رفتار Candidate-side Job Post باید از مفهوم shared Job Post استفاده کند و مالک قواعد مدیریت Employer نباشد.
- apply یک ارتباط بین Candidate و تجربه recruiting سمت Employer ایجاد می‌کند.
- در session مشاهده‌شده، action Apply روی Job Post به gate readiness رزومه منتقل شد و پیش از ایجاد application متوقف شد.
- قواعد authentication، eligibility و application-state باید هنگام مستند شدن صریح بمانند.
- در context مشاهده‌شده برای کارجوی واردشده، save کردن Job Post آن را به Saved Jobs اضافه می‌کند و در refresh همان session باقی می‌ماند.
- Saved Jobs و Saved Searches دو مقصد و مفهوم جدا هستند.

قواعد visibility، save، share، application و personalization نیاز به owner review دارند.

## دسترسی‌ها

تفاوت‌های permission محتمل:

- مشاهده عمومی در برابر مشاهده authenticated
- ذخیره یا apply در حالت کاربر واردنشده
- apply با رزومه ناقص یا ناموجود
- مشاهده insightهای شخصی‌سازی‌شده یا premium

هیچ‌کدام از این تفاوت‌ها هنوز کامل مستند نشده‌اند.

## وضعیت‌ها و گذارها

تجربه کارجو ممکن است stateهای زیر را نمایش دهد:

- قابل مشاهده
- ذخیره‌شده یا ذخیره‌نشده
- eligible یا blocked برای apply
- apply نشده، در حال apply، applied یا previously applied
- Job Post ناموجود، closed یا expired

نام دقیق stateها و گذارها باید با `shared.job-post` و مستندات Application هماهنگ شود.

گذار save مشاهده‌شده:

```text
ذخیره‌نشده (bookmark خالی)
-> Save
-> ذخیره‌شده (bookmark پر و آیتم در Saved Jobs)
```

گذار معکوس هنوز تست نشده است.

## اعتبارسنجی‌ها

حوزه‌های validation محتمل که evidence لازم دارند:

- authentication
- آمادگی profile یا resume کارجو
- availability آگهی
- application تکراری
- سؤال‌ها یا اطلاعات required برای application
- eligibility یا محدودیت‌های حساب

## حالت‌های مرزی

- ناموجود شدن Job Post هنگام باز بودن صفحه
- باز کردن لینک قدیمی یا share شده
- قبلاً apply کرده بودن کارجو
- تکرار action save یا apply
- interrupt شدن flow توسط authentication
- ناقص بودن resume یا profile
- failure بعد از پیشرفت partial در application
- ناموجود یا uncertain بودن insightهای premium یا AI

## Product Areaهای مرتبط

- Job Search
- Application Management
- Resume Management
- Premium Insights
- Employer Job Post Management

## Variationهای شناخته‌شده

- وضعیت authentication ممکن است actionهای موجود را تغییر دهد.
- insightهای premium یا AI-powered ممکن است رفتار product-specific اضافه کنند.
- presentation در mobile و desktop ممکن است متفاوت باشد.

## Unknownها و رفتارهای تست‌نشده

- hierarchy اطلاعات canonical
- رفتار دقیق save و share
- رفتار حذف و save تکراری
- persistence در sessionهای بعدی، deviceهای دیگر و loginهای بعدی
- failure و recovery در save یا removal
- Job Postهای closed، expired، deleted یا unavailable در Saved Jobs
- authentication gateها
- eligibility و داده‌های required برای application
- رابطه با resume/profile
- تعریف universal eligibility و completion رزومه برای apply
- نتیجه apply موفق و رفتار مسیر upload رزومه شخصی
- analytics و instrumentation
- accessibility و keyboard behavior

## منابع

- `products/jobvision/candidate/overview.md`
- `products/jobvision/overview.md`
- `shared/product-concepts/job-post.md`
- `product-walkthrough/walkthroughs/products/jobvision/candidate/WT-2026-005/evidence.md` (برای reconciliation prototype به‌عنوان accepted در نظر گرفته شده است)
- برای تکمیل review، evidenceهای production، Jira، Figma، analytics و research بیشتری لازم است.

- `product-walkthrough/walkthroughs/products/jobvision/candidate/WT-2026-002/evidence.md` (claimهای E-001 تا E-010 توسط Product Owner پذیرفته شده‌اند)
