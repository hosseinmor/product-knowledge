---
id: design-system.handoff.component-token-changes-storybook-2026-10-20
collection: design-system
type: development-handoff
title: Karbon Component Token Changes — Storybook Handoff
summary: Implementation deltas from the October 2026 token audit, separated from Figma-only variable bindings; intended for Angular/Storybook owners.
knowledge_state: verified
document_maturity: implementation-ready
design_status: implementation-pending
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.file-uploader
  - design-system.component.chip
  - design-system.component.progress-bar
  - design-system.component.select
  - design-system.component.button
  - design-system.component.dialog
  - design-system.component.table
---

# Karbon — تغییرات کامپوننت‌ها برای پیاده‌سازی در Storybook

**تاریخ:** ۲۰ اکتبر ۲۰۲۶  
**مخاطب:** توسعه‌دهندگان Angular / Tailwind / Storybook  
**مبنا:** تصمیم‌ها و تغییرات ثبت‌شده در ممیزی توکن‌های Design System در ۱۹–۲۰ اکتبر ۲۰۲۶  
**وضعیت:** تغییرات Design اعمال شده‌اند؛ تطبیق با پیاده‌سازی فعلی و تست Storybook هنوز انجام نشده است.

> **این سند لیست کار توسعه است، نه گزارش عملیات فیگما.** «قبل» و «بعد» به **قرارداد طراحیِ قبل و بعد از ممیزی** اشاره دارند، نه لزوماً مقدار موجود در سورس Storybook. توسعه‌دهنده ابتدا پیاده‌سازی فعلی را بررسی کند؛ هر موردی که از قبل با قرارداد جدید سازگار است، نیازی به تغییر کد ندارد.

## ۱. تغییرات لازم در ظاهر یا Semantic Style

این بخش **اولویت اصلی پیاده‌سازی** است. تغییرات زیر بر خروجی کامپوننت یا نقش معنایی رنگ/تایپوگرافی اثر دارند.

| شناسه | کامپوننت / بخش / State | قبل از ممیزی طراحی | قرارداد جدید برای Storybook | نوع تغییر |
|---|---|---|---|---|
| FU-01 | **File Uploader / File Item** — همهٔ Stateها | پس‌زمینهٔ \`surface/neutral-muted\` | **\`surface/muted\`**؛ آیتم صرفاً ارائه‌دهندهٔ فایل/وضعیت است و کل بدنه یک کنترل تعاملی خنثی نیست | Color / تغییر بصری |
| FU-02 | **File Uploader / File Item** — همهٔ Stateها | \`border-radius: 4px\` | **Radius/Medium = 6px** | Radius / تغییر بصری |
| FU-03 | **File Uploader / File Item / Error** — پیام خطای کوتاه | \`fg/error\` | **\`fg/primary\`** برای متن اصلی پیام؛ آیکون و Border همچنان \`fg/error\` و \`line/error\` هستند | Color / کنتراست |
| FU-04 | **File Uploader / File Item / Error** — توضیح طولانی | \`fg/error\` | **\`fg/secondary\`** برای توضیح تکمیلی؛ آیکون و Border همچنان Error باقی می‌مانند | Color / کنتراست |
| FU-05 | **File Uploader / Dropzone / Disabled** — متن راهنما | رنگ قدیمی/ارجاع نامشخص | **\`fg/disabled\`** | Color / یکپارچگی |
| FU-06 | **File Uploader / Dropzone / Focus** | Border با \`line/accent\` و ضخامت ۲px، بدون Focus ring مستقل | **Border یک‌پیکسلی \`line/emphasis\` + Focus ring استاندارد \`focus/default\` با ضخامت ۲px و فاصلهٔ ۱px از Border** | Focus / تغییر بصری و تعاملی |
| CH-01 | **Chip / Selectable** — Selected + Disabled | \`surface/surface-selected-disabled\` | **\`surface/disabled\`** | Color / به‌ویژه Dark |
| CH-02 | **Chip / Removable** — Disabled | \`surface/surface-selected-disabled\` | **\`surface/disabled\`** | Color / به‌ویژه Dark |
| CH-03 | **Chip / Disclosure** — Applied + Disabled | \`surface/surface-selected-disabled\` | **\`surface/disabled\`** | Color / به‌ویژه Dark |
| PB-01 | **Progress Bar / Success** — متن وضعیت تکمیل | \`fg/secondary\` | **\`fg/success\`**؛ Track از قبل باید \`line/success\` و Error از \`line/error\` استفاده کند | Color / تغییر بصری |
| SE-01 | **Select / Option** — Metadata | فونت Regular، **۱۲px / ۱۸px** | **\`Label/XS\` = ۱۲px / ۱۶px، Medium 500** | Typography / وزن و ارتفاع خط |
| SE-02 | **Select / Option** — Secondary text | فونت Regular، **۱۲px / ۱۸px** | **\`Body/Compact/XS\` = ۱۲px / ۱۶px، Regular 400** | Typography / ارتفاع خط |
| SE-03 | **Selection Panel / Title** | **۱۴px SemiBold** با ارتفاع خط Auto | **\`Heading/SM\` = ۱۴px / ۲۰px، Bold 700** | Typography / وزن و ارتفاع خط |

**توضیحات الزامی:**

- **FU-03 و FU-04:** تغییر رنگ متن خطا برای برآورده‌کردن کنتراست متن ۱۲px در Dark ضروری است. نشانهٔ خطا از روی آیکون و Border حذف نشود؛ متن توضیحی را دوباره به قرمز برنگردانید. کنتراست محاسبه‌شده روی \`surface/muted\` در Dark: \`fg/primary\` برابر **۸٫۸۳:۱** و \`fg/secondary\` برابر **۵٫۸۵:۱**.
- **FU-06:** Focus ring فقط برای Focus واقعیِ قابل‌دسترسی، به‌ویژه فوکوس کیبورد روی File Input/اکشن مرتبط، نمایش داده شود؛ Hover و Drag-over جایگزین Focus نیستند. از الگوی مشترک Focus در بقیهٔ فیلدهای Karbon استفاده شود و یک نسخهٔ سفارشیِ مستقل تعریف نشود. Ring استاندارد روی \`surface/default\` در Dark کنتراست محاسبه‌شدهٔ **۴٫۳۱:۱** دارد، اما روی \`surface/muted\` Dark به **۲٫۸۵:۱** می‌رسد؛ در این پس‌زمینه باید طرح نهایی و وضوح Focus جداگانه بررسی شود.
- **CH-01 تا CH-03:** صرفاً Stateهای یادشده اصلاح می‌شوند؛ State معمولی، Hover، Active یا Disabledهای دیگری که هم‌اکنون درست‌اند بی‌دلیل بازنویسی نشوند. این تغییر ظاهر Dark را به‌طور محسوسی اصلاح می‌کند.
- **SE-01 تا SE-03:** Option metadata و Secondary text در بعضی نمونه‌های پیش‌فرض پنهان‌اند. برای مشاهدهٔ تغییر، Story قابل‌نمایش با محتوای واقعی و متن فارسی/انگلیسی لازم است. فقط کلاس فونت کافی نیست؛ line-height و weight نیز بررسی شوند.
- **این‌ها تغییر Contract طراحی هستند**. هیچ API، Variant، نام Component، valuePolicy یا رفتار انتخاب مقدار با این ممیزی عوض نشده است.

## ۲. یکسان‌سازی مصرف Token بدون تغییر عدد یا Geometry

این موارد در فیگما به توکن‌های Foundation متصل شدند، اما **مقدار بصری جدید ندارند**. در Storybook فقط اگر هنوز مقدارها Hard-code شده‌اند یا از مسیر Token اشتباه مصرف می‌شوند، آن‌ها را به خروجی استاندارد Karbon/Tailwind منتقل کنید؛ **Spacing یا ابعاد را مجدداً طراحی نکنید**.

| کامپوننت | قرارداد فعلی که باید در کد رعایت شود | اقدام توسعه |
|---|---|---|
| **Button** | ارتفاع Sizeها: Extra Small **۲۸**، Small **۳۲**، Medium **۴۰**، Large **۴۸px**؛ Padding افقی به‌ترتیب **۸/۱۲/۱۶/۲۰px**؛ Gap واقعی آیکون و Label **۸px** | در صورت وجود مقدار مستقیم، از Spacing مشترک استفاده شود: معادل Tailwind \`px-2/3/4/5\` و \`gap-2\`؛ **بدون تغییر فاصله** |
| **Chip / Removable / Body (Edit action target)** | در RTL: Padding سمت شروع (راست) **۸/۱۲/۱۶px** به‌ازای XS/Small/Medium؛ Padding سمت پایان (چپ) **۸px**؛ Gap داخلی **۸px** | از توکن Spacing و ترجیحاً CSS logical padding استفاده شود؛ Body و دکمهٔ Remove همچنان **دو Target مستقل** باشند |
| **Progress Bar** | Gap حالت‌های **Default/Indent = ۸px**، **Inline = ۱۶px**؛ فاصلهٔ Label تا آیکون وضعیت **۱۶px**؛ Padding سمت شروع Label و Helper در **Indent = ۱۶px** | فقط اگر مقدارها Hard-coded یا متفاوت هستند، از Spacing مشترک (\`gap-2\`/\`gap-4\`) استفاده شود؛ اندازهٔ Track دست‌نخورده بماند |
| **File Uploader** | فاصله‌های مشترک فعلی از مقیاس **۲/۸/۱۲/۱۶px** مصرف شوند؛ Geometry محلی مثل **۷/۱۱/۱۵px** برای File Item و **۱۰/۵۰px** برای Dropzone فعلاً **همان‌طور حفظ شود** | اصلاح مسیر مصرف Spacing مشترک فقط در صورت نیاز؛ **گردکردن خودکار Geometry محلی ممنوع** |
| **Data Table** | Spacing فعلی Source صحیح است؛ ردیف یک‌خطی **۳۲/۴۰/۴۸px** و Padding عمودی Cell **۴/۸/۱۲px**، با رشد ارتفاع برای چندخطی؛ Divider ساختاری \`line/muted\` | **تغییر عددی جدید ندارد**. تنها هم‌خوانی با توکن‌ها و رفتار Responsive/Slot موجود را کنترل کنید |
| **Select / Autocomplete / Selection Panel** | فیلدهای تعاملی **Radius/Medium = ۶px**؛ پنل شناور **Radius/Large = ۱۲px** | Aliasهای Radius قدیمی در صورت وجود به نقش‌های استاندارد منتقل شوند؛ **هیچ تغییر اندازه‌ای لازم نیست** |
| **Dialog / Alert Dialog / Confirmation Dialog / Close Button** | Color نقش‌های عمومی از **\`surface/*\`، \`fg/*\`** و سایر خانواده‌های public Semantic مصرف شود، نه aliasهای داخلی \`semantic/*\` در مسیر Product | فقط در صورت وجود وابستگی به alias داخلی، به public Semantic map منتقل کنید؛ انتظار تغییر بصری نداریم |
| **Toggle / Field Label / Select required marker** | Typography متن‌ها در Styleهای موجود تنظیم شده؛ اندازه و وزن قبلی در اصلاحات اولیه تغییری نکرده است | اگر کد هم‌اکنون برابر Spec است، **هیچ تغییری نیاز ندارد** |

**نکتهٔ Spacing:** این لیست دستور ایجاد کلاس CSS جدید یا نام Token جدید نیست. از **نگاشت تولیدشدهٔ Design System به Tailwind 3** و کلیدهای موجود استفاده کنید. مثال \`gap-2\` برای ۸px و \`gap-4\` برای ۱۶px است، به شرط اینکه تنظیمات فعلی پروژه به مقیاس Karbon متصل باشند.

**نکتهٔ Icon Button:** \`itemSpacing=8px\` در قاب \`Start Icon\` که فقط **یک فرزند مستقیم** دارد، هیچ فاصلهٔ بصری نمی‌سازد. این مقدار در ممیزی‌های Button و Data Table منشأ گزارش‌های کاذب بود. **برای آن Spacing جدید یا تغییر UI نسازید.** اگر معماری Wrapper تغییر کند و چند فرزند بگیرد، آن‌وقت Gap را دوباره بررسی کنید.

## ۳. مواردی که در این Handoff تغییر نمی‌کنند

- **Image Uploader:** کاملاً **خارج از محدوده**؛ هیچ تغییر یا مهاجرتی درخواست نشده است.
- **Autocomplete:** ممیزی مستقیم آن بدون اختلاف بود؛ به‌جز اطمینان از مصرف درست Selection Panel مشترک، تغییر جدیدی در Storybook لازم نیست.
- **Data Table، Button، Chip و Progress Bar:** شمار زیادی از اصلاحات ممیزی فقط اتصال اعداد/رنگ‌های از قبل صحیح به توکن در فایل طراحی بودند. آن اعداد **درخواست تغییر بصری جدید نیستند**.
- **Progress Bar track و Progress Circle:** این ممیزی دستور تغییر تازهٔ مسیر Stroke ایجاد نکرده است؛ قرارداد موجود **\`line/default\`، \`line/accent\`، \`line/success\`، \`line/error\`** و Track با ضخامت **۴px Small / ۸px Big** مبنای کنترل هم‌خوانی است.
- **Legacy Paint Styles:** جایگزینی مکانیکی \`Transparent/Transparent\` و دیگر Paint Styleهای خاص با یک Fill مات ممنوع است؛ ترکیب Blend/Focus را می‌تواند خراب کند.
- **Variant/API:** هیچ تغییر تازه‌ای برای Propها، مقدار Selection، Slotها، Content stateها یا منطق Determinate/Indeterminate مصوب نشده است. پیاده‌سازی انیمیشن Indeterminate جزو این **changelog** نیست.
- **Legacy و Archive:** Number Input، Date Picker، Pagination، Structured List و کامپوننت‌های آرشیوی وارد این بستهٔ توسعه نمی‌شوند.

## ۴. پیشنهاد اجرای توسعه و Storybook QA

**گام ۱ — بررسی کد موجود:** برای هر ردیف بخش ۱، کد پیاده‌سازی و Story مربوط را با «قرارداد جدید» مقایسه کنید. اگر از قبل منطبق است، آن مورد را **Already compliant** علامت بزنید. از عبارت‌های «قبل از ممیزی» نباید وضعیت واقعی ریپوی توسعه نتیجه‌گیری کرد.

**گام ۲ — اعمال تغییرات لازم:** Color/Radius/Focus/Typography بخش ۱ را اعمال کنید. برای بخش ۲ فقط مصرف توکن را اصلاح کنید، نه Geometry. Semantic Color باید با تم‌های JobVision/Cando و Light/Dark از همان خروجی توکن مشترک resolve شود.

**گام ۳ — Storybook visual regression و تست Stateها:**

- [ ] File Item: Default/Uploading/Success/Error در Light و Dark؛ پس‌زمینهٔ \`surface/muted\`، Radius ۶، Error short/long و آیکون/Border Error.
- [ ] Dropzone: Enabled/Disabled/Focus؛ \`fg/disabled\` و Focus با ۱px \`line/emphasis\` + حلقهٔ ۲px / فاصلهٔ ۱px؛ آزمون واقعی Tab/Keyboard و پس‌زمینهٔ Dark.
- [ ] Chip: Selectable Selected+Disabled، Removable Disabled، Disclosure Applied+Disabled؛ هر سه Size و تم Dark؛ عمل مستقل Remove/Body مختل نشود.
- [ ] Progress Bar: Success و Error کنار Active و Indeterminate؛ \`fg/success\` برای پیام و نقش‌های Stroke دست‌نخورده؛ Light/Dark.
- [ ] Select / Selection Panel: Option همراه Metadata و Secondary text **نمایان**؛ عنوان پنل؛ متن طولانی فارسی/انگلیسی، line-height و wrap/overflow.
- [ ] Button/Chip/Progress Bar: Padding و Gapهای بخش ۲ با توکن مشترک باشند و Visual diff ناخواسته نداشته باشند.
- [ ] سناریوهای بالا در **JobVision × Light/Dark** و **Cando × Light/Dark** کنترل شوند. پیش از تأیید، موارد اختلاف را به‌صورت diff و Story ID گزارش کنید.

**گام ۴ — خروجی توسعه‌دهنده:** در Storybook یا PR توسعه برای هر تغییر یک توضیح کوتاه شامل **Component/State، نام توکن قبلی و جدید، Screenshot قبل/بعد و تست انجام‌شده** قرار گیرد. برای موارد بخش ۲ که از قبل صحیح‌اند، «No code change / token already compliant» ثبت شود.

## مرجع طراحی و مستندات دقیق

- [File Uploader — قرارداد نهایی](../components/file-uploader.md)، [گزارش تغییرات Color/Radius/Focus](../audits/file-uploader-token-migration-2026-10-20.md)
- [Chip — قرارداد](../components/chip.md)، [گزارش Disabled و Spacing](../audits/chip-token-compliance-2026-10-20.md)
- [Progress Bar — قرارداد](../components/progress-bar.md)، [گزارش Success و Spacing](../audits/progress-bar-token-compliance-2026-10-20.md)
- [Select — قرارداد](../components/select.md)، [Autocomplete — وضعیت بدون تغییر](../audits/autocomplete-token-compliance-2026-10-20.md)
- [Button — Spacing](../audits/button-spacing-2026-10-20.md)، [Data Table — گزارش بدون تغییر بصری](../audits/data-table-token-compliance-2026-10-20.md)
- [Spacing Foundation](../foundations/spacing.md)، [Radius Foundation](../foundations/radius.md)، [قواعد مصرف توکن در فیگما](../integrations/figma-token-compliance.md)
- [گزارش عمومی ممیزی](../audits/component-token-compliance-2026-10-19.md)

**معیار پایان این Handoff:** موارد ظاهری بخش ۱ با Story/Visual test معتبر بررسی شده، بخش ۲ بدون تغییر ناخواستهٔ Geometry با توکن مشترک منطبق شده و هیچ تغییری به Image Uploader تحمیل نشده است. این سند **صرفاً درخواست تغییر در پیاده‌سازی** است، نه تأیید اینکه Storybook هم‌اکنون به‌روزرسانی شده است.
