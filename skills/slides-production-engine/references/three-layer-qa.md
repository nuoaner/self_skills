# Three-layer QA

## 1. Semantic gate

Verify the deck says the right thing before judging appearance. Check claims, data, relationships, process direction, labels, source mapping, and domain-specific acceptance criteria.

## 2. File-engineering gate

Verify the PPTX package is coherent. Run `pptx_package_audit.py`. For template-derived work, always provide `--original` so inherited defects are separated from new regressions.

A render that looks correct does not prove the file will behave correctly in PowerPoint. Relationship, content-type, slide-layout, notes, and chart problems can survive other renderers.

## 3. Visual gate

Render the current file after all changes. Inspect every slide for clipping, overflow, unintended overlap, weak contrast, broken alignment, bad crop, uneven spacing, footer collision, and large accidental voids.

## Failure policy

- Semantic failure: fix content or diagram logic first.
- File-engineering failure: fix package/generator logic and rebuild; avoid manual patching unless the task specifically requires OOXML editing.
- Visual failure: fix layout and re-render.

Re-run all affected gates after a change. A final deck must pass all three.
