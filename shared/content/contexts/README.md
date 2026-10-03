---
id: content.contexts.overview
collection: content
type: content-overview
title: Content Context Contracts
summary: Routes approved product- and audience-specific language variations without moving product behavior out of Product Areas.
knowledge_state: verified
document_maturity: draft
related:
  - content.content-guidelines
  - content.product-voice
  - content.terminology
  - content.localization
---

# قراردادهای Context محتوا

این پوشه variationهایی را نگه می‌دارد که برای یک محصول یا audience مشخص لازم
هستند اما foundation، pattern یا component contract عمومی را تغییر نمی‌دهند.

```text
Foundation
→ صدای مشترک، terminology و localization

Pattern / Component
→ ساختار پیام و نقش copy در interaction

Context
→ انتخاب اصطلاح، شدت لحن و محدودیت ادعا برای یک product × audience

Product Area
→ رفتار، state، permission، validation و flow واقعی
```

Context نباید lifecycle، eligibility، consequence یا action تازه‌ای بسازد. هر
قاعدهٔ رفتاری باید از Product Area مربوط بیاید و unknownهای آن همان‌طور visible
بمانند.

## موجودی فعلی

| Context | سند انسانی | منبع machine-readable | ارزیابی |
|---|---|---|---|
| JobVision Candidate | [`jobvision-candidate.md`](jobvision-candidate.md) | [`jobvision-candidate.yml`](jobvision-candidate.yml) | [`../evals/jobvision-candidate-context-cases.yml`](../evals/jobvision-candidate-context-cases.yml) |
| JobVision Employer | [`jobvision-employer.md`](jobvision-employer.md) | [`jobvision-employer.yml`](jobvision-employer.yml) | [`../evals/jobvision-employer-context-cases.yml`](../evals/jobvision-employer-context-cases.yml) |
| Cando ATS | [`cando-ats.md`](cando-ats.md) | [`cando-ats.yml`](cando-ats.yml) | [`../evals/cando-ats-context-cases.yml`](../evals/cando-ats-context-cases.yml) |

## قاعدهٔ رشد

Context جدید فقط وقتی ساخته می‌شود که تفاوت واقعی در audience یا product با
قواعد shared وجود داشته باشد. نام متفاوت surface به‌تنهایی کافی نیست. قرارداد
بعدی باید evidence، Product Area مالک و evalهای blocking داشته باشد؛ scaffold
خالی نسازید.

## اعتبارسنجی

```bash
python scripts/check_content_contexts.py
```

Validator موجودی بستهٔ Contextها، هویت فایل‌ها، منبع قواعد، term decisionها و
پوشش همهٔ قواعد blocking در evalها را بررسی می‌کند.
