---
name: project-prompt-polisher
description: Turn rough Chinese product, UI, frontend, and platform change requests into implementation-ready prompts tailored to the current drone supervision and smart agriculture project. Use when the user asks to polish a prompt, optimize a modification request, rewrite vague page changes into clearer development instructions, or generate project-aware prompt templates for the real-time dashboard, video monitor, history page, regulator dashboard, login page, admin pages, and future smart-agriculture IoT modules.
---

# Project Prompt Polisher

Rewrite the user's rough modification request into a prompt another Codex instance can execute with minimal ambiguity.

## Apply These Project Defaults

- Treat the product roadmap as staged: first complete the drone base platform, then extend into the smart-agriculture IoT supervision and linkage platform.
- Preserve the current product language unless the user explicitly asks for a redesign: white cards, blue primary color, gray background, enterprise-control layout, and consistent admin-style information density.
- Preserve existing business logic, route structure, role permissions, and data linkage unless the user explicitly requests structural changes.
- Prefer responsive layouts and flexible spacing. Avoid fixed widths and heights unless they are clearly required.
- Prevent text overflow, clipping, overlap, hidden content, broken scroll areas, or decorative changes that reduce usability.
- Assume the user wants implementation-ready Chinese prompts, not abstract product copy.

## Recognize The Main Project Areas

Map the user's request to one of these areas before rewriting:

- Real-time dashboard: map, HUD, left and right side panels, bottom efficiency chart, fleet switching, homepage visual polish.
- Video monitoring: multi-channel monitoring center, main screen switching, alert display, homepage video entry.
- History operations: task list, replay, task detail, settlement export.
- Areas and projects: area management, project linkage, map-region coordination.
- Regulator dashboard: regulator-facing large screen, rankings, risk panels, monitoring overview.
- Login and admin: login page, account management, role management, device management.
- Smart-agriculture extension: environment sensing, IoT linkage, agricultural monitoring cockpit, but only when the user explicitly asks for that stage.

## Rewrite Workflow

1. Identify the target page, component, or business module.
2. Infer what must stay unchanged: style, logic, data binding, routing, permissions, or interaction flow.
3. Convert vague wording into concrete actions: resize, align, add, hide, reorder, link, constrain, or refactor.
4. Add implementation constraints that fit this project:
   - keep current style consistent
   - do not break existing functions
   - prefer responsive layout
   - ensure content remains fully visible
5. Return a prompt that is ready to execute without extra cleanup.

## Output Rules

- Default to a single polished prompt.
- If the user gives a very short sentence, expand it into a structured development prompt.
- If the request is about UI, layout, or visual cleanup, include explicit non-regression requirements.
- If the request is about a feature, include scope boundaries so the implementation does not drift.
- Only provide multiple prompt variants when the user explicitly asks for options.
- Do not turn the answer into product strategy unless the user asked for strategy.

## Prompt Shape To Produce

Use this structure unless the user asks for a different format:

```md
请基于当前项目进行修改，保持现有页面风格、布局体系和业务逻辑不变，重点优化`页面/组件`。

修改目标：`目标`

具体要求：
1. `改动点 1`
2. `改动点 2`
3. `改动点 3`

要求：
- 保持与当前无人机平台整体风格一致
- 优先使用响应式布局，减少固定宽高
- 不影响现有功能和数据展示
- 修改后保证内容不溢出、不遮挡、不裁切
```

## Strong Defaults By Request Type

### UI and Layout Refinement

Always add:

- keep current overall style unchanged
- optimize spacing, typography, and alignment
- avoid overflow and clipping
- improve responsiveness
- do not introduce a visually inconsistent new design language

### Feature Expansion

Always add:

- define the target page and entry point
- state what existing logic must be reused
- limit the new feature to the requested scope
- preserve routes, permissions, and current data flow unless explicitly changed

### Large Screen / Dashboard Optimization

Always add:

- reduce non-critical visual occupation of the map area
- improve hierarchy between core data, map, and side panels
- ensure large-screen readability without wasting space
- maintain consistency with the rest of the system

## Example Transformations

### Example 1

User input:

```text
实时监控页面左上角和右上角那个框太大了
```

Preferred rewrite:

```text
请基于当前项目的实时监控页面进行界面优化，保持现有无人机监管首页的整体风格、地图布局和 HUD 逻辑不变。将地图区域左上角的 N-Mode / GPS 状态框，以及右上角的 LINK / 电量状态框进一步缩小，减少它们对主地图可视区域的占用。

具体要求：
1. 缩小这两个状态框的整体宽度、高度、内边距和圆角尺寸。
2. 同步缩小框内图标、文字字号和分隔线间距，但要保证核心信息仍清晰可读。
3. 优先使用响应式尺寸方案，不要继续使用过大的固定像素值。
4. 调整后要保证它们与中间地图、顶部绘地块按钮和底部飞行参数条之间的视觉关系更协调。
5. 修改后不能影响实时状态展示逻辑，也不能遮挡地图中的无人机点位和轨迹信息。
```

### Example 2

User input:

```text
登录界面的备案号位置不太好
```

Preferred rewrite:

```text
请基于当前项目的登录页面进行优化，保持现有登录卡片、配色和整体风格不变。重点调整备案号展示位置，使其与登录页底部信息区域形成统一结构，不要孤立悬浮在卡片外。要求备案信息层级清晰、位置稳定、视觉上更规整，同时保留工信部备案链接跳转能力，不影响现有登录流程和页面响应式表现。
```

### Example 3

User input:

```text
视频监控页要更像正式监控中心
```

Preferred rewrite:

```text
请基于当前项目的视频监控页面进行优化，保持现有系统整体风格一致，不要做与首页和监管页割裂的新设计。将当前页面调整为更接近正式监控中心的结构，突出主监控画面、多通道列表、状态信息和告警区块。

具体要求：
1. 强化主画面区域的视觉中心地位，并优化通道切换逻辑。
2. 完善在线、离线、告警等状态展示，使页面具备正式监控中心的识别度。
3. 保持与当前无人机基础平台一致的配色、卡片风格和信息密度。
4. 优先兼容后续真实视频流接入，不要把结构写死成演示页。
```

## If The User Asks To "Polish" Only

Return the polished prompt directly. Do not explain the transformation unless the user asks for the reasoning.

## If The User Asks For Prompt Templates

Return reusable templates grouped by page type, using the current project structure and terminology.