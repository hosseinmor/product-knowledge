---
id: content.context.cando-ats
collection: content
type: content-context
title: Cando ATS Content Context
summary: Defines ATS-specific terminology, audience language, evidence boundaries, and Product Area routing for recruiting operations.
knowledge_state: verified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - cando.ats.overview
  - cando.ats.recruitment-request
  - cando.ats.approval-workflow
  - cando.ats.job-management
  - shared.application
  - shared.resume
  - shared.company
  - shared.job-post
topics:
  - cando
  - ats
  - recruitment
  - approval
  - candidates
  - product-content
---

# Context محتوایی Cando ATS

این سند قواعد محتوایی مخصوص Cando ATS را تعریف می‌کند. قرارداد
machine-readable در [`cando-ats.yml`](cando-ats.yml) و regression caseها در
[`../evals/cando-ats-context-cases.yml`](../evals/cando-ats-context-cases.yml)
قرار دارند.

## مرز Context

```text
Shared Content
→ معنی اصطلاح، صدای پایه، localization، pattern و component contract

Cando ATS Context
→ preferred label، تفکیک concept و محدودیت ادعا برای کاربران ATS

ATS Product Area
→ رفتار، state، permission، validation، AI behavior و flow واقعی
```

Context نام‌گذاری و claim boundary را تعیین می‌کند. از وجود یک action، tab یا
گروه مشاهده‌شده نمی‌توان permission، lifecycle یا automation کامل را نتیجه
گرفت.

## وضعیت منابع

### قواعد source-derived

- `Recruitment Request` نیاز داخلی سازمان است و با `Job` یک entity نیست.
- `Approval Workflow` از مرحله‌های مرتب و تأییدکنندگان انتخاب‌شده تشکیل می‌شود.
- `ATS Job` workspace استخدامی است که اطلاعات شغل، فرم درخواست، مراحل جذب،
  دسترسی تیم، تنظیمات انتشار و درخواست‌های مرتبط را کنار هم نگه می‌دارد.
- Job Management در پنج بخش اطلاعات شغل، فرم درخواست، مراحل جذب، اعضای تیم و
  انتشار مشاهده شده است.
- در board مشاهده‌شده، درخواست‌های در حال بررسی در ستون‌های مرحلهٔ جذب نمایش
  داده می‌شوند و گروه‌های «در حال بررسی» و «ردشده» وجود دارند.
- UI مرتب‌سازی مرتبط‌ترین رزومه‌ها را براساس تطبیق با شرح شغل معرفی می‌کند.

### سطح اطمینان منابع

| منبع | وضعیت | نحوهٔ استفاده |
|---|---|---|
| ATS Overview | draft | مرز اولیهٔ محصول و audience |
| Recruitment Request | draft | قواعد جاری، با حفظ نیاز به verification |
| Approval Workflow | draft | قواعد جاری، با حفظ نیاز به verification |
| Job Management | reviewed | فقط برای scope مشاهده‌شده در یک حساب |

`reviewed` بودن Job Management به این معنی نیست که همهٔ accountها، planها،
roleها یا حالت‌های lifecycle بررسی شده‌اند.

### تصمیم‌های عملیاتی Context

- در surface تخصصی ATS از «شغل» و در مستندات، notification یا متن مستقل از
  «شغل ATS» استفاده می‌شود.
- `pipeline` اصطلاح فنی است؛ label عمومی concept مشاهده‌شده «مراحل جذب» است.
- رتبه‌بندی رزومه یک قابلیت مبتنی بر هوش مصنوعی است، نه «دستیار هوشمند» و نه
  حکم قطعی دربارهٔ شایستگی کاندیدا.
- گروه‌ها و actionهای مشاهده‌شده به state model یا permission کامل تعمیم داده
  نمی‌شوند.

### خارج از مالکیت

- نام رسمی roleها و permission inheritance؛
- lifecycle کامل شغل، درخواست و کاندیدا؛
- رابطه و cardinality دقیق شغل ATS، درخواست جذب و آگهی شغلی؛
- منطق رد خودکار و recovery آن؛
- eligibility، هزینه، moderation و sync کانال‌های انتشار؛
- کیفیت، explainability، bias و fallback رتبه‌بندی هوشمند؛
- mapping هویت و state با JobVision.

## مخاطب و خطاب

مخاطبان ممکن است عضو تیم جذب یا منابع انسانی، مالک درخواست، نمایندهٔ واحد،
تأییدکننده یا مدیر گردش کار باشند. چون نام رسمی نقش‌ها و permissionهایشان هنوز
تأیید نشده، در copy مستقیم از «شما» استفاده کنید و role خاص را فقط از access
model تأییدشده بگیرید.

```text
می‌توانید اطلاعات شغل را پیش از انتشار بازبینی کنید.
برای ادامه، مرحله‌های لازم را تکمیل کنید.
```

خطاب‌هایی مانند «مدیر منابع انسانی» یا «ادمین گردش کار» بدون evidence مجاز
نیستند.

## مدل اصطلاحات

### سازمان، کاندیدا و کارجو

| Concept | label | کاربرد |
|---|---|---|
| `employer_organization` | سازمان | entity مشتری ATS |
| `ats_candidate` | کاندیدا | فرد مدیریت‌شده در ATS |
| `jobseeker` | کارجو | هویت فرد در JobVision |

کاندیدا ممکن است از JobVision آمده یا مستقیماً در ATS اضافه شده باشد. تا وقتی
mapping cross-product تأیید نشده، «کاندیدا» و «کارجو» synonym نیستند.

### شغل ATS، آگهی شغلی و موقعیت شغلی

| Concept | معنی | label |
|---|---|---|
| `ats_job` | workspace استخدامی در ATS | شغل / شغل ATS |
| `job_post` | موجودیت منتشرشده برای جذب مخاطب | آگهی شغلی |
| `job_position` | نقش واقعی موردنیاز سازمان | موقعیت شغلی |

```text
ویرایش شغل                         ← surface تخصصی ATS
تنظیمات شغل ATS                   ← متن مستقل یا مستندات
انتشار آگهی شغلی در JobVision     ← publication entity/channel
موقعیت شغلی کارشناس فروش          ← نقش واقعی
```

رابطهٔ دقیق این سه entity هنوز کامل تأیید نشده است؛ به‌خصوص نباید فرض کرد هر
شغل ATS دقیقاً یک درخواست جذب یا یک آگهی شغلی دارد.

### درخواست جذب و درخواست شغلی

`درخواست جذب` نیاز داخلی سازمان برای آغاز یا پیش‌برد جذب است. `درخواست شغلی`
پاسخ یک فرد به فرصت استخدامی است و در context کاملاً روشن می‌تواند کوتاه‌شدهٔ
«درخواست» داشته باشد. این دو concept را حتی اگر در یک flow به هم مرتبط‌اند یکی
نام‌گذاری نکنید.

### جذب و استخدام

از «جذب» برای process و از «استخدام» برای decision یا outcome استفاده کنید:

```text
فرایند جذب
مرحلهٔ جذب
تیم جذب
تصمیم استخدام
تاریخ استخدام
```

جابجایی کاندیدا بین مرحله‌ها یا امتیاز بالای تطبیق، استخدام را ثابت نمی‌کند.

### گردش کار تأیید و مراحل جذب

| Concept | label |
|---|---|
| `approval_workflow` | گردش کار تأیید |
| `approval_step` | مرحلهٔ تأیید |
| `approver` | تأییدکننده |
| `hiring_stage` | مرحلهٔ جذب / مراحل جذب |

مرحلهٔ تأیید برای تصمیم روی درخواست جذب است؛ مرحلهٔ جذب برای سازمان‌دهی
کاندیداها و درخواست‌ها در یک شغل ATS. `pipeline` واژهٔ فنی و `code_only` است و
نباید label عمومی این مفهوم باشد.

### رزومه، آزمون و امتیاز تطبیق

برای artifact حرفه‌ای از «رزومه»، برای capability ارزیابی از «آزمون» و برای
metric تناسب از «امتیاز تطبیق» استفاده کنید. وجود امتیاز یا ترتیب نمایش، نتیجهٔ
استخدام، کیفیت قطعی یا بی‌طرفی تصمیم را تضمین نمی‌کند.

### هوش مصنوعی و دستیار هوشمند

مرتب‌سازی رزومه‌ها براساس تطبیق با شرح شغل یک قابلیت مبتنی بر «هوش مصنوعی» است.
تا وقتی تجربهٔ مستقل و assistant-like وجود ندارد آن را «دستیار هوشمند» ننامید.

```text
رزومه‌ها براساس میزان تطبیق با شرح شغل مرتب شده‌اند.  ← در حد evidence UI
این دستیار بهترین کاندیدا را برای شما انتخاب کرده است. ← نامعتبر
```

در copy تصمیم‌ساز، عدم‌قطعیت و امکان بررسی انسانی حفظ شود.

## مرز ادعاهای محصول

### درخواست جذب و تأیید

منابع این دو Area draft هستند. قواعد جاری مانند کفایت تأیید حداقل یک
تأییدکننده در هر مرحله، اجباری‌بودن دلیل رد، امکان ارسال مجدد و محدودیت ویرایش
گردش کار دارای dependency فعال باید با همین status استفاده شوند؛ آن‌ها را به
policy دائمی یا behavior همهٔ accountها تعمیم ندهید.

### Job Management

گروه‌های `Active`، `Internal` و `Archived` برای شغل و `In progress` و
`Rejected` برای board مشاهده شده‌اند، اما lifecycle کامل نیستند. این موارد
هنوز unknown هستند:

- transition، rejection، restoration، bulk action و history کاندیدا؛
- validation، save، persistence و recovery پنج مرحلهٔ تعریف شغل؛
- rule، threshold، audit و recovery رد خودکار؛
- eligibility، cost، moderation، synchronization و recovery انتشار؛
- permission detail اعضای تیم؛
- input، quality، explainability، bias، refresh و fallback رتبه‌بندی هوشمند.

## Routing به Product Area

| موضوع | منبع رفتار |
|---|---|
| نیاز استخدامی، approval request و fulfillment | `cando.ats.recruitment-request` |
| ساختار، scope، step و progression تأیید | `cando.ats.approval-workflow` |
| تعریف شغل، انتشار و board مشاهده‌شده | `cando.ats.job-management` |
| Candidate Management فراتر از scope مشاهده‌شده | Area مستندنشده |
| حساب، role و permission | Area مستندنشدهٔ Organization and Access |

اگر Area مستند نشده یا answer آن unknown است، copy نباید behavior را بسازد.

## Pattern، Component و Localization

ATS Context همراه pattern و component contract مشترک استفاده می‌شود:

- submit، approval، rejection یا publication consequential → Confirmation؛
- validation و failure → Error؛
- نتیجهٔ کوتاه و تأییدشده → Notification؛
- ranking و automation → AI Content and Disclosure؛
- action label → Button؛
- field requirement → Instructions و Text Input.

تعداد ظرفیت، تعداد کاندیدا، تاریخ، شناسه، نام فرد و عنوان شغل باید طبق
Localization format و isolate شوند.

## قرارداد قطعی

### باید

- سازمان، کاندیدا و کارجوی JobVision را مطابق concept نام ببرید.
- شغل ATS، آگهی شغلی و موقعیت شغلی را جدا نگه دارید.
- درخواست جذب را از درخواست شغلی و جذب را از استخدام تفکیک کنید.
- مرحلهٔ تأیید را از مرحلهٔ جذب جدا کنید.
- status منبع و محدودیت scope مشاهده‌شده را در ادعاها حفظ کنید.
- پیش از نوشتن behavior، Product Area مالک را load کنید.
- pattern، component و localization مشترک را به ارث ببرید.

### نباید

- `pipeline` را label عمومی کنید.
- رتبه‌بندی رزومه را «دستیار هوشمند»، تصمیم استخدام یا تضمین تناسب بنامید.
- از action مشاهده‌شده permission استنتاج کنید.
- گروه‌های مشاهده‌شده را lifecycle کامل اعلام کنید.
- transition، رد خودکار، انتشار یا sync cross-product را اختراع کنید.
- رابطهٔ یک‌به‌یک میان درخواست جذب، شغل ATS و آگهی شغلی بسازید.

## موارد باز

- role nameها، permission matrix و inheritance؛
- Candidate Management مستقل؛
- lifecycle کامل شغل و کاندیدا؛
- رابطهٔ شغل ATS با درخواست جذب، ظرفیت و fulfillment؛
- workflow matching، fallback، activation و notification؛
- publication-channel contract؛
- automatic-rejection contract؛
- AI-ranking contract؛
- mapping با JobVision Candidate و Employer.
