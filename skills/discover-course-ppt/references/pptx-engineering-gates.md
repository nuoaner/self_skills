# PPTX engineering gates

This course skill uses three independent delivery gates.

## Gate A: teaching semantics

Use the existing course rules to verify knowledge coverage, concept explanation, diagram semantics, arrow meaning, data/source traceability, speaker notes, and teacher-template fit.

## Gate B: file engineering

Before final delivery, run all of the following:

```bash
python scripts/pptx_content_audit.py output.pptx --strict-notes
python scripts/pptx_font_preflight.py output.pptx
python scripts/validate_course_ppt.py output.pptx --mode formal --original assets/teacher-course-template.pptx
```

When the deck was not derived from the bundled teacher template, point `--original` to the actual source template. When the deck was built from scratch, omit `--original`.

The course validator now includes a package-integrity audit. Structural errors introduced by the generated deck are formal-delivery failures.

## Gate C: rendered appearance

Render the latest PPTX after all edits. Inspect every slide. Fix clipping, accidental overlap, weak contrast, broken alignment, floating connectors, footer/source collisions, bad image crops, large accidental blank zones, and unreadable text.

After any XML-level or template-structure edit, run Gate B again before re-rendering.

## Template inventory

Before mapping course content onto a teacher or customer template, create a slide inventory:

```bash
python scripts/pptx_template_inventory.py template.pptx --markdown template-inventory.md --json template-inventory.json
```

Use the inventory to identify mature slide archetypes first. Prefer a matching existing archetype over inventing a new card layout.

## Failure priority

Fix in this order:

1. semantic errors;
2. file/package errors;
3. visual defects.

A visually attractive slide cannot compensate for a wrong relationship or a structurally fragile PPTX package.
