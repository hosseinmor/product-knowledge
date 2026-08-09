---
id: shared.resume
kind: shared-product-concept
title: رزومه
summary: مفهوم shared Resume را تعریف می‌کند که توسط کارجو مدیریت می‌شود و در تجربه‌های recruiting Jobvision مصرف می‌شود.
status: draft
owner: تیم‌های محصول Jobvision
last_reviewed:
related:
  - jobvision.overview
  - jobvision.candidate.overview
  - jobvision.employer.overview
  - shared.application
  - jobvision.candidate.resume-management
topics:
  - resume
  - candidate
  - employer
  - application
  - professional-profile
  - recruiting
---

# رزومه

## تعریف

Resume نمایش shared پیشینه حرفه‌ای کارجو است که در تجربه‌های recruiting Jobvision استفاده می‌شود. Candidate مالک ساخت و نگهداری تجربه رزومه است، در حالی که recruiting سمت Employer ممکن است نمایی از آن را مصرف کند.

این concept فقط مالک معنا، relationshipها و lifecycleهایی است که واقعاً بین محصولات shared هستند. ساخت، ویرایش، راهنمای completion، visibility، access و presentation رزومه در Product Areaهای مربوط می‌ماند.

## چرا مهم است

رزومه اطلاعات حرفه‌ای مدیریت‌شده توسط کارجو را به تصمیم‌های recruiting وصل می‌کند:

```text
کارجو رزومه می‌سازد و به‌روزرسانی می‌کند
-> کارجو ممکن است هنگام apply از آن استفاده کند
-> Employer ممکن است نمایی از رزومه را ببیند
-> activity استخدامی ممکن است به آن نما وابسته باشد
```

تعریف shared برای جدا کردن رزومه قابل ویرایش فعلی از نسخه‌ای که به یک Application وصل شده مهم است.

## داده‌ها و attributeهای shared

field set canonical هنوز مستند نشده است.

دسته‌های محتمل مثل identity و contact information، سابقه کار، تحصیلات، مهارت‌ها، زبان‌ها، preferences، attachmentها، completeness و visibility باید قبل از confirmed shared attribute شدن بررسی شوند.

## Lifecycle مشترک

lifecycle کامل و مدل state نامشخص است.

repo هنوز مشخص نمی‌کند stateهای رزومه شامل incomplete، complete، published، hidden، archived یا versioned هستند یا این labelها بین محصولات shared هستند یا نه.

## قواعد shared

در سطح فعلی تأیید شده است:

- Candidate اطلاعات Resume را در محصول Candidate مدیریت می‌کند.
- اطلاعات Resume ممکن است در application و تجربه‌های recruiting سمت Employer استفاده شود.
- ویرایش، validation، permission، visibility و presentationهای product-specific باید در Product Areaها بمانند.
- رابطه بین Resume فعلی و representation رزومه attach شده به Application باید صریح باشد.

اینکه Application یک frozen snapshot، live reference، generated document یا ترکیبی از آن‌ها را ذخیره می‌کند هنوز نامشخص است.

## استفاده در محصولات و Areaها

### Jobvision Candidate

`jobvision.candidate.resume-management` مالک ساخت، ویرایش، completion، preview، export و visibility سمت کارجو است. انتخاب یا attachment هنگام application باید با رفتار Application reconcile شود.

### Jobvision Employer

Product Areaهای Employer مالک access و استفاده از اطلاعات Resume در مدیریت Candidate و Application هستند، مشروط به permissionها و قواعد visibility تأییدشده.

### Cando ATS

اینکه داده Resume به Cando ATS منتقل، copy، synchronize یا جداگانه نگهداری می‌شود هنوز نیاز به بررسی دارد.

## Variationهای product-specific

- Candidate به اطلاعات ساختاریافته قابل ویرایش، راهنمایی، preview و کنترل نیاز دارد.
- Employer به representation مناسب recruiting با access درست نیاز دارد.
- یک Application ممکن است حتی بعد از ویرایش رزومه فعلی توسط کارجو، representation تاریخی پایدار لازم داشته باشد.
- ATS ممکن است profile یا document نرمال‌شده جداگانه استفاده کند.

تفاوت‌های دقیق نیاز به review محصول و integration دارد.

## Unknownها

- fieldهای canonical shared
- ownership رزومه و مدل identity
- رزومه فعلی در برابر snapshot رزومه Application
- versioning و رفتار historical
- قواعد visibility و privacy
- چند رزومه یا variantهای زبانی
- رابطه generated file با structured data
- قواعد export و download
- access کارفرما قبل و بعد از application
- synchronization یا mapping با Cando ATS
- رفتار deletion و retention

## منابع

- `products/jobvision/overview.md`
- `products/jobvision/candidate/overview.md`
- `products/jobvision/employer/overview.md`
- `shared/product-concepts/application.md`
- تصمیم مالک محصول هنگام mapping Product Areaهای Candidate در 2026-08-06
- برای review کامل، evidenceهای Jira، Figma، production، analytics و walkthrough بیشتری لازم است.
