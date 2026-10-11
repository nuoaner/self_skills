---
name: slides-production-engine
description: Reliable PowerPoint engineering and QA for .pptx creation, template reuse, editing, and final delivery. Use when a presentation needs robust template analysis, package-integrity checks, content-placeholder audits, font preflight, regression-aware validation against an original template, or a formal three-layer QA gate covering semantic intent, file structure, and rendered appearance. This skill complements slide-authoring workflows; it does not replace domain-specific teaching, brand, or narrative rules.
---

# Slides Production Engine

Use this skill as the engineering QA layer around presentation authoring. Keep domain and brand rules in the domain skill; keep package integrity, template inventory, content hygiene, font risk, and delivery gates here.

## Core contract

A presentation is complete only after three independent gates pass:

1. Semantic gate: the intended content, relationships, data, and sources are correct.
2. File-engineering gate: the PPTX package is internally consistent and template edits did not introduce new structural defects.
3. Visual gate: rendered slides have no clipping, accidental overlap, broken alignment, unreadable text, or unbalanced composition.

Do not treat successful generation or a successful LibreOffice render as proof that PowerPoint package structure is sound.

## Required workflow

### 1. Inventory a template before using it

For any supplied template or reference deck, run:

```bash
python scripts/pptx_template_inventory.py template.pptx --markdown template-inventory.md --json template-inventory.json
```

Use the inventory to map content to existing layouts and slide archetypes before creating custom layouts. Prefer reuse of a mature template pattern when it can express the content accurately.

### 2. Author or edit the deck

Use the presentation authoring tool selected by the active slide workflow. Preserve the source template's page size, theme intent, layout grammar, typography, and recurring decorations unless the user explicitly requests a redesign.

### 3. Run content hygiene checks

```bash
python scripts/pptx_content_audit.py output.pptx
```

For formal delivery, resolve placeholder text, empty slides, accidental duplicate titles, and missing notes when notes are required by the domain skill.

### 4. Run font preflight

```bash
python scripts/pptx_font_preflight.py output.pptx
```

Treat the result as a QA-environment signal, not a promise about the user's Office installation. If an important font is substituted, leave additional text-fit slack and visually inspect affected slides carefully.

### 5. Run PPTX package audit

For a deck created from scratch:

```bash
python scripts/pptx_package_audit.py output.pptx
```

For a deck derived from a template:

```bash
python scripts/pptx_package_audit.py output.pptx --original template.pptx
```

The `--original` mode baselines inherited structural issues and reports only new regressions as failures while still surfacing inherited issues separately.

### 6. Render and inspect every slide

Render the final PPTX to images with the active slide-rendering workflow. Inspect every slide after the latest change. Re-run package audit after any XML-level or template-structure edit.

## Template reuse policy

Use this decision order:

1. Reuse an existing template slide/layout when it expresses the relationship correctly.
2. Adapt an existing layout while preserving its visual grammar.
3. Create a new layout only when the existing template cannot express the content without semantic distortion.

Do not force source content into a fixed number of template slots. Remove unused slot groups completely instead of leaving empty decorative shells.

See `references/template-reuse.md`.

## Package audit scope

The package auditor checks, at minimum:

- ZIP/package readability and required top-level parts.
- XML parseability.
- duplicate relationship IDs.
- broken internal relationship targets.
- presentation slide IDs and slide relationship mapping.
- exactly one slide-layout relationship per slide.
- notes-slide reuse across multiple slides.
- content-type coverage for package parts.
- chart axis IDs that appear structurally suspicious.
- baseline regressions when `--original` is supplied.

This is a structural guardrail, not a full Microsoft Office conformance suite.

See `references/three-layer-qa.md`.

## Content audit scope

The content auditor flags common leftovers such as Lorem Ipsum, TODO markers, generic insert placeholders, repeated titles, and effectively empty slides. Domain skills may allow explicit placeholders such as `TBD` or `pending source`; use `--allow` to whitelist deliberate markers.

## Font preflight policy

Do not enforce one universal font whitelist. Instead:

- report explicit font families present in the package;
- compare them with the current QA environment when fontconfig is available;
- mark substitutions as risk signals;
- keep extra fit margin when the QA renderer substitutes a font;
- preserve user- or brand-required fonts when requested.

See `references/font-preflight.md`.

## Delivery gate

Before delivery, require:

- semantic/domain validator passes;
- `pptx_content_audit.py` has no unresolved formal-delivery issues;
- `pptx_package_audit.py` has no new structural errors;
- the latest render has been inspected slide by slide;
- any font substitutions relevant to text fit have been reviewed.

If a domain skill has stricter rules, the stricter rule wins.
