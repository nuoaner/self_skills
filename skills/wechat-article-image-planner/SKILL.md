---
name: wechat-article-image-planner
description: Use when a finalized or near-final WeChat Official Account article needs cover art, inline illustrations, summary posters, visual prompts, image placement, or optional image generation. Trigger on Chinese-language requests about WeChat article image planning, WeChat cover images, article illustrations, adding images to an article, generating images from a finalized draft, or using an available image generation tool for WeChat article visuals.
---

# WeChat Article Image Planner

Plan visuals after the article draft is stable. This skill does not write the long-form article; it turns a finalized WeChat article into a publishable image plan and, only when requested, uses an available image generation capability.

## Core Rule

Article first, images second. If the article is still rough, ask the user to finalize or explicitly approve visual planning from the current draft.

Use `references/visual-planning-playbook.md` when deciding image types, visual tone, prompt structure, or QA criteria.

## Image Generation Capability

Prefer available image generation tools in the current environment.

Priority:

1. Use the environment's native image generation capability when available.
2. Use an installed image generation skill or helper tool if available.
3. If no image generation capability exists, provide production-ready prompts and image specifications only.

Do not assume a specific local path, API key location, operating system, or image tool implementation unless it is confirmed in the current environment.

Never ask the user to paste API keys into chat.

## Workflow

1. Read the article or article file.
2. Identify article type, audience, emotional arc, and core message.
3. Extract 3-7 visual anchors: people, scenes, objects, metaphors, data, quotes, or turning points.
4. Produce an image plan before generating anything.
5. Ask for confirmation before generation unless the user explicitly requests direct generation.
6. Generate images through the available capability when possible.
7. Report saved image paths and where each image should be inserted when the environment provides them.

## Output Contract

Always provide:

- Article visual diagnosis: article type, tone, and target reader.
- Image list: cover, inline images, optional summary poster.
- Placement: after which paragraph or section each image belongs.
- Prompt: one production-ready prompt per image.
- Parameters: aspect, clarity, format, quality, and whether to use generate or edit.
- QA notes: what to check before publishing.

## Image Defaults

- Cover: `16:9`, `2K`, `png`, `quality medium` or `high`.
- Inline conceptual image: `4:3` or `1:1`, `1K`, `png`, `quality medium`.
- Mobile poster or closing summary: `9:16`, `2K`, `png`, `quality high`.

## Avoid

- Do not plan generic "AI tech background" images when the article has concrete scenes.
- Do not put too much readable Chinese text inside generated images; image models often distort text. Prefer short title overlays after generation if exact text matters.
- Do not generate images before the user confirms the plan unless they explicitly requested direct generation.
- Do not use one image prompt for all article sections. Each image must serve a distinct reading moment.
