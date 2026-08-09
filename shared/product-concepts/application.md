---
id: shared.application
kind: shared-product-concept
title: درخواست
summary: مفهوم shared Application را تعریف می‌کند که submission و tracking سمت کارجو را به مدیریت recruiting سمت کارفرما وصل می‌کند.
status: draft
owner: تیم‌های محصول Jobvision
last_reviewed:
related:
  - jobvision.overview
  - jobvision.candidate.overview
  - jobvision.employer.overview
  - shared.job-post
  - shared.resume
  - jobvision.candidate.application-management
topics:
  - application
  - job-application
  - candidate
  - employer
  - job-post
  - resume
  - recruiting
---

# درخواست

## تعریف

Application نمایش shared این است که یک کارجو برای یک Job Post مشخص apply کرده است. این مفهوم submission و progress tracking سمت کارجو را به دریافت و مدیریت recruiting سمت کارفرما وصل می‌کند.

این مفهوم از flow خود Apply جداست. shared concept مالک معنای cross-product و relationshipهای Application است؛ submission، tracking، review، permission و presentation در Product Areaهای مربوط به خودشان می‌مانند.

## چرا مهم است

Application دو سمت گروه محصول Jobvision را به هم وصل می‌کند:

```text
کارجو روی یک Job Post apply می‌کند
-> یک Application ایجاد می‌شود
-> کارجو پیشرفت آن را دنبال می‌کند
-> کارفرما آن را دریافت و مدیریت می‌کند
```

تعریف shared جلوی این را می‌گیرد که مستندات Candidate و Employer یک record استخدامی واحد را ناسازگار توصیف کنند.

## داده‌ها و attributeهای shared

repo فعلاً فقط رابطه اصلی بین action کارجو، یک Job Post و activity استخدامی سمت Employer را پشتیبانی می‌کند.

field set canonical هنوز مستند نشده است. Candidate identity، Job Post، زمان submission، source، Resume یا version رزومه attach شده، answerها و status باید قبل از confirmed shared attribute شدن بررسی شوند.

## Lifecycle مشترک

lifecycle کامل و نام دقیق stateها هنوز مستند نشده است.

مرحله‌های احتمالی مثل started، submitted، viewed، under review، progressed، rejected، withdrawn یا hired باید در برابر رفتار Candidate، Employer و ATS توسط ownerها review شوند.

## قواعد shared

در سطح فعلی تأیید شده است:

- Application action کارجو را به یک Job Post مشخص وصل می‌کند.
- رفتار submission و tracking سمت کارجو در Product Areaهای Candidate می‌ماند.
- review و recruiting management سمت Employer در Product Areaهای Employer می‌ماند.
- داده‌ها، relationshipها و lifecycle shared نباید جداگانه در هر محصول دوباره تعریف شوند.

قواعد duplicate application، withdrawal، reapplication، deletion، visibility، synchronization status و retention هنوز نامشخص است.

## استفاده در محصولات و Areaها

### Jobvision Candidate

`jobvision.candidate.application-management` مالک progress tracking و مدیریت سمت کارجو بعد از submission است. flow submission آینده می‌تواند در همان Area بماند یا فقط اگر نگهداری آن سخت شد جدا شود.

### Jobvision Employer

Product Areaهای Employer مالک دریافت، مشاهده، ارزیابی، پیش‌بردن، رد کردن و سایر مدیریت‌های Application هستند.

### Cando ATS

اینکه یک Jobvision Application به Cando ATS منتقل، copy، synchronize یا به entity دیگری تبدیل می‌شود هنوز نیاز به بررسی دارد.

## Variationهای product-specific

یک Application واحد ممکن است در محصولات مختلف متفاوت نمایش داده شود، چون هر محصول از کاربر و تصمیم متفاوتی پشتیبانی می‌کند:

- کارجو به feedback submission و progress قابل فهم نیاز دارد.
- Employer به context استخدامی، کنترل‌های ارزیابی و stateهای عملیاتی نیاز دارد.
- ATS ممکن است داده و lifecycle مخصوص pipeline لازم داشته باشد.

تفاوت‌های دقیق نیاز به review Product Area و integration دارد.

## Unknownها

- fieldهای canonical shared
- lifecycle دقیق و ownership stateها
- Application draft در برابر submitted
- قواعد duplicate application و reapplication
- رفتار withdrawal و deletion
- رابطه با رزومه فعلی و snapshot رزومه ارسال‌شده
- رابطه با screening questionها و answerها
- قواعد visibility و retention
- synchronization یا mapping با Cando ATS
- رفتار وقتی Job Post مرتبط بسته، expired یا حذف می‌شود

## منابع

- `products/jobvision/overview.md`
- `products/jobvision/candidate/overview.md`
- `products/jobvision/employer/overview.md`
- `shared/product-concepts/job-post.md`
- تصمیم مالک محصول هنگام mapping Product Areaهای Candidate در 2026-08-06
- برای review کامل، evidenceهای Jira، Figma، production، analytics و walkthrough بیشتری لازم است.
