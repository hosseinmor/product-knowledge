---
id: content.context.jobvision-candidate
collection: content
type: content-context
title: JobVision Candidate Content Context
summary: Defines audience-specific terminology, tone, and claim boundaries for JobVision experiences addressed to jobseekers; product behavior remains external.
knowledge_state: unverified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.pattern.notifications
  - content.pattern.ai-content-and-disclosure
topics:
  - jobvision
  - candidate
  - jobseeker
  - terminology
  - tone
  - product-content
---

# Context محتوایی JobVision Candidate

این سند قواعد محتوایی مخصوص تجربهٔ کارجوی جاب‌ویژن را تعریف می‌کند. قرارداد
machine-readable در [`jobvision-candidate.yml`](jobvision-candidate.yml) و
regression caseها در
[`../evals/jobvision-candidate-context-cases.yml`](../evals/jobvision-candidate-context-cases.yml)
قرار دارند.

> **Source boundary:** این Context منبع Product Knowledge نیست. هر ادعای رفتار
> محصول باید همان زمان از <https://docs-jv.jvoffice.ir/> و دامنهٔ مرتبط بررسی
> شود. بخش‌های رفتاری قدیمی این سند تا revalidation نباید به‌عنوان حقیقت محصول
> استفاده شوند.

## این Context چه چیزی را مالک است؟

```text
Shared Content
→ معنی اصطلاح، صدای پایه، localization، pattern و component contract

Candidate Context
→ preferred label و محدودیت ادعا برای مخاطب کارجو

Candidate Product Area
→ رفتار، state، eligibility، permission، consequence و flow
```

این Context برای نوشتن یا ارزیابی copy سمت کارجو استفاده می‌شود؛ از صفحهٔ
جست‌وجو و آگهی تا رزومه، درخواست‌های شغلی و پیشنهادها. این سند دربارهٔ رفتار
سمت Employer یا Cando ATS تصمیم نمی‌گیرد.

## مرز منابع

### قواعد source-derived

- مخاطب محصول Candidate «کارجو» است و با «شما» خطاب می‌شود.
- آگهی شغلی، موقعیت شغلی و فرصت شغلی conceptهای متمایزند.
- در تجربهٔ Candidate، سازمان استخدام‌کننده با label «شرکت» نمایش داده می‌شود؛
  «کارفرما» نقش انسانی است.
- entity درخواست با «درخواست شغلی» و action آن با «ارسال رزومه» نامیده می‌شود.
- رزومه یک concept است و رزومهٔ فارسی و انگلیسی variantهای زبانی آن هستند.
- «دستیار هوشمند رزومه» نمونهٔ مشخص دستیار هوشمند است؛ هر قابلیت AI دستیار
  نیست.

### قواعد عملیاتی این Context

- صورت کامل اصطلاح در پیام مستقل، اعلان و سطح چنددامنه‌ای استفاده می‌شود.
- متن recommendation احتمال یا ارتباط را توضیح می‌دهد و استخدام را تضمین
  نمی‌کند.
- activity قابل مشاهدهٔ کارفرما از outcome استخدامی جدا نوشته می‌شود.
- observationهای prototype، threshold و quota به policy عمومی تبدیل نمی‌شوند.

### خارج از مالکیت

- lifecycle و نام canonical وضعیت‌های درخواست شغلی؛
- eligibility ارسال درخواست، تکمیل رزومه یا استفاده از قابلیت‌ها؛
- منطق ranking و دلیل recommendation؛
- permission و visibility واقعی کارفرما؛
- اثر action کارجو در Employer یا ATS؛
- سیاست زبان، رقم، تقویم، timezone و formatter runtime.

این موارد باید از Product Area یا implementation source معتبر بیایند.

## مخاطب و خطاب

نام نقش مخاطب `کارجو` است. `کاندیدا` به Cando ATS تعلق دارد و `متقاضی` یا
`داوطلب` preferred این سطح نیستند.

در copy مستقیم از `شما` استفاده کنید:

```text
رزومهٔ شما ذخیره شد.
می‌توانید این آگهی شغلی را برای بعد ذخیره کنید.
```

از خطاب تزئینی یا تکرار نقش خودداری کنید:

```text
کارجوی عزیز، رزومه‌تان با موفقیت هرچه تمام‌تر ثبت شد!  ← نامناسب
```

نقش «کارجو» را فقط وقتی نام ببرید که تمایز نقش برای فهم محتوا لازم است.

## مدل اصطلاحات

### آگهی، موقعیت و فرصت

| Concept | label در Candidate | کاربرد |
|---|---|---|
| `job_post` | آگهی شغلی | listing منتشرشده، metadata، ذخیره و مشاهده |
| `job_position` | موقعیت شغلی | خود نقش یا جایگاه واقعی |
| `job_opportunity` | فرصت شغلی | discovery، recommendation و copy عمومی |

```text
این آگهی شغلی ۳ روز پیش منتشر شده است.
برای این موقعیت شغلی رزومه ارسال کنید.
فرصت‌های شغلی پیشنهادی شما
```

این سه عبارت synonym نیستند. برای کوتاه‌شدن متن، entity دقیق را «فرصت» یا
«موقعیت» ننامید.

### شرکت و کارفرما

در تجربهٔ Candidate:

- entity سازمان استخدام‌کننده → `شرکت`؛
- فرد یا نقش انسانی طرف فرایند جذب → `کارفرما`.

```text
صفحهٔ شرکت
آگهی‌های شغلی این شرکت
کارفرما رزومهٔ شما را مشاهده کرده است.
```

«کارفرما» را نام شرکت، حساب سازمان یا entity مالک آگهی فرض نکنید. «سازمان» در
متن رسمی حقوقی یا concept چندمحصولی ممکن است لازم شود، اما تغییر label باید از
همان context و Product Area بیاید.

### درخواست شغلی

```text
Entity در متن مستقل        → درخواست شغلی
Entity در صفحهٔ روشن        → درخواست
Action                      → ارسال رزومه
```

`ارسال رزومه` نام عمل است، نه نام record. `اپلای`، `تقاضا` و صورت کوتاه
`درخواست` در notification یا متن مستقل label entity نیستند.

```text
درخواست شغلی شما ارسال شد.
مشاهدهٔ درخواست
ارسال رزومه
```

نام و معنی وضعیت‌ها باید از Product Area بیاید. copy نباید stage داخلی ATS یا
نتیجهٔ استخدام را از یک signal سادهٔ مشاهده استنتاج کند.

### رزومه

نام preferred، `رزومه` است؛ نه `CV`، `سی‌وی` یا `پروفایل کاری`.

رزومهٔ فارسی و رزومهٔ انگلیسی دو بازنمایی زبانی همان concept هستند. copy نباید
به کارجو بگوید «دو رزومه دارید» مگر product truth واقعاً entityهای جداگانه را
تعریف کند.

`رزومهٔ شخصی` فایل بارگذاری‌شدهٔ کارجو است و از رزومهٔ ساختاریافتهٔ جاب‌ویژن
متمایز می‌ماند. رفتار upload، fallback و استفاده در درخواست هنوز Product Area
و runtime-owned است.

### جذب و استخدام

`جذب` فرایند پیدا کردن و ارزیابی افراد است؛ `استخدام` outcome آن فرایند است.
در Candidate copy این دو را synonym نکنید:

```text
فرایند جذب شرکت
شانس استخدام
تاریخ استخدام
```

هیچ recommendation، مشاهدهٔ رزومه یا پیشرفت وضعیت به‌تنهایی تضمین استخدام نیست.

### هوش مصنوعی و دستیار هوشمند

- technology یا capability عمومی → `هوش مصنوعی`؛
- تجربهٔ مستقل assistant-like → `دستیار هوشمند`؛
- تجربهٔ تأییدشدهٔ رزومه → عنوان کامل `دستیار هوشمند ارزیابی و بهبود رزومه`
  و در context روشن `دستیار هوشمند رزومه`.

یک امتیاز، پیشنهاد یا automation را فقط برای جذاب‌ترشدن copy «دستیار هوشمند»
ننامید. نتیجه، محدودیت و نیاز به review باید از pattern محتوای AI بیاید.

## لحن Candidate

صدای پایه همان فارسی معیار نوشتاری جاب‌ویژن است. Candidate Context آن را با
این محدودیت‌ها تنظیم می‌کند:

- در discovery و empty state می‌توان گرم و تشویق‌کننده بود؛
- در submission، error، status و eligibility وضوح بر انگیزش مقدم است؛
- دربارهٔ fit، شانس، زمان استخدام یا اقدام کارفرما وعده ندهید؛
- کمبود اطلاعات کارجو را سرزنش یا به شکست شخصی تبدیل نکنید؛
- موفقیت فقط بعد از تأیید outcome نوشته شود.

```text
می‌توانید با تکمیل سوابق کاری، اطلاعات بیشتری به کارفرما نشان دهید.  ← مناسب
رزومه‌تان ضعیف است؛ حتماً کاملش کنید تا استخدام شوید.                ← نامناسب
```

## ادعاها و stateها

Candidate Product Areaها هنوز draft هستند. بنابراین:

- threshold مشاهده‌شدهٔ تکمیل رزومه policy عمومی نیست؛
- quota مشاهده‌شدهٔ My Priority برای همهٔ کاربران تضمین نمی‌شود؛
- مشاهدهٔ رزومه با پذیرش، پیشرفت یا استخدام یکی نیست؛
- employer preview تضمین نمی‌کند view واقعی Employer دقیقاً همان باشد؛
- recommendation دلیل قطعی fit یا outcome نیست؛
- stateهای Employer یا ATS بدون mapping تأییدشده به کارجو نمایش داده نمی‌شوند.

متن باید کمترین ادعای کافی را بسازد:

```text
کارفرما رزومهٔ شما را مشاهده کرده است.  ← signal مشاهده‌شده
درخواست شما پذیرفته شد.                  ← فقط با outcome تأییدشده
```

## Routing به Product Area

| موضوع copy | منبع رفتار |
|---|---|
| جست‌وجو، فیلتر، جست‌وجوی ذخیره‌شده | دامنهٔ «جست‌وجوی شغل» در سایت داخلی |
| جزئیات، ذخیره، share یا شروع apply | دامنهٔ «آگهی» در سایت داخلی |
| پیشنهادها و ترجیحات | دامنهٔ مرتبط در سایت داخلی؛ اگر مستند نیست unknown |
| submission، وضعیت، activity و انصراف | دامنهٔ «درخواست شغلی» در سایت داخلی |
| ساخت، تکمیل، preview و AI رزومه | دامنهٔ «رزومه» در سایت داخلی |

برای action، eligibility، state، مقدار یا consequence همیشه Area مربوط را load
کنید. اگر Area پاسخ قطعی ندارد، unknown را حفظ کنید.

## Pattern، Component و Localization

Context جای pattern یا component contract را نمی‌گیرد:

- پیام خطا از Error pattern می‌آید؛
- feedback از Notification pattern و contract می‌آید؛
- CTA از Button contract می‌آید؛
- field copy از Text Input contract می‌آید؛
- disclosure قابلیت AI از AI Content pattern می‌آید.

عدد، درصد، تاریخ، نام شرکت، عنوان آگهی و identifierهای runtime نیز باید طبق
Localization format و isolate شوند. Candidate Context رقم، تقویم یا timezone
تازه‌ای تعریف نمی‌کند.

## قرارداد قطعی

### باید

- اصطلاح preferred سمت کارجو را برای concept درست انتخاب کنید.
- پیام مستقل را با صورت کامل و بدون اتکا به context پنهان بنویسید.
- activity، recommendation و progress را فقط در حد evidence توصیف کنید.
- برای رفتار و state، Product Area مالک را load کنید.
- pattern، component و localization مشترک را حفظ کنید.

### نباید

- «کاندیدا»، «متقاضی» یا اصطلاح ATS را جای «کارجو» استفاده کنید.
- شرکت را «کارفرما» یا آگهی شغلی را «موقعیت/فرصت» بنامید.
- action «ارسال رزومه» را نام entity درخواست شغلی قرار دهید.
- قابلیت AI عمومی را بدون تجربهٔ assistant-like «دستیار هوشمند» بنامید.
- threshold، quota، شانس استخدام یا اثر سمت Employer را از observation حدس
  بزنید.

## Unknownهای باز

- رفتار کاربر واردنشده و تفاوت copy آن با کارجوی واردشده؛
- state vocabulary canonical درخواست شغلی؛
- نام و توضیح نهایی My Priority؛
- terminology نهایی Premium Insights؛
- policy نمایش recommendation reason و confidence؛
- نسبت رزومهٔ ساختاریافته، رزومهٔ شخصی و snapshot درخواست؛
- labelهای تأییدشدهٔ visibility و privacy رزومه؛
- variationهای mobile، email، campaign و transactional channel.
