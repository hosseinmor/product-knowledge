---
id: shared.company
kind: shared-product-concept
title: شرکت
summary: مفهوم shared Company را تعریف می‌کند که در تجربه‌های Employer و Candidate جاب‌ویژن نمایش داده می‌شود.
status: draft
owner: تیم‌های محصول Jobvision
last_reviewed:
related:
  - jobvision.overview
  - jobvision.candidate.overview
  - jobvision.employer.overview
  - shared.job-post
topics:
  - company
  - employer
  - candidate
  - company-profile
  - job-post
  - followed-company
  - company-review
---

# شرکت

## تعریف

Company نمایش shared یک سازمان استخدام‌کننده در Jobvision است. کاربران سمت Employer اطلاعات سازمان و فعالیت‌های استخدامی را مدیریت می‌کنند، در حالی که Candidate از طریق Job Postها، اطلاعات Company، دنبال‌کردن، امتیازدهی و نظرها با آن مواجه می‌شود.

این concept باید از حساب کاربری Employer، اشتراک یا plan کارفرما، شخصیت حقوقی و brand جدا بماند؛ مگر اینکه evidence محصول یکسان‌بودن آن‌ها را تأیید کند.

## چرا مهم است

Company هویت مدیریت‌شده توسط Employer را به اعتماد و discovery سمت Candidate وصل می‌کند:

```text
Employer نماینده یک سازمان است
→ سازمان Job Post منتشر می‌کند
→ Candidate Company و فرصت‌های آن را ارزیابی می‌کند
→ Candidate ممکن است Company را دنبال، امتیازدهی یا review کند
```

تعریف shared از توصیف ناسازگار identity و relationshipهای Company در محصولات Employer و Candidate جلوگیری می‌کند.

## داده‌ها و attributeهای shared

field set canonical هنوز مستند نشده است.

اطلاعات محتملی مانند name، logo، industry، size، description، locationها، verification، public profile و relationship با حساب‌های Employer و Job Postها باید پیش از درنظرگرفتن به‌عنوان attribute shared تأییدشده، بررسی شوند.

rating، review و relationship دنبال‌کردن ممکن است entityهای مستقلی متصل به Company باشند، نه attributeهای Company.

## Lifecycle مشترک

lifecycle کامل shared نامشخص است.

stateهای احتمالی مربوط به creation، verification، publication، suspension، merge یا archive نیاز به review مالک دارند. status حساب Employer و visibility شرکت ممکن است lifecycleهای جداگانه داشته باشند.

## قواعد shared

در سطح فعلی تأیید شده است:

- Company نمایش سازمان سمت Employer را به اطلاعات سمت Candidate وصل می‌کند.
- Job Postها به یک Company مرتبط‌اند.
- تجربه‌های Candidate شامل دنبال‌کردن، rating یا review Company هستند.
- مدیریت، permission، presentation، رفتار دنبال‌کردن و رفتار review که product-specific هستند در Product Areaها می‌مانند.
- Company نباید خودبه‌خود هم‌معنای حساب Employer، subscription، شخصیت حقوقی یا brand تلقی شود.

قواعد دقیق ownership، verification، visibility، handling رکورد تکراری و moderation هنوز نامشخص‌اند.

## استفاده در محصولات و Areaها

### Jobvision Employer

Product Areaهای Employer مالک مدیریت profile شرکت، access سازمان، relationshipهای حساب و context استخدامی خواهند بود.

### Jobvision Candidate

Product Areaهای Candidate مالک مشاهده و ارزیابی اطلاعات Company، دنبال‌کردن Companyها و ایجاد یا مصرف rating و review در صورت کاربرد هستند.

### Job Postها و Applicationها

Company context سازمان را برای Job Postها و Applicationهای مرتبط با آن‌ها فراهم می‌کند. رفتار تاریخی دقیق در صورت تغییر اطلاعات Company نیاز به verification دارد.

## Variationهای product-specific

- Employer به اطلاعات سازمانی قابل ویرایش، access control و context عملیاتی نیاز دارد.
- Candidate به اطلاعات عمومی قابل اعتماد و signalهایی برای ارزیابی فرصت‌ها نیاز دارد.
- rating، review و follow permissionها و stateهای مخصوص Candidate دارند و نباید در این concept متمرکز شوند.

تفاوت‌های دقیق به review Product Area نیاز دارند.

## Unknownها

- fieldهای canonical Company
- Company در برابر حساب Employer، organization، brand و شخصیت حقوقی
- relationshipهای ownership و administrator
- قواعد verification و public-visibility
- رفتار duplicate، merge، rename و archive
- رابطه با location و شعبه‌ها
- رابطه با Job Post و Applicationهای تاریخی
- اینکه rating و review به Company تعلق دارند یا concept مستقل دیگری هستند
- رفتار relationship دنبال‌کردن و notification
- permissionهای moderation و پاسخ Employer

## منابع

- `products/jobvision/overview.md`
- `products/jobvision/candidate/overview.md`
- `products/jobvision/employer/overview.md`
- `shared/product-concepts/job-post.md`
- تصمیم مالک محصول و walkthrough محصول Candidate در 2026-08-06
- برای review کامل، evidenceهای Jira، Figma، production، analytics و walkthrough بیشتری لازم است.
