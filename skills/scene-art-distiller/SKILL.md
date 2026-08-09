---
name: scene-art-distiller
description: Transform a user-supplied photograph into an original editorial illustration or conceptual zine artwork that preserves the source semantic nucleus and emotional meaning while removing all photographic pixels from the final image. Use when users want a photo reinterpreted as an original art poster, expressive illustration, abstract editorial artwork, or conceptual visual. Do not use when the user wants the real photograph preserved; use scene-paper-collage instead.
---

# Scene Art Distiller

Turn a photograph into a new artwork, not a styled photo. The source is semantic evidence and visual inspiration only.

## Core Rules

- Preserve meaning, not pixels.
- The final image must contain original illustration, paper, ink, color, and typography only.
- Never reproduce, embed, crop, trace, collage, or retain photographic pixels or photorealistic regions.
- Preserve the semantic nucleus, two to four source anchors, and one meaningful spatial relationship.

## Workflow

1. Build a Distillation Card using `references/distillation-framework.md`.
2. Define one artistic proposition, one central tension, and one source-derived visual metaphor.
3. Recompose using `references/composition-system.md`.
4. Choose color behavior using `references/color-system.md`.
5. Decide typography using `references/typography.md`.
6. Generate the artwork.
7. Check against `references/quality-gate.md`; regenerate once only for hard failures.

## Expression Chain

Use internally:

source fact → emotional residue → artistic proposition → visual metaphor → formal embodiment → interpretive opening

Avoid generic mood labels without visible design consequences.

## Color Modes

Default: one purposeful high-chroma accent hue.

Exact trigger:

`单色块模式`

When triggered, use exactly one contiguous saturated color field plus neutral ink and paper tone. Do not create multiple color regions.

## Hard Avoids

Avoid photo fragments, traced images, generic surreal symbols, arbitrary decoration, multiple bright hues, fake 3D depth, glossy mockups, commercial CTA layouts, and watermarks.

## Resources

- `references/distillation-framework.md`
- `references/composition-system.md`
- `references/color-system.md`
- `references/typography.md`
- `references/quality-gate.md`
