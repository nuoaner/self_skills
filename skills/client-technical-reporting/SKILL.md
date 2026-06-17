---
name: client-technical-reporting
description: Use when preparing a Chinese client-facing technical report, delivery note, migration summary, integration update, handoff explanation, or progress report for customers who understand some technology, especially after code migration, module refactoring, API replacement, bug fixing, or joint debugging.
---

# Client Technical Reporting

## Overview

Use this skill to turn engineering work into a client-facing technical report. Write for a client-side reader who understands some technology: concrete enough to trace modules and interfaces, but not overloaded with low-level implementation noise.

The report should answer: what changed, how it was migrated, where it changed, where real APIs should be connected later, how to locate problems, what still needs joint confirmation, and what conclusion the client should take away.

## Required Structure

Always organize the report with these seven sections:

```text
1. 本次做了什么
2. 迁移方式
3. 主要改动位置
4. 真实接口后续在哪改
5. 模块问题定位
6. 后续联调需确认的事项
7. 总结
```

## Writing Rules

- Use Chinese by default.
- Keep the tone professional, cooperative, and evidence-based.
- Use module names, page names, file paths, API names, and config names when available.
- Distinguish completed work, temporary adaptation, mock data, pending real API integration, and items requiring client confirmation.
- Avoid vague claims such as "已优化" without explaining the changed scope.
- Avoid excessive source-code detail unless the client explicitly asks for it.
- Do not invent paths, endpoints, owners, dates, test results, or client decisions. Mark unknowns as "待确认".

## Section Guidance

### 1. 本次做了什么

Summarize the actual delivered scope in plain language.

Include:

- Migrated or adjusted modules.
- Completed UI, route, API, data model, config, or compatibility changes.
- Visible result for the client.
- Any temporary mock, placeholder, or compatibility layer.

### 2. 迁移方式

Explain the migration strategy and why it was chosen.

Common patterns:

- Direct migration: preserve original structure and adapt minimal differences.
- Compatibility migration: keep old behavior while adapting new framework or interface conventions.
- Layered migration: split UI, data service, API adapter, and config changes.
- Mock-first migration: use temporary mock data until real client APIs are ready.
- Incremental migration: migrate module by module to reduce risk.

Mention risk controls such as preserving route names, keeping old field mapping, isolating API adapters, or maintaining fallback logic.

### 3. 主要改动位置

List key changed locations. Prefer a table.

```text
| 位置 | 改动内容 | 说明 |
|---|---|---|
| src/... | ... | ... |
```

Use paths, module names, pages, components, stores, services, configs, SQL files, or deployment files depending on the project.

### 4. 真实接口后续在哪改

Point out where real APIs should be connected later.

Include:

- API service file or adapter file.
- Mock data location.
- Field mapping location.
- Environment/config location.
- Authentication or token handling location.
- Response format assumptions.

If exact API details are not available, state what needs to be provided by the client.

### 5. 模块问题定位

Give the client a practical troubleshooting map.

Use this pattern:

```text
现象 -> 优先检查位置 -> 可能原因 -> 建议处理方式
```

Cover likely issues:

- Page cannot open: route, menu, permission, build output.
- Data empty: API address, mock switch, query params, field mapping.
- Save fails: request payload, required fields, auth, backend validation.
- Style abnormal: scoped style, design system, asset path.
- Build or deployment failure: dependency, environment variable, base path, proxy config.

### 6. 后续联调需确认的事项

List client-side confirmations as clear action items.

Include:

- Real API endpoint, method, auth, and response structure.
- Field names, enum values, dictionary mapping, and required fields.
- Pagination, filtering, sorting, and export behavior.
- Error code and message conventions.
- Permission/menu rules.
- Deployment environment, domain, proxy, and cross-origin requirements.
- Acceptance criteria and test account/data.

Use "需甲方确认" instead of assigning blame.

### 7. 总结

Summarize the delivery state and next step.

Good summary pattern:

```text
本次已完成 [scope]，当前通过 [mock/adapter/config] 保证页面和流程可运行。
后续重点是与甲方确认 [API/字段/权限/环境]，再将临时数据或适配层切换为真实接口。
```

## Output Template

```markdown
# 项目阶段汇报

## 1. 本次做了什么

- ...

## 2. 迁移方式

- ...

## 3. 主要改动位置

| 位置 | 改动内容 | 说明 |
|---|---|---|
| ... | ... | ... |

## 4. 真实接口后续在哪改

- ...

## 5. 模块问题定位

| 问题现象 | 优先检查位置 | 可能原因 | 建议处理 |
|---|---|---|---|
| ... | ... | ... | ... |

## 6. 后续联调需确认的事项

- 需甲方确认：...

## 7. 总结

...
```

## Quality Checklist

Before finalizing, verify:

- Each of the seven required sections exists.
- Client-facing claims are backed by concrete modules, files, APIs, or observable results.
- Temporary mock/adaptation points are clearly separated from completed real integration.
- Follow-up items are written as confirmation points, not blame.
- The summary states current status and next action.
