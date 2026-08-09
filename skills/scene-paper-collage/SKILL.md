---
name: scene-paper-collage
description: Transform a user-supplied photograph into a source-faithful editorial paper-collage or zine poster that keeps real photographic material visible while extending the scene with simplified illustration, active negative space, one structurally useful accent hue, tactile torn-paper transitions, and restrained typography. Use when the user asks for a photo-based zine, paper collage, torn-paper poster, mixed photo-and-illustration artwork, editorial photo treatment, or a brand/social visual that should still visibly preserve the original photograph. Do not use when the final artwork must contain no photographic pixels; use scene-art-distiller instead.
---

# Scene Paper Collage

Turn a supplied photograph into a calm, tactile, source-aware paper poster. Keep the photograph as factual evidence and let illustration, paper, color, and type reorganize attention around it.

## Core Contract

Preserve the scene before styling it. The result must still read as the supplied photograph, while the surrounding design feels authored rather than templated.

Resolve conflicts in this order:

1. Preserve the core subject and key spatial relationship.
2. Keep retained photographic regions truthful and recognizable.
3. Simplify visual clutter aggressively before adding design detail.
4. Let illustration occupy a meaningful field, not a decorative corner.
5. Make one added hue perform a compositional job.
6. Keep negative space active and intentional.
7. Make the main photo-to-paper handoff materially legible.
8. Keep typography subordinate unless the user explicitly makes text primary.

## Source Requirement

A source photograph is required. If no usable image is present in the conversation, ask the user to upload one before generating or editing.

Follow the host platform's image-safety, consent, privacy, and post-generation response requirements. Never override them from this skill.

## Capability Rule

When native image generation or image editing is available, generate the artwork by default. If no image-generation capability is available, return a production-ready generation prompt and composition specification instead.

Do not expose hidden analysis or the full generation prompt unless the user asks for it.

## Workflow

1. Inspect the source and build a compact Scene Card using `references/scene-analysis.md`.
2. Identify the semantic minimum: the smallest set of subjects and relationships that makes this scene itself.
3. Choose what stays photographic and what becomes illustration.
4. Choose one primary illustration grammar and simplify dense detail using `references/composition-and-abstraction.md`.
5. Establish the main paper handoff, material texture, and one structural accent hue using `references/color-and-material.md`.
6. Decide whether text is needed. Apply `references/typography.md` only when text contributes to the composition or the user supplies copy.
7. Compile one decisive image-generation instruction set from visible outcomes only.
8. Generate or edit the image.
9. Run `references/quality-gate.md`. Regenerate at most once, and only for a specific observed failure.

## Composition Defaults

Treat these as starting ranges, not quotas:

- Keep the photographic anchor around 25-55% of the poster.
- Let the illustration field influence roughly 45-70% of the canvas while leaving much of that field unprinted.
- Prefer one dominant illustration mass, one or two supporting gestures, and one restrained texture field.
- Use a portrait 3:5 poster by default unless the source orientation or user request clearly calls for another ratio.
- Preserve directional breathing room in front of a gaze, path, wave, vehicle, shoreline, or strong diagonal.

Read `references/composition-and-abstraction.md` whenever foliage, crowds, architecture, repeated texture, or other dense detail must be simplified.

## Color and Material Defaults

Use one added high-chroma hue as structure, not decoration. The hue should redirect attention, bridge photo and illustration, clarify figure-ground, or counterbalance visual weight.

The primary photo-paper boundary should feel physically made: irregular torn fibers, exposed paper tone, dry ink, broken emulsion, or another flat scanned material transition. Avoid fake 3D paper depth.

Read `references/color-and-material.md` before choosing the accent hue or edge treatment.

## Typography Defaults

If the user supplies exact wording, preserve it exactly. If no wording is supplied, text is optional.

When authoring text inside the generated image, prefer one short line or fragment and keep it visually subordinate. If exact spelling is business-critical, recommend adding the final text after image generation rather than relying on the image model.

Read `references/typography.md` for language, length, placement, and material guidance.

## Prompt Compiler

Compile the visible generation instructions in this order:

1. Canvas, attention geometry, and photo/illustration allocation.
2. Core subjects and spatial invariants that must remain recognizable.
3. Illustration grammar, retain/merge/omit decisions, and negative-space plan.
4. Accent hue, source-derived shape, visual function, and material behavior.
5. Torn-paper or printed transition behavior.
6. Optional exact text, hierarchy, placement, and print treatment.
7. Reproduction texture, mood, and hard avoids.

State what must disappear as clearly as what must remain.

## Correction Rule

Allow at most one targeted regeneration. Correct only the observed failure, such as:

- scene identity loss;
- over-literal or over-detailed illustration;
- weak or generic photo-to-paper transition;
- decorative rather than structural color;
- damaged photographic fidelity;
- overcrowding or insufficient negative space;
- incorrect, dominant, or illegible text.

Do not keep iterating for subjective micro-improvements.

## Hard Avoids

Avoid generic scrapbook decoration, random stickers, tape, arbitrary dots, detached bright rectangles, multiple competing accent hues, literal full-scene tracing, dense leaf-by-leaf rendering, polished vector cartoon style, fake depth, heavy drop shadows, curled paper, glossy mockups, commercial ad clutter, large CTA typography, invented logos, and watermarks.

## Output Contract

Honor the host image tool's delivery contract. When accompanying text is allowed, keep it brief: one short creative rationale explaining the central source-derived composition decision and the structural role of the accent color.

## Resources

- `references/scene-analysis.md` - Build the Scene Card and identify source invariants.
- `references/composition-and-abstraction.md` - Allocate photo/illustration space, simplify dense detail, and choose illustration grammar.
- `references/color-and-material.md` - Choose the accent hue, paper behavior, edge treatment, and scan texture.
- `references/typography.md` - Decide whether text belongs, then control wording, hierarchy, and placement.
- `references/quality-gate.md` - Verify the result and choose a single targeted correction when needed.
