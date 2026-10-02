---
id: content.context.jobvision-employer
collection: content
type: content-context
title: JobVision Employer Content Context
summary: Defines audience-specific terminology, tone, claim boundaries, and Product Area routing for JobVision employer-side experiences.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.context.jobvision-candidate
  - jobvision.employer.overview
  - jobvision.employer.job-post-management
  - shared.job-post
  - shared.application
  - shared.resume
  - shared.company
topics:
  - jobvision
  - employer
  - organization
  - recruitment
  - job-post
  - terminology
  - product-content
---

# Context محتوایی JobVision Employer

این سند قواعد محتوایی مخصوص پنل کارفرمای جاب‌ویژن را تعریف می‌کند. قرارداد
machine-readable در [`jobvision-employer.yml`](jobvision-employer.yml) و
regression caseها در
[`../evals/jobvision-employer-context-cases.yml`](../evals/jobvision-employer-context-cases.yml)
قرار دارند.

## مرز Context

```text
Shared Content
→ معنی اصطلاح، صدای پایه، localization، pattern و component contract

Employer Context
→ preferred label و محدودیت ادعا برای کاربر سمت کارفرما

Employer Product Area
→ رفتار، state، permission، entitlement، validation و flow
```

Employer Context نام‌گذاری و claim boundary را تعیین می‌کند. این سند نقش‌های
واقعی حساب، quota، plan eligibility، lifecycle آگهی یا رفتار مدیریت درخواست‌های
شغلی را اختراع نمی‌کند.

## وضعیت منابع

### قواعد source-derived

- entity مشتری در Employer «سازمان» و actor انسانی «کارفرما» است.
- در سطح تخصصی و روشن پنل کارفرما، `job_post` با «آگهی» نامیده می‌شود.
- «موقعیت شغلی» خود نقش است و با آگهی یکی نیست.
- «جذب» process و «استخدام» outcome است.
- «درخواست جذب» نیاز داخلی سازمان و «درخواست شغلی» پاسخ کارجو به آگهی است.
- فرد JobVision «کارجو» و فرد ATS «کاندیدا» است.
- بسته، پلن و سرویس conceptهای یکسان نیستند.

### تصمیم‌های عملیاتی Context

- صورت کوتاه «آگهی» فقط در surface تخصصی و self-contained Employer استفاده
  می‌شود؛ در notification، email یا متن مستقل «آگهی شغلی» روشن‌تر است.
- اصطلاح داخلی فقط وقتی نمایش داده می‌شود که visibility و public label آن
  تأیید شده باشد.
- publication، activity یا automation فقط در حد outcome تأییدشده توصیف می‌شود.

### خارج از مالکیت

- نام و permission دقیق Recruiter، HR، Hiring Manager و Admin؛
- lifecycle آگهی و تفاوت Draft، Published، Paused، Closed، Archived و Expired؛
- quota، plan access، moderation و publication eligibility؛
- رفتار Candidate/Application Management؛
- اثر تغییر آگهی روی Candidate و درخواست‌های موجود؛
- تعریف عمومی Premium Subscription و صف رد؛
- رفتار دستیار کارفرما و automation رد درخواست‌ها.

## مخاطب و خطاب

کاربران این محصول می‌توانند recruiter، عضو منابع انسانی، مدیر استخدام یا مدیر
حساب باشند، اما role nameهای رسمی و permissionهایشان هنوز تأیید نشده است.
بنابراین در copy مستقیم از «شما» استفاده کنید و نقش خاص را فقط از Product Area
یا access model تأییدشده بگیرید.

```text
می‌توانید آگهی را پیش از انتشار بازبینی کنید.
برای انتشار، اطلاعات لازم را تکمیل کنید.
```

از خطاب‌های فرضی مانند «مدیر محترم منابع انسانی» یا «ادمین سازمان» استفاده
نکنید مگر همان role در product truth ثبت شده باشد.

## مدل اصطلاحات

### سازمان، کارفرما و رابط

| Concept | label | visibility |
|---|---|---|
| `employer_organization` | سازمان | user-facing Employer |
| `employer_actor` | کارفرما | نقش انسانی/عمومی |
| `operator` | رابط | internal/admin و هنوز draft |
| `system_operator` | بدون label عمومی | needs decision |

```text
اطلاعات سازمان
اعضای سازمان
فعالیت کارفرما
```

`کارفرما` نام entity سازمان نیست. `رابط` نیز نباید صرفاً به‌دلیل وجود در source
code به label عمومی پنل تبدیل شود.

### آگهی، موقعیت و فرصت

در صفحه‌ها و فهرست‌های تخصصی Employer که object روشن است:

```text
ایجاد آگهی
ویرایش آگهی
آگهی‌های سازمان
```

در پیام مستقل یا channel بیرون از پنل:

```text
آگهی شغلی شما منتشر شد.
انتشار آگهی شغلی ناموفق بود.
```

`موقعیت شغلی` نقش واقعی‌ای است که سازمان برای آن نیرو می‌خواهد. `فرصت شغلی`
عبارت عمومی discovery است و label موجودیت مدیریت‌شده نیست. «آگهی استخدام» و
«وکنسی» نیز preferred نیستند.

### جذب و استخدام

```text
فرایند جذب
تیم جذب
درخواست جذب
تصمیم استخدام
تاریخ استخدام
```

جذب با استخدام synonym نیست. بررسی رزومه، مصاحبه یا انتقال مرحله outcome
استخدام را به‌تنهایی ثابت نمی‌کند.

### درخواست جذب و درخواست شغلی

| Concept | معنی | label |
|---|---|---|
| `hiring_request` | درخواست داخلی سازمان برای آغاز جذب | درخواست جذب |
| `job_application` | پاسخ کارجو به یک آگهی | درخواست شغلی / درخواست در context روشن |

در surface مستقل «درخواست شغلی» را کامل بنویسید. `ارسال رزومه` action سمت کارجو
است و label entity مدیریت‌شده در Employer نیست.

### کارجو و کاندیدا

فردی که از JobVision برای یک آگهی درخواست فرستاده، در مدل shared `کارجو` است.
`کاندیدا` concept مخصوص ATS است و می‌تواند فردی را هم شامل شود که recruiter
مستقیماً اضافه کرده است. تا زمانی که mapping JobVision Employer و Cando ATS
تأیید نشده، این دو label را آزادانه جابه‌جا نکنید.

### رزومه و snapshot

نام user-facing سند حرفه‌ای `رزومه` است. `اسنپشات رزومه` artifact داخلی است؛
اگر لازم باشد برای کاربر توضیح داده شود، از «نسخهٔ رزومه در زمان ارسال درخواست
شغلی» استفاده کنید. هنوز معلوم نیست Employer همیشه live resume، snapshot یا
ترکیبی از آن‌ها را می‌بیند؛ copy نباید یکی را تضمین کند.

### بسته، پلن، سرویس و اشتراک ویژه

- `بسته` entitlement خریداری‌شده/اختصاص‌یافته به یک سازمان است؛
- `پلن` سطح خدمات مرتبط با آگهی است؛
- `سرویس` کوچک‌ترین entitlement مصرف‌شدنی و فعلاً internal است؛
- `اشتراک ویژه` definition محصولی تأییدشده ندارد و user-facing ممنوع است.

این چهار concept را برای ساده‌سازی copy synonym نکنید. entitlement، مانده،
انقضا و اثر خرید باید از Product Area مربوط بیاید؛ Area محصولات و پلن‌ها هنوز
مستند نشده است.

### دستیار کارفرما

`دستیار کارفرما` در واژه‌نامه automation مشخصی است، نه نمونهٔ عمومی
`دستیار هوشمند`. رفتار ثبت‌شدهٔ آن draft است و نباید بدون تأیید runtime دربارهٔ
رد خودکار، مهلت یا notification آن ادعا کرد. «صف رد» نیز internal،
`needs_decision` و طبق منبع احتمالاً غیرفعال است؛ آن را به UI عمومی نیاورید.

## لحن Employer

Employer surface عملیاتی و تصمیم‌محور است:

- label و instruction مستقیم و نتیجه‌محور باشد؛
- در publication، permission، quota و error وضوح حداکثری باشد؛
- urgency یا فشار تبلیغاتی برای خرید/انتشار ساخته نشود؛
- مسئولیت failure مبهم به کاربر یا سازمان نسبت داده نشود؛
- موفقیت فقط پس از تأیید outcome نوشته شود.

```text
آگهی شغلی منتشر نشد. اطلاعات الزامی را بررسی کنید.  ← اگر validation معلوم است
فرصت طلایی شما رو به پایان است؛ همین حالا منتشر کنید! ← نامناسب
```

## مرز ادعاهای محصول

Job Post Management هنوز draft است. بنابراین:

- state nameهای فعلی placeholder هستند؛
- وجود save draft، autosave، duplicate، pause یا archive قطعی نیست؛
- انتشار موفق لزوماً visibility فوری برای همهٔ کارجوها را ثابت نمی‌کند؛
- باقی‌ماندن درخواست‌های قبلی بعد از pause/close هنوز rule قطعی نیست؛
- plan، quota، moderation و approval تأیید نشده‌اند؛
- permission نقش‌ها مستند نیست.

متن باید minimum sufficient claim را بنویسد:

```text
آگهی شغلی منتشر شد.                 ← فقط پس از outcome تأییدشده
آگهی برای همهٔ کارجوها فعال شد.     ← فقط با visibility evidence
```

## Routing به Product Area

| موضوع | منبع رفتار |
|---|---|
| ایجاد، ویرایش، انتشار و مدیریت آگهی | `jobvision.employer.job-post-management` |
| حساب، اعضا، role و permission | Area مستندنشدهٔ Employer Account and Access |
| درخواست‌های شغلی و رزومه‌ها | Area مستندنشدهٔ Candidate and Application Management |
| بسته، پلن، quota و خرید | Area مستندنشدهٔ Employer Products and Plans |

اگر Area مستند نشده یا پاسخ قطعی ندارد، copy نباید behavior را بسازد. unknown
را ثبت کنید و برای owner review نگه دارید.

## Pattern، Component و Localization

Employer Context همراه pattern و component contract مشترک استفاده می‌شود:

- انتشار یا تغییر وضعیت consequential → Confirmation pattern و Modal contract؛
- validation و failure → Error pattern؛
- outcome کوتاه → Notification pattern و contract؛
- action label → Button contract؛
- field requirement → Instructions و Text Input contract.

تعداد آگهی، ماندهٔ بسته، مبلغ، تاریخ انقضا، شناسه، نام کارجو و عنوان آگهی باید
طبق Localization format و isolate شوند. Context دربارهٔ رقم، currency، timezone
یا rounding تصمیم تازه‌ای نمی‌گیرد.

## قرارداد قطعی

### باید

- سازمان، کارفرما و نقش‌های داخلی را از هم جدا نگه دارید.
- در سطح تخصصی Employer «آگهی» و در پیام مستقل «آگهی شغلی» بنویسید.
- جذب، استخدام، درخواست جذب و درخواست شغلی را مطابق concept انتخاب کنید.
- رفتار، permission، entitlement و state را از Area مالک بگیرید.
- unknownها و محدودیت شواهد را در claim حفظ کنید.

### نباید

- سازمان را «کارفرما» یا رابط را role عمومی بنامید.
- کارجو و کاندیدای ATS را بدون mapping یکی کنید.
- package، plan، service و subscription را synonym فرض کنید.
- اصطلاحات `needs_decision` مانند صف رد یا اشتراک ویژه را public کنید.
- state، quota، permission، moderation یا visibility سمت Candidate را حدس بزنید.

## Unknownهای باز

- نام رسمی roleهای Employer و permission matrix؛
- Product Areaهای Account/Access، Application Management و Products/Plans؛
- lifecycle و state vocabulary آگهی؛
- publication eligibility، quota، moderation و approval؛
- mapping کارجو، درخواست و رزومه با Cando ATS؛
- رفتار و نام نهایی دستیار کارفرما؛
- تعریف و مالک Premium Subscription؛
- visibility و retention رزومه و application؛
- channel variationهای email، notification و campaign.
