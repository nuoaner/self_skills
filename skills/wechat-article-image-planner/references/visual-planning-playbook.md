# WeChat Article Visual Planning Playbook

## Goal

Turn a finalized WeChat article into a visual system that improves click-through, reading momentum, comprehension, and sharing.

## Article Diagnosis

Classify the article before planning images:

| Article type | Visual strategy |
|---|---|
| Product experience | Show scenes, devices, before/after moments, user action. |
| Tool/tutorial | Show workflow metaphors, screenshots if supplied, step posters. |
| Opinion/analysis | Use symbolic scenes, contrast images, conceptual metaphors. |
| Case story | Show people, places, turning points, emotional beats. |
| Commercial/project intro | Show value proposition, audience pain, product maturity. |
| Technical explainer | Use clean conceptual diagrams or editorial illustrations. |

## Image Set

Minimum practical set:

1. Cover image: promises the article's core tension in one glance.
2. First inline image: appears after the hook or first major claim to keep momentum.
3. Core concept image: visualizes the most important idea.
4. Case/detail image: makes an example feel concrete.
5. Closing poster: optional, useful when the article has a strong conclusion or shareable quote.

For short articles, use cover + 1 inline image. For long articles, use cover + 3-5 inline images.

## Visual Anchor Extraction

Extract anchors in this order:

1. Concrete scenes: office, live room, street, device, chat window, dashboard.
2. Objects: token, phone, server, document, notebook, robot arm, whiteboard.
3. People: ordinary reader, operator, market manager, developer, customer.
4. Tension: expensive/cheap, old/new, human/AI, chaos/order, private/public.
5. Metaphor: station, bridge, maze, market stall, factory, observatory, theater.
6. Data: numbers, rankings, timelines, before/after.
7. Quote: only use if short and exact typography can be added after generation.

## Prompt Structure

Use this structure for every image prompt:

```text
Use case: WeChat article <cover/inline/poster>
Article role: <what this image helps readers understand>
Primary scene: <one concrete visual scene>
Subject: <main subject>
Style: <editorial illustration / cinematic photo / clean 3D / product mockup / diagram-like poster>
Composition: <framing, visual hierarchy, negative space>
Mood: <curious / sharp / warm / commercial / futuristic / humorous>
Color: <palette>
Details: <objects, environment, symbolic elements>
Text: <avoid text / short exact phrase if necessary>
Constraints: no watermark, no logo, no distorted Chinese text, no random UI text
```

## Style Presets

### AI Tech Editorial

Clean editorial illustration, slightly cinematic, cool blue-gray base with warm accent light, high clarity, modern Chinese tech media feeling, not generic cyberpunk.

### Commercial Product

Polished product marketing visual, clear subject, business-friendly, confident but not exaggerated, good negative space for title placement.

### Human Story

Warm realistic editorial scene, ordinary people, believable environment, subtle emotional detail, not glossy stock photo.

### Internet Meme / Live Commerce

High-energy Chinese livestream selling scene, humorous exaggeration, bright product display, expressive host, playful but publishable.

### Concept Diagram

Minimal visual metaphor, clean shapes, readable hierarchy, no tiny text, suitable for explaining an abstract idea in a WeChat article.

## Placement Rules

- Cover: must communicate tension, not just topic.
- First inline image: place after the first emotional hook or first surprise.
- Concept image: place before the densest explanation.
- Case image: place after a concrete story/example begins.
- Poster: place near the ending only if it strengthens sharing.

## Generation Decision

Use `imagegen2 generate` when the article supplies only text.

Use `imagegen2 edit` when the user supplies:

- brand image
- product screenshot
- article cover draft
- logo or IP character
- reference style image
- photo that must be preserved

## QA Checklist

- Does each image serve a different paragraph or reading job?
- Is the cover clickable without being clickbait?
- Is there enough blank space for a title overlay if needed?
- Are generated texts avoided unless short and non-critical?
- Does the visual tone match the article's trust level?
- Is the image safe for commercial/public posting?
- Are prompts specific enough to avoid generic AI slop?
