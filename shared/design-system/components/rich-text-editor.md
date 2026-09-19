---
id: design-system.component.rich-text-editor
collection: design-system
type: component
title: Rich Text Editor
summary: Rich Text Editor captures formatted multiline content through the shared Field contract and an internal formatting toolbar.
knowledge_state: verified
document_maturity: draft
related:
- design-system.component.textarea
- design-system.accessibility.forms
- design-system.accessibility.component-authoring-contract
design_status: ready-for-dev
design_maturity: handoff-ready
---

# Rich Text Editor

## Purpose

Rich Text Editor captures multiline content that requires inline or paragraph-level formatting.

It is a separate public component from Textarea.

Textarea is for plain multiline text and should preserve native `<textarea>` behavior. Rich Text Editor owns a formatting toolbar, selection-aware formatting actions, and richer editing semantics that require a dedicated editor implementation.

Both components reuse the shared Field contract for Label, Required, Info, supporting content, validation, RTL treatment, semantic colors, and focus/error composition.

## When to Use

Use Rich Text Editor when users need to format authored content, for example:

- longer descriptions with emphasis;
- formatted internal notes;
- template or message content;
- content that needs lists, alignment, or explicit text direction.

Use Textarea when plain multiline text is sufficient.

## Canonical Figma API

Component set: `Rich Text Editor`

Figma node: `22852:131093` in `-DS--Job-Vision-NEXT`.

### Variant axes

| Property | Values |
|---|---|
| `State` | `Default`, `Hover`, `Focus`, `Error`, `Error focus`, `Disabled` |
| `Toolbar` | `Compact`, `Expanded` |
| `Supporting` | `Hidden`, `Visible` |

Default: `State=Default, Toolbar=Compact, Supporting=Hidden`.

The current matrix contains 24 variants.

### Top-level authoring properties

| Property | Behavior |
|---|---|
| `Show label` | Shows/hides the shared Field label row |
| `Filled` | Figma-only content condition; False shows Placeholder, True shows Content |
| `Placeholder` | Placeholder copy |
| `Content` | Plain sample content used for Figma authoring |

`Filled` is a Figma authoring convenience, not a runtime state or required code prop.

The `Content` text property is only a representation of editor content in Figma. It does not encode rich-text spans, marks, links, list structure, document JSON, or HTML.

### Contextual nested properties

`Field label` exposes the shared:

- `Label`
- `Required`
- `Show info`

Supporting content is contextual:

- non-error + `Supporting=Visible` → shared Helper/Count row
- Error / Error focus → required Error row; Count may also be shown

Error content remains required even when the `Supporting` axis is `Hidden`.

## Anatomy

```text
Rich Text Editor
├── Field label
├── Editor
│   ├── Rich Text Toolbar
│   ├── Divider
│   └── Editable area
│       ├── Placeholder
│       └── Content representation
└── Supporting content
    ├── Helper / Count
    └── Error / Count
```

Focus and validation styling belong to the complete Editor shell, not only the editable body.

## Geometry

Default width: `520px`.

Shared editor geometry:

- radius → `6px`
- body padding → `16px`
- body typography → shared Textarea body style, currently Vazirmatn Regular `14/20`
- toolbar/body divider → `1px`
- editable-body baseline height → `160px`

### Compact toolbar

```text
40 toolbar
+ 1 divider
+ 160 body
= 201px Editor shell
```

With visible Label and no supporting row, the default outer height is `225px`.

### Expanded toolbar

```text
81 toolbar
+ 1 divider
+ 160 body
= 242px Editor shell
```

With visible Label and no supporting row, the default outer height is `266px`.

A visible supporting row adds `24px` to the outer field geometry.

### Resizing

The Figma instance may be resized horizontally and vertically.

On vertical growth:

- Label height remains fixed;
- Toolbar height remains fixed;
- Supporting height remains fixed;
- Editable area absorbs the additional height.

On horizontal growth, Toolbar, Editable area, supporting content, border, and focus indicator all stretch with the Editor.

## State Model

### Default

- Editor surface → `surface/default`
- shell line → `line/default`
- Content → `fg/primary`
- Placeholder → `fg/placeholder`

### Hover

- shell line → `line/emphasis`
- geometry remains unchanged.

### Focus

```text
Editor line → line/emphasis, 1px
Focus indicator → focus/default, 2px outside
```

The focus indicator wraps the complete Editor shell.

### Error

```text
Editor line → line/error, 2px
Error message → fg/error
Programmatic invalid state → required in implementation
```

The 2px error line is visual overlay geometry and must not shift content.

### Error focus

Error and focus remain independently visible:

```text
Editor line → line/error, 2px
Focus indicator → focus/default, 2px outside
Error message → fg/error
```

### Disabled

Disabled applies to the complete editor:

- Editor surface → `surface/disabled`
- line → `line/disabled`
- content → `fg/disabled`
- Toolbar controls → Disabled Icon Button state
- Toolbar dividers → `line/disabled`

## Internal Rich Text Toolbar

Internal component set: `_Rich Text Toolbar`

Figma node: `22848:1282`.

The toolbar is intentionally internal in v1. It is part of the Rich Text Editor contract, not a separately published general-purpose toolbar.

### Toolbar axes

| Property | Values |
|---|---|
| `Layout` | `Compact`, `Expanded` |
| `State` | `Enabled`, `Disabled` |

The toolbar has four variants.

Formatting-active state is owned by each nested Icon Button and is not multiplied into Toolbar variants.

### Compact

One `40px` row containing:

- Bold
- Italic
- Underline
- Strikethrough
- Bulleted list
- Numbered list
- Undo
- Redo
- Overflow

The toolbar uses canonical `Icon Button / Default` → `Ghost / Small`.

### Expanded

Expanded adds a second `40px` row separated by a `1px` divider.

The second row contains:

- Align right
- Align center
- Align left
- Align justify
- RTL text direction
- LTR text direction

Expanded toolbar height: `81px`.

For the RTL-first default presentation, Align right and RTL direction are shown as active examples.

### Intentionally excluded from the general v1 toolbar

The previous CanDo toolbar included product/editor-specific controls that are not carried into the shared v1 contract:

- Add Token / Parameter;
- Font family;
- raw pixel Font size.

Add Token is CanDo-specific product behavior.

Font family should not bypass the product typography/theme contract.

Raw font-size selection should not be introduced until the design system defines a semantic rich-text style model such as paragraph/heading styles.

Indentation and additional editor actions may be added only when validated by shared product needs.

## RTL

The component is RTL-first for current JobVision/Cando products.

Toolbar groups are ordered from the RTL starting edge.

Current primary-row visual order from right to left:

```text
Character formatting
→ Lists
→ History
→ Overflow
```

Expanded secondary row begins with alignment controls at the RTL start edge, followed by text-direction controls.

Mixed-direction editor content must not change the structural meaning of toolbar position.

Text direction is a content-formatting action, not a layout-direction switch for the Design System component itself.

## Formatting State

Active formatting belongs to individual toolbar controls.

Examples:

- Bold active when selection/caret is inside bold content;
- List active when the current block is in that list type;
- alignment action active for the current paragraph;
- text direction active for the current paragraph/selection.

Do not introduce toolbar-level variants for every possible formatting combination.

Figma examples may override nested Icon Button `State=Active` to represent selection formatting.

## Behavior Boundary

The Design System owns:

- Editor shell anatomy;
- toolbar grouping and visual hierarchy;
- toolbar control visual states;
- shared Field integration;
- focus/error/disabled visuals;
- sizing and responsive geometry;
- formatting-action affordances.

The consuming editor implementation owns or must define:

- actual rich-text document model;
- selection and caret behavior;
- command execution;
- keyboard shortcuts;
- paste/sanitization behavior;
- output format such as HTML, JSON, or Markdown;
- undo/redo history semantics;
- link editing, if added;
- paragraph/block-style model, if added.

Do not infer a specific editor framework from Figma.

## Accessibility

Rich Text Editor is not a native Textarea and requires an explicit accessibility contract in implementation.

### Editable region

Implementation should use an editor framework or editable primitive that preserves:

- meaningful accessible labeling;
- keyboard text editing;
- selection/caret access;
- screen-reader-compatible content semantics;
- invalid/disabled relationships as applicable.

### Toolbar

Every toolbar action requires:

- an accessible name independent of the icon;
- keyboard operability;
- exposed pressed/active state when the formatting command is active;
- predictable focus movement;
- a strategy that does not accidentally destroy the editor selection when toolbar actions are used.

Undo/Redo and unavailable actions must expose disabled state when applicable.

### Focus

Visible focus must remain clear for both:

- the Editor/editable area;
- individual toolbar controls during keyboard navigation.

The Editor shell focus treatment must not be used as a substitute for focused-button indication inside the Toolbar.

### Error

Error must include:

- textual error content;
- programmatic invalid state or equivalent editor semantics;
- visible Error styling;
- independent visible focus.

## QA Checklist

Verify:

- exactly 24 public variants exist;
- default is Default / Compact / Hidden;
- Compact toolbar is 40px;
- Expanded toolbar is 81px;
- editable-body baseline is 160px;
- body padding is 16px;
- Filled preserves Placeholder and Content independently;
- Compact/Expanded switches preserve editor content;
- Supporting Visible adds helper/count geometry without shrinking body;
- Error always retains Error content;
- Error focus preserves both Error and Focus;
- Disabled disables editor and all toolbar controls;
- active toolbar formatting can be represented through nested Icon Button state;
- horizontal resizing stretches toolbar, body, border, focus, and supporting rows;
- vertical resizing grows only the editable body;
- hiding the visual label leaves the Editor usable only when another accessible-name mechanism exists;
- toolbar group order remains correct in RTL;
- formatting actions do not require combinatorial toolbar variants.

## Figma Reference

Canonical source:

- Figma file: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Text area`
- Page node: `5564:279849`
- Section: `HOS-16 / Canonical Rich Text Editor`
- Section node: `22846:128110`
- Rich Text Editor set: `22852:131093`
- Internal Toolbar set: `22848:1282`
- Examples: `22854:2962`
- Documentation frame: `22854:2959`

Migration references:

- old CanDo Text toolbar reference: file `8CZOoFsYpENfaNx2WoDqIp`, node `16057:535700`
- legacy NEXT `_Text area toolbar`: `13562:307390`
- legacy NEXT `Text area with toolbar`: `13562:307473`

Legacy components are migration references only and are not the canonical contract.

## Runtime / Storybook Status

No runtime editor package or Storybook implementation is currently registered as canonical for Rich Text Editor.

Do not infer:

- editor framework;
- Angular API;
- DOM/contenteditable structure;
- serialization format;
- command API;
- keyboard shortcut implementation.

## Open Items

Before runtime contract is finalized:

- select or register the canonical editor implementation/framework;
- define the rich-text value/output model;
- define toolbar keyboard-navigation and selection-preservation behavior;
- decide whether Link is required in the shared toolbar or belongs in Overflow/product configuration;
- define semantic paragraph/heading styles before adding typography controls;
- decide whether indentation is a shared toolbar action;
- define paste/sanitization rules;
- confirm loading/read-only behavior if real product use cases require first-class states;
- register Storybook and browser accessibility tests.

These open items do not block the current visual and Figma-authoring contract.

## Related Documents

- `./textarea.md`
- `./text-input.md`
- `../accessibility/forms.md`
- `../accessibility/component-accessibility-authoring-contract.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
