# AI Context Retrieval Flow

## اصل سیستم

ای‌آی کل Product Knowledge را نمی‌خواند. ابتدا نوع کار را تشخیص می‌دهد، قرارداد همان workflow را می‌خواند، سپس از Manifest برای پیدا کردن کوچک‌ترین مجموعه اسناد مرتبط استفاده می‌کند.

---

## ای‌آی از کجا شروع می‌کند؟

```text
AGENTS.md
   ↓
ai/router.md
   ↓
تشخیص Intent
   ├── Write / Review PRD
   ├── Start Design
   └── Update Knowledge
```

### 1. `AGENTS.md`

نقطه ورود AI به repository است.

کارش این است که:

- قواعد کلی repository را مشخص کند.
- به AI بگوید برای هر نوع task از چه workflow یا skillی استفاده کند.
- مرزها و source of truth را مشخص کند.

### 2. `ai/router.md`

بعد از ورود، AI intent کاربر را تشخیص می‌دهد.

مثلاً:

- اگر کاربر PRD بخواهد → مسیر PRD Writing
- اگر PRD تأیید شده باشد و طراحی بخواهد → مسیر Design Start
- اگر دانش محصول نیاز به اصلاح داشته باشد → مسیر Knowledge Update

---

# مسیر AI برای نوشتن PRD

```text
PM Input
   ↓
AGENTS.md
   ↓
ai/router.md
   ↓
ai/skills/prd-writing/SKILL.md
   ↓
┌─────────────────────┬────────────────────────┐
│ ai/prd-writing.md   │ templates/jira-prd.md │
│ Process Contract    │ Output Contract         │
└─────────────────────┴────────────────────────┘
   ↓
manifest.generated.json
   ↓
Relevant Product Knowledge
   ↓
Context Synthesis
   ↓
Blocking Decisions
   ↓
PM Decision
   ↓
Jira-ready PRD
```

## 1. ورودی اولیه PM

مدیر محصول لازم نیست یک PRD کامل بنویسد.

حداقل ورودی مورد نیاز:

- Problem
- Why it matters or supporting evidence
- Affected users
- Desired outcome
- Known constraints

---

## 2. `ai/skills/prd-writing/SKILL.md`

این فایل execution contract برای AI است.

AI از این فایل می‌فهمد:

- این task دقیقاً چه هدفی دارد.
- چه فایل‌هایی باید خوانده شوند.
- چه چیزهایی را نباید حدس بزند.
- چه زمانی باید سؤال بپرسد.
- مسئولیت AI چیست.
- مسئولیت PM چیست.
- خروجی نهایی باید چه شکلی تحویل داده شود.

به بیان ساده:

> Skill به AI می‌گوید «برای نوشتن PRD چطور رفتار کن».

---

## 3. `ai/prd-writing.md`

این فایل Process Contract است.

یعنی ترتیب فرایند PRD Writing را مشخص می‌کند.

AI باید:

1. Product Context مرتبط را پیدا کند.
2. رفتار فعلی محصول را استخراج کند.
3. رفتار فعلی و رفتار مورد انتظار را از هم جدا کند.
4. gapها و contradictionها را پیدا کند.
5. فقط Blocking Questionها را تشخیص دهد.
6. تصمیم PM را دریافت کند.
7. PRD را draft کند.
8. خروجی را validate کند.

---

## 4. `templates/jira-prd.md`

این فایل Output Contract است.

یعنی تعیین می‌کند PRD نهایی چه ساختاری داشته باشد.

ساختار فعلی:

- Product context
- Problem
- Why it matters
- Affected users
- Desired outcome
- Current behavior
- Scope
  - In scope
  - Out of scope
- Expected behavior
- Main flow
- Alternate and error flows
- Rules
- Permissions
- States and transitions
- Validations and edge cases
- Shared service behavior and fallback
- Dependencies and constraints
- Open questions
- Success criteria
- Related Product Knowledge
- Design references

---

# Manifest چه کار می‌کند؟

## `manifest.generated.json`

Manifest خودش Product Knowledge نیست.

Manifest مثل یک index یا routing table برای Knowledge Base عمل می‌کند.

```text
PRD Context
   ↓
manifest.generated.json
   ↓
Filter by:
- group
- product
- kind
- title
- summary
- topics
- related IDs
   ↓
Smallest Relevant Document Set
```

به جای اینکه AI کل repository را بخواند، Manifest کمک می‌کند فقط documentهای مرتبط را پیدا کند.

مثلاً برای یک feature در Apply Flow ممکن است فقط این‌ها لازم باشند:

```text
Jobvision Overview
        ↓
Candidate Overview
        ↓
Candidate Apply Product Area
        ↓
Application Shared Concept
        ↓
Relevant Shared Service
```

در نتیجه:

> AI هر بار صدها فایل را وارد context نمی‌کند؛ فقط کوچک‌ترین مجموعه اطلاعاتی که برای تصمیم فعلی لازم است retrieve می‌شود.

---

# AI بعد از Manifest چه فایل‌هایی را می‌خواند؟

AI بسته به مسئله ممکن است از چند نوع سند استفاده کند.

## Product Group Overview

برای درک context سطح بالای مجموعه محصول.

مثلاً:

```text
Jobvision
```

## Product Overview

برای شناخت boundary و کاربران یک محصول مشخص.

مثلاً:

```text
Candidate
```

## Product Areas

مهم‌ترین منبع رفتار فعلی محصول.

Product Area می‌تواند شامل این‌ها باشد:

- User outcomes
- Flows
- Rules
- Permissions
- States
- Validations
- Edge cases

مثلاً:

```text
Candidate Apply
```

## Shared Product Concepts

وقتی یک مفهوم در چند محصول مشترک است.

مثلاً:

```text
Application
Resume
Job Post
Company
```

## Shared Product Services

وقتی یک service بین چند محصول استفاده می‌شود.

مثلاً:

```text
AI Matching Service
AI Fit Service
```

رفتار خود service اینجا تعریف می‌شود و نحوه استفاده یک محصول از آن داخل Product Area همان محصول باقی می‌ماند.

## Content / Product Standards

فقط زمانی خوانده می‌شوند که روی feature اثر داشته باشند.

AI نباید کل این بخش‌ها را بدون نیاز وارد context کند.

---

# Context Synthesis

بعد از خواندن اسناد مرتبط، AI اطلاعات را مستقیم وارد PRD نمی‌کند.

ابتدا آن‌ها را دسته‌بندی می‌کند:

```text
Current Behavior
→ چیزی که امروز طبق Product Knowledge وجود دارد

Intended Behavior
→ چیزی که PM برای feature جدید می‌خواهد

Assumption
→ چیزی که برای ادامه لازم است ولی هنوز تأیید نشده

Open Question
→ تصمیمی که هنوز مشخص نشده

Recommendation
→ پیشنهاد AI، نه Product Decision
```

این تفکیک یکی از guardrailهای اصلی سیستم است.

هدف این است که AI:

- assumption را fact در نظر نگیرد.
- رفتار فعلی و رفتار آینده را با هم مخلوط نکند.
- recommendation خودش را تصمیم محصول تلقی نکند.

---

# Blocking Questions

بعد از ساخت context، AI بررسی می‌کند آیا تصمیمی وجود دارد که بدون آن PRD قابل اعتماد نیست.

فقط سؤال‌هایی blocking محسوب می‌شوند که جوابشان بتواند این موارد را تغییر دهد:

- Scope
- Main Flow
- Business Rule
- Permission
- State Transition
- Validation
- Destructive Behavior
- Shared Service Behavior
- Technical Feasibility
- Success Criteria

```text
AI detects gap
      ↓
Is it blocking?
   ├── No  → Continue drafting
   └── Yes → Ask PM
                ↓
           PM Decision
                ↓
           Continue PRD
```

AI نباید برای موارد کم‌اهمیت مثل copy یا layout فرایند PRD را متوقف کند.

---

# خروجی PRD

بعد از دریافت تصمیم‌های لازم، AI:

1. PRD را بر اساس Template می‌سازد.
2. consistency را بررسی می‌کند.
3. assumptions و open questions را visible نگه می‌دارد.
4. Product Knowledge استفاده‌شده را reference می‌دهد.
5. PRD را برای Review و Approval PM تحویل می‌دهد.

```text
Product Knowledge
      +
PM Input
      +
PM Decisions
      ↓
AI Validation
      ↓
Jira-ready PRD
      ↓
PM Approval
```

---

# بعد از Approved PRD چه اتفاقی می‌افتد؟

بعد از تأیید PRD وارد Design Start می‌شویم.

```text
Approved PRD
      +
Product Knowledge
      +
Shared Product Services
      +
Design System
      ↓
ai/design-start.md
      ↓
AI Design Context
      ↓
Initial Design Draft
      ↓
Designer Review
      ↓
Final Design
```

---

# مسیر AI در Design Start

## 1. Approved PRD

PRD مشخص می‌کند:

> چه چیزی باید تغییر کند؟

## 2. `ai/design-start.md`

این workflow به AI می‌گوید برای شروع طراحی چه contextی لازم دارد و چه artifactهایی می‌تواند تولید کند.

## 3. `manifest.generated.json`

Manifest دوباره استفاده می‌شود.

این بار retrieval فقط Product Knowledge نیست.

AI می‌تواند اسناد مرتبط از این بخش‌ها را پیدا کند:

```text
Product Knowledge
Shared Product Concepts
Shared Product Services
Design System
Content Guidance
```

---

# Design System Retrieval

AI کل Design System را نمی‌خواند.

فقط قسمت‌هایی را انتخاب می‌کند که برای طراحی فعلی لازم هستند.

مثلاً اگر feature شامل form داخل modal باشد:

```text
Design System
   ↓
Text Input
Select
Checkbox
Button
Modal
Validation
Action Hierarchy
Error Recovery
```

در نتیجه Design System هم بخشی از targeted retrieval است.

---

# AI Design Context

قبل از تولید UI، AI این context را آماده می‌کند:

- User goal
- Current behavior
- Intended change
- Rules
- Permissions
- States
- Edge cases
- Shared Service dependencies
- Relevant components
- Relevant patterns
- UX rules
- Open questions

بعد می‌تواند artifactهایی مثل این‌ها تولید کند:

```text
User Flow
Screen Inventory
State Matrix
Information Architecture
Wireframe
UI Draft
Component Mapping
Copy Draft
```

---

# خروجی Design Start

خروجی این مرحله Final Design نیست.

```text
AI Design Draft
      ↓
Designer Review
      ↓
Evaluate Solutions
Interaction Decisions
UX Trade-offs
Visual Hierarchy
Simplification
      ↓
Final Design
```

AI نقطه شروع را جلو می‌آورد؛ Designer همچنان مسئول تصمیم طراحی است.

---

# نمای کلی سیستم

```text
                         ┌──────────────────────────┐
                         │          PM Input        │
                         │ Problem / Outcome / ...  │
                         └────────────┬─────────────┘
                                      ↓
                               ┌─────────────┐
                               │  AGENTS.md  │
                               └──────┬──────┘
                                      ↓
                               ┌─────────────┐
                               │ ai/router.md│
                               └──────┬──────┘
                                      ↓
                        ┌────────────────────────┐
                        │   PRD Writing Skill    │
                        └───────────┬────────────┘
                                    ↓
               ┌────────────────────┴────────────────────┐
               ↓                                         ↓
       ai/prd-writing.md                        templates/jira-prd.md
       Process Contract                         Output Contract
               └────────────────────┬────────────────────┘
                                    ↓
                         manifest.generated.json
                                    ↓
                      Relevant Product Knowledge
                                    ↓
                         Context + Gap Detection
                                    ↓
                            Blocking Questions
                                    ↓
                              PM Decisions
                                    ↓
                              Approved PRD
                                    ↓
                            ai/design-start.md
                                    ↓
                         manifest.generated.json
                                    ↓
               ┌────────────────────┼────────────────────┐
               ↓                    ↓                    ↓
        Product Knowledge    Shared Services       Design System
               └────────────────────┼────────────────────┘
                                    ↓
                            AI Design Context
                                    ↓
                            AI Design Draft
                                    ↓
                           Designer Review
                                    ↓
                              Final Design
```

---

# خلاصه

## PRD Flow

```text
AGENTS.md
→ ai/router.md
→ PRD Writing Skill
→ PRD Workflow + Template
→ Manifest
→ Relevant Product Knowledge
→ Context Synthesis
→ Blocking Decisions
→ PM
→ Jira-ready PRD
```

## Design Flow

```text
Approved PRD
→ ai/design-start.md
→ Manifest
→ Relevant Product Knowledge
→ Relevant Shared Services
→ Relevant Design System
→ AI Design Context
→ Design Draft
→ Designer
```

## مهم‌ترین ایده معماری

```text
AI does not read everything.

AI identifies intent
→ loads workflow rules
→ retrieves only relevant context
→ produces a draft
→ human makes the decision
```

این ساختار Product Knowledge را از یک repository مستندات به یک **Shared Context Layer برای PM، AI و Designer** تبدیل می‌کند.
