---
name: wechat-article-image-planner
description: Use when a finalized or near-final WeChat Official Account article needs cover art, inline illustrations, summary posters, visual prompts, image placement, or optional imagegen2 generation. Trigger on Chinese requests such as 公众号配图, 公众号封面, 文章配图, 给这篇文章配图, 根据定稿生成图片, 用 imagegen2 给公众号生图.
---

# WeChat Article Image Planner

Plan visuals after the article draft is stable. This skill does not write the long-form article; it turns a finalized WeChat article into a publishable image plan and, only when requested, calls `imagegen2` to generate images.

## Core Rule

Article first, images second. If the article is still rough, ask the user to finalize or explicitly approve visual planning from the current draft.

Use `references/visual-planning-playbook.md` when deciding image types, visual tone, prompt structure, or QA criteria.

## Workflow

1. Read the article or article file.
2. Identify article type, audience, emotional arc, and core message.
3. Extract 3-7 visual anchors: people, scenes, objects, metaphors, data, quotes, or turning points.
4. Produce an image plan before generating anything.
5. Ask for confirmation before live generation unless the user already said "directly generate", "直接生图", or "用 imagegen2".
6. Use `imagegen2` for real generation. Do not recreate its API code.
7. Report saved image paths and where each image should be inserted.

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
- If the user provides a brand/reference image, use `imagegen2 edit`; otherwise use `imagegen2 generate`.

## imagegen2 Commands

Text-to-image:

```powershell
python "$env:USERPROFILE\.codex\skills\imagegen2\scripts\imagegen2.py" generate `
  --prompt "<prompt>" `
  --aspect 16:9 --clarity 2K --quality medium --format png
```

Reference/edit image:

```powershell
python "$env:USERPROFILE\.codex\skills\imagegen2\scripts\imagegen2.py" edit `
  --prompt "<prompt>" `
  --image "<reference-image-path>" `
  --aspect 1:1 --clarity 1K --quality medium --format png
```

If `IMAGEGEN2_API_KEY` is missing, stop before live generation and tell the user to set it locally. Never ask the user to paste a key into chat.

## Avoid

- Do not plan generic "AI tech background" images when the article has concrete scenes.
- Do not put too much readable Chinese text inside generated images; image models often distort text. Prefer short title overlays after generation if exact text matters.
- Do not generate images before the user confirms the plan unless they explicitly requested direct generation.
- Do not use one image prompt for all article sections. Each image must serve a distinct reading moment.
