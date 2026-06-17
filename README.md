# self_skills

> 中文为主的个人 Codex Skills 仓库，用来沉淀我在工程开发、项目文档、Prompt 打磨和仓库审查中的常用工作流。

## 简介

这个仓库存放我自己维护的 Codex skills。它们不是通用插件市场的合集，而是围绕真实项目协作整理出来的一组“工作习惯工具”：

- 让 AI 写代码前先澄清边界、复用已有结构、控制复杂度。
- 把模糊中文需求改成另一个 AI Agent 可以直接执行的 prompt。
- 按内部项目规范整理 `README.md`、`docs/` 和 `agent.md`。
- 在项目提交、交付或评审前检查仓库结构和文档完整性。
- 从市场经理视角评审产品吸引力、用户留存、市场匹配和商业化成熟度。
- 把迁移、改造、接口替换和联调工作整理成甲方能看懂的技术汇报。

## Skills 列表

| Skill | 主要用途 | 适合场景 |
|---|---|---|
| `ai-coding-discipline` | 工程化编码纪律 | 写功能、修 bug、重构、架构设计时，要求 AI 先检查现有结构、复用已有实现、按最小闭环实现并验证 |
| `ai-coding-paradigm` | 工程范式分析与 Prompt 加固 | 分析代码质量、模块边界、测试、契约、可观测性、安全和发布流程 |
| `client-technical-reporting` | 甲方技术汇报整理 | 迁移、改造、接口替换、问题定位或联调阶段后，整理甲方可读、技术可追踪的汇报材料 |
| `internal-project-doc-standardizer` | 内部项目文档标准化 | 创建或审查 `README.md`、`docs/`、`agent.md`，检查状态枚举、模板和文档合规性 |
| `market-commercialization-strategist` | 市场经理与商业化策略 | 设计项目、产品、页面、功能、README 或商业方案时，评估用户吸引力、留存依赖、市场匹配、定价和商业成熟度 |
| `project-prompt-polisher` | 中文任务 Prompt 打磨 | 把口语化产品、前端、后端、文档、测试、重构或自动化需求改成可执行 prompt |
| `project-structure-review` | 项目结构审查 | 项目提交、交付、验收、申请或团队交接前，检查目录结构、命名、README 和工程说明 |

## 推荐使用方式

### 写代码前

优先使用：

```text
ai-coding-discipline
```

适合让 Codex 在实现前先看现有代码、拆模块、明确边界、做增量验证。当前版本已经补充执行清单、压力场景、通用 prompt 模板和只读自检脚本。

### 分析项目质量

优先使用：

```text
ai-coding-paradigm
```

适合从工程范式角度检查项目：需求边界、模块职责、接口契约、测试、日志、安全、发布和回滚。

### 整理项目文档

优先使用：

```text
internal-project-doc-standardizer
```

适合初始化或检查标准项目文档结构：

```text
README.md
agent.md
docs/standard.md
docs/requirements.md
docs/architecture.md
docs/api.md
docs/database.md
docs/deploy.md
docs/test.md
docs/changelog.md
```

### 打磨中文需求

优先使用：

```text
project-prompt-polisher
```

示例：

```text
用 project-prompt-polisher 帮我把这个需求改成 Codex 能直接执行的 prompt：登录接口帮我完善一下。
```

### 做市场与商业化评审

优先使用：

```text
market-commercialization-strategist
```

适合在产品设计、功能规划、落地页、README、商业方案或定价前，检查项目是否有清晰目标用户、用户吸引力、留存机制、市场差异、付费理由和商业化成熟度。

### 给甲方做技术汇报

优先使用：

```text
client-technical-reporting
```

适合在一次迁移、改造、接口替换、问题修复或联调阶段后，按“本次做了什么、迁移方式、主要改动位置、真实接口后续在哪改、模块问题定位、后续联调需确认事项、总结”的结构整理给甲方。

### 项目提交前审查

优先使用：

```text
project-structure-review
```

适合检查项目是否具备可交付的 README、结构、依赖说明、工程配置和架构说明。

## 仓库结构

```text
self_skills/
  README.md
  skills/
    ai-coding-discipline/
    ai-coding-paradigm/
    client-technical-reporting/
    internal-project-doc-standardizer/
    market-commercialization-strategist/
    project-prompt-polisher/
    project-structure-review/
```

每个 skill 通常遵循以下结构：

```text
skill-name/
  SKILL.md
  agents/openai.yaml        # 可选：Codex UI 元数据
  references/               # 可选：模板、规范、详细参考
  scripts/                  # 可选：辅助脚本
```

## 安装方式

克隆仓库：

```powershell
git clone https://github.com/nuoaner/self_skills.git
```

复制单个 skill 到 Codex skills 目录：

```powershell
Copy-Item -Recurse .\self_skills\skills\project-prompt-polisher "$env:USERPROFILE\.codex\skills\project-prompt-polisher"
```

复制全部 skills：

```powershell
Copy-Item -Recurse .\self_skills\skills\* "$env:USERPROFILE\.codex\skills"
```

安装或更新后，重启 Codex 让新 skill 生效。

## 维护边界

这个仓库只收录我自己维护、愿意长期调整的 skills。

不收录：

- Codex 官方系统 skills：`.codex/skills/.system`
- 插件缓存 skills：`.codex/plugins/cache`
- 第三方仓库安装的 skills

第三方 skills 应该保留原始来源链接，不直接复制到这里维护。

## 质量状态

| Skill | 状态 | 说明 |
|---|---|---|
| `project-structure-review` | 稳定 | 有只读审查脚本，适合直接用于项目交付前检查 |
| `ai-coding-discipline` | 稳定 | 已从原则型说明升级为执行闸门，包含执行清单、压力场景、Prompt 模板和只读自检脚本 |
| `client-technical-reporting` | 可用 | 轻量甲方技术汇报 skill，适合迁移、接口替换、模块问题定位和联调事项整理 |
| `internal-project-doc-standardizer` | 稳定 | 已升级为 audit/generate/split/sync/repair 五模式文档闸门，包含模板、审查脚本和 skill 自检脚本 |
| `market-commercialization-strategist` | 可用 | 轻量 `SKILL.md` + 重型 Markdown 手册，适合市场经理视角、产品商业化和网页端复用 |
| `project-prompt-polisher` | 稳定 | 已升级为轻量入口 + 多场景 Prompt 模板 + 自检脚本，适合高频打磨中文任务 prompt |
| `ai-coding-paradigm` | 可用 | 偏分析型，适合做工程成熟度和提示词加固；后续可补充仓库内 references |

## English Summary

`self_skills` is a personal Codex skills collection focused on practical engineering workflows.

It includes skills for disciplined coding, engineering paradigm analysis, client-facing technical reporting, internal project documentation standardization, market commercialization strategy, Chinese prompt polishing, and project structure review.

`ai-coding-discipline` has been upgraded from a principle-style reminder into an execution-gate skill with a checklist, pressure scenarios, prompt template, and read-only quality check script.

This repository intentionally keeps only self-maintained skills. Official Codex system skills, plugin cache skills, and third-party skills should stay linked to their original sources.
