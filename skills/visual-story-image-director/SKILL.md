---
name: visual-story-image-director
description: Use when an existing photo, reference image, or described scene should become a story-driven visual asset through deliberate art direction. Trigger on requests to reinterpret ordinary photos as editorial, zine, collage, poster, social-cover, brand-story, travel-memory, lifestyle, or narrative images while preserving important subjects and scene facts. Also use for production-ready image prompts or edit briefs grounded in a source scene. Do not use for full WeChat article image planning; use wechat-article-image-planner instead.
---

# Visual Story Image Director

Turn a source scene into a usable visual story. Preserve the factual layer first, then add design language that supports the intended use.

Read `references/visual-analysis-framework.md` when diagnosing the source image, choosing what to preserve, or selecting a visual direction. Read `examples/window-side-summer-afternoon.md` when a concrete portrait-to-editorial example is useful. `examples/travel-memory-case.md` is a second lightweight example.

## Core Rules

1. **Facts before style.** Separate what is visibly true from what is optional creative interpretation.
2. **Preserve identity anchors.** Keep the people, objects, relationships, setting cues, and emotional signals that make the source recognizable.
3. **Give style a job.** Choose a visual language because it helps the intended use, not because it is fashionable.
4. **Direct, do not filter.** Recompose hierarchy, rhythm, texture, framing, and narrative emphasis instead of merely applying a surface style.
5. **Borrow principles, not implementation.** When external work inspires the approach, independently rewrite the workflow, prompts, examples, and terminology for this repository. Do not copy another Skill's prose, prompt blocks, examples, or file structure.

## Workflow

### 1. Establish the Scene Truth

Identify:

- primary subject
- supporting subjects and objects
- spatial relationships
- lighting and environment
- visual anchors that must survive
- emotional residue already present in the source

Split findings into:

- **Must preserve**: losing these changes the identity or meaning of the scene.
- **May reinterpret**: palette, texture, crop, graphic devices, paper treatment, framing, secondary background details.
- **Do not invent**: details that would create false identity, location, event, product, or relationship claims.

### 2. Define the Communication Goal

Write one sentence that states what the finished image should make the viewer notice or feel.

Examples:

- "Turn a quiet summer portrait into an intimate independent-magazine page."
- "Turn a travel snapshot into a memory-led editorial composition without losing place cues."
- "Turn a product-in-use photo into a brand-story visual that still reads as the same product and setting."

### 3. Choose One Primary Visual Language

Select one dominant direction first. Add variants only when the user asks to explore.

Useful families include:

- editorial zine / paper collage
- refined magazine layout
- cinematic still
- graphic poster
- tactile scrapbook / memory journal
- restrained brand narrative

Describe the direction using design decisions, not creator imitation. Prefer terms such as material, composition, texture, typography treatment, lighting, color behavior, and spatial rhythm.

### 4. Build the Generation or Edit Brief

Always define:

- **Subject**: who or what stays central
- **Composition**: crop, hierarchy, negative space, layering, perspective
- **Visual language**: materials, texture, graphic devices, photographic or illustrative behavior
- **Lighting and color**: what remains from the source and what may shift
- **Mood**: intended emotional tone
- **Preservation constraints**: identity, pose, objects, setting cues, product details
- **Avoid list**: unwanted additions, distortions, fake text, over-decoration
- **Usage format**: cover, poster, feed post, story, article image, presentation, etc.
- **Aspect ratio**: choose for the destination surface

If an image-generation or image-editing tool is available and the user asks for generation, use it. If not, return a production-ready prompt and edit brief without pretending an image was generated.

### 5. Run Visual QA

Reject or revise output when any of these fail:

- **Recognition**: the important subject or memory no longer reads as the same scene.
- **Narrative**: the added design language does not strengthen a clear story.
- **Coherence**: decorative elements compete with the focal point.
- **Utility**: the composition does not fit the requested channel or aspect ratio.
- **Integrity**: invented details imply facts not present in the source.
- **Craft**: faces, hands, product details, text-like marks, edges, or collage layers show distracting artifacts.

## Output Contract

Return, in this order:

1. **Scene diagnosis** — 2-5 bullets.
2. **Must preserve** — the identity and meaning anchors.
3. **Art direction** — one primary concept with a short rationale.
4. **Generation/edit brief** — production-ready, tool-agnostic instructions.
5. **Avoid list** — explicit failure modes.
6. **Format recommendation** — aspect ratio and destination use.
7. **QA checklist** — what to inspect after generation.

When the user asks for multiple directions, provide at most three meaningfully different concepts before generating.

## Boundaries

- Use `wechat-article-image-planner` when the task is to plan a finalized WeChat article's entire cover/inline/poster system.
- Do not turn this into a generic prompt-polishing Skill; the defining work is visual diagnosis and art direction grounded in a scene.
- Do not claim to preserve exact likeness or product geometry unless the available image tool can actually support that level of edit fidelity.
- Do not imitate a named living artist or copy a specific copyrighted composition; translate the request into high-level visual attributes instead.
