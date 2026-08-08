<div align="center">

# 🧰 self_skills

**为 Codex / AI Agent 沉淀的一套个人 Skills 工具箱**

把反复出现的工程习惯、交付标准和工作流程，整理成可复用、可审计、可版本化的 Skills。

工程开发 · Prompt 打磨 · 文档治理 · 项目评审 · 商业化 · 客户交付 · Scoop · 公众号配图

<p>
  <img src="https://img.shields.io/badge/Skills-9-2563eb?style=flat-square" alt="9 Skills" />
  <img src="https://img.shields.io/badge/Version-v2.0.0-0ea5e9?style=flat-square" alt="Version v2.0.0" />
  <img src="https://img.shields.io/github/last-commit/nuoaner/self_skills?style=flat-square" alt="Last commit" />
  <img src="https://img.shields.io/github/stars/nuoaner/self_skills?style=flat-square" alt="GitHub stars" />
</p>

**[简体中文](README.md) · [English](README_EN.md)**

[快速开始](#-快速开始) · [Skill 一览](#-skill-一览) · [怎么选 Skill](#-怎么选-skill) · [使用示例](#-使用示例) · [质量体系](#-质量体系) · [仓库结构](#-仓库结构)

<sub>Self-maintained · Chinese-first · Codex-oriented</sub>

</div>

---

## ✨ 这是什么

`self_skills` 不是一个“提示词收藏夹”，而是一套面向真实项目协作的个人 Skill 仓库。

这里沉淀的是我希望 AI **长期稳定执行** 的工作方式，例如：

- 写代码前先读现有实现，复用已有结构，不随手造第二套机制。
- 把口语化需求整理成另一个 Agent 可以直接执行的任务说明。
- 对架构、测试、可观测性、安全和交付风险做有证据的工程评审。
- 让 README、`docs/`、`agent.md` 和项目状态保持一致。
- 在项目交付前检查结构、文档、依赖和运行说明是否完整。
- 对市场、竞品、定价等时效性信息先验证，再做商业判断。
- 把技术改造整理成客户能看懂、研发能追踪的交付汇报。
- 把 GitHub Release / 官网下载源整理成可维护的 Scoop manifest。
- 在公众号文章定稿后规划封面、插图、海报和生成提示词。

> **核心原则：** 一个 Skill 负责一类明确问题；能复用规则就不重复写，能验证就不靠猜，能用脚本稳定执行就不靠临场发挥。

---

## 🧩 Skill 一览

| 类别 | Skill | 主要用途 | 适合场景 | 版本 | 状态 |
|---|---|---|---|---|---|
| Engineering | [`ai-coding-discipline`](skills/ai-coding-discipline/SKILL.md) | 工程化执行纪律 | 写功能、修 Bug、重构、调试，要求复用现有结构并增量验证 | `2.0.0` | Stable |
| Engineering | [`ai-coding-paradigm`](skills/ai-coding-paradigm/SKILL.md) | 工程成熟度 / 架构评审 | 模块边界、测试、可观测性、安全、交付和技术风险评审 | `2.0.0` | Stable |
| Prompt | [`project-prompt-polisher`](skills/project-prompt-polisher/SKILL.md) | 可执行 Prompt 打磨 | 把模糊中文需求整理成 Codex / Agent 可直接执行的任务 | `2.0.0` | Stable |
| Documentation | [`internal-project-doc-standardizer`](skills/internal-project-doc-standardizer/SKILL.md) | 内部项目文档标准化 | 创建、审查、拆分、同步或修复 README / docs / agent.md | `2.0.0` | Stable |
| Review | [`project-structure-review`](skills/project-structure-review/SKILL.md) | 项目交付结构评审 | 提交、验收、交接前检查仓库结构、README、依赖和工程说明 | `2.0.0` | Stable |
| Delivery | [`client-technical-reporting`](skills/client-technical-reporting/SKILL.md) | 客户技术汇报 | 迁移、改造、接口替换、问题定位和联调后的对客报告 | `2.0.0` | Usable |
| Business | [`market-commercialization-strategist`](skills/market-commercialization-strategist/SKILL.md) | 市场与商业化评审 | 定位、吸引力、留存、竞品、定价、商业闭环和成熟度分析 | `2.0.0` | Usable |
| Packaging | [`app-to-scoop`](skills/app-to-scoop/SKILL.md) | Scoop manifest 创建与维护 | GitHub Release、官网、直链或已有 manifest 的生成 / 修复 | `2.0.0` | Usable |
| Content | [`wechat-article-image-planner`](skills/wechat-article-image-planner/SKILL.md) | 公众号文章视觉规划 | 文章定稿后的封面、插图、海报、位置与图片生成提示词 | `2.0.0` | Usable |

> 每个 Skill 的具体触发条件和执行规则，以对应目录中的 `SKILL.md` 为准。

---

## 🧭 怎么选 Skill

如果你不确定该用哪个，可以按下面的路径判断：

```text
我现在要做什么？
│
├─ 直接修改 / 调试 / 重构代码
│  └─ ai-coding-discipline
│
├─ 不改代码，只想评估工程质量 / 架构 / 风险
│  └─ ai-coding-paradigm
│
├─ 我有一段模糊需求，想整理成 Codex 能执行的 Prompt
│  └─ project-prompt-polisher
│
├─ README / docs / agent.md 需要创建、同步或治理
│  └─ internal-project-doc-standardizer
│
├─ 项目准备提交 / 交付 / 验收，想检查仓库是否规范
│  └─ project-structure-review
│
├─ 技术工作完成了，需要给客户写交付 / 联调 / 迁移汇报
│  └─ client-technical-reporting
│
├─ 想评估定位、用户吸引力、竞品、定价或商业化路径
│  └─ market-commercialization-strategist
│
├─ 想把一个 Windows 应用做成 Scoop manifest
│  └─ app-to-scoop
│
└─ 公众号文章已经基本定稿，需要封面和文中配图方案
   └─ wechat-article-image-planner
```

### 三个最容易混淆的 Engineering Skill

```text
project-prompt-polisher
    ↓ 负责“把需求说清楚”

ai-coding-discipline
    ↓ 负责“把代码改好并验证”

ai-coding-paradigm
    ↓ 负责“判断工程设计和交付质量好不好”
```

这三个 Skill 在 v2 中已经明确拆分职责，尽量避免相互抢触发。

---

## 🚀 快速开始

### 1. 克隆仓库

```powershell
git clone https://github.com/nuoaner/self_skills.git
cd self_skills
```

### 2. 安装单个 Skill

例如安装 `project-prompt-polisher`：

```powershell
Copy-Item -Recurse .\skills\project-prompt-polisher "$env:USERPROFILE\.codex\skills\project-prompt-polisher"
```

### 3. 安装全部 Skill

```powershell
Copy-Item -Recurse .\skills\* "$env:USERPROFILE\.codex\skills"
```

### 4. 更新

先拉取仓库最新版本：

```powershell
git pull
```

再重新复制需要更新的 Skill 到 Codex Skill 目录。

> 安装或更新后，建议重启 Codex，让 Skill 元数据和指令重新加载。

---

## 💬 使用示例

Skill 可以显式点名使用，也可以依赖描述进行自动触发。显式调用更适合你希望确定使用某套流程的时候。

### 工程实现

```text
Use ai-coding-discipline to implement this feature in the existing project.
Reuse existing structures, keep the change narrow, and verify the result.
```

### 工程评审

```text
Use ai-coding-paradigm to review this repository's architecture boundaries,
testing, observability, security, and delivery risks.
```

### Prompt 打磨

```text
用 project-prompt-polisher 帮我把这个需求整理成 Codex 能直接执行的 Prompt：
登录接口帮我完善一下，注意不要影响现有权限逻辑。
```

### 项目文档治理

```text
Use internal-project-doc-standardizer to audit this project's README, docs,
and agent.md, then tell me what is missing or inconsistent.
```

### Scoop 打包

```text
Use app-to-scoop to turn this GitHub Release into a Scoop manifest.
Verify the current release assets first and do not guess hashes or URLs.
```

### 商业化评审

```text
用 market-commercialization-strategist 评估这个产品的目标用户、核心吸引力、
竞品差异、定价逻辑和商业化成熟度。涉及当前市场数据的结论先验证来源。
```

<details>
<summary><strong>更多典型使用场景</strong></summary>

<br />

**客户交付汇报**

```text
Use client-technical-reporting to turn this migration and API replacement work
into a client-facing delivery report with follow-up confirmation items.
```

**项目交付前检查**

```text
Use project-structure-review to check whether this repository is ready for
handoff, including README, dependencies, tooling, structure, and run instructions.
```

**公众号配图规划**

```text
用 wechat-article-image-planner 为这篇已经定稿的公众号文章规划封面、
3 张文中插图和结尾海报，并给出每张图的插入位置与生成提示词。
```

</details>

---

## 🛡️ 质量体系

这个仓库不是只维护 Skill 内容，也维护 Skill 本身的“工程质量”。

### 版本管理

每个 Skill 根目录都有独立的 `VERSION`：

```text
skills/<skill-name>/VERSION
```

当前统一基线：**`2.0.0`**。

仓库级变更记录见：[`skills/CHANGELOG.md`](skills/CHANGELOG.md)。

### Trigger 边界测试

[`skills/TRIGGER_TESTS.md`](skills/TRIGGER_TESTS.md) 维护每个 Skill 的：

- `Should trigger`
- `Should not trigger`

目的不是测试“文案好不好看”，而是减少 Skill 之间的**过度触发、漏触发和职责重叠**。

### 仓库审计

运行只读审计：

```powershell
python .\scripts\audit_skills.py
```

当前审计会检查：

- Skill 数量与目录命名
- `SKILL.md` frontmatter
- `agents/openai.yaml`
- `VERSION` 与语义版本格式
- `skills/CHANGELOG.md`
- Trigger 测试完整性
- 未被 `SKILL.md` 引用的 references
- 未被说明的运行脚本
- UTF-8 / 常见乱码
- 疑似真实密钥或敏感字段
- `SKILL.md` 是否过长

正常情况下会看到类似：

```text
Skills discovered: 9
Version baseline: 2.0.0 (9 skills)
Skill audit passed
```

### Skill 自检脚本

部分 Skill 带有自己的维护检查脚本：

```text
scripts/check_*.py
```

修改 Skill 后，优先运行对应的 `scripts/check_*.py`，最后再运行仓库级 `scripts/audit_skills.py`。

> `agents/openai.yaml` 当前保留 Codex 使用中的 legacy top-level metadata。仓库审计同时兼容 legacy 格式和 `interface.*` 格式，因此后续可以单独迁移，而不需要一次性破坏现有环境。

---

## 🗂️ 仓库结构

```text
self_skills/
├─ README.md
├─ README_EN.md
├─ scripts/
│  └─ audit_skills.py
└─ skills/
   ├─ README.md
   ├─ CHANGELOG.md
   ├─ TRIGGER_TESTS.md
   │
   ├─ ai-coding-discipline/
   ├─ ai-coding-paradigm/
   ├─ app-to-scoop/
   ├─ client-technical-reporting/
   ├─ internal-project-doc-standardizer/
   ├─ market-commercialization-strategist/
   ├─ project-prompt-polisher/
   ├─ project-structure-review/
   └─ wechat-article-image-planner/
```

大多数 Skill 遵循下面的结构：

```text
skill-name/
├─ SKILL.md
├─ VERSION
├─ agents/
│  └─ openai.yaml
├─ references/     # 可选：按需加载的知识 / 模板 / 规则
├─ scripts/        # 可选：确定性检查或辅助脚本
└─ assets/         # 可选：最终输出需要使用的静态资源
```

### 文件职责

| 文件 / 目录 | 作用 |
|---|---|
| `SKILL.md` | Skill 入口，定义触发条件、核心流程、约束和资源导航 |
| `VERSION` | 当前 Skill 的语义版本 |
| `agents/openai.yaml` | Agent / UI 元数据 |
| `references/` | 详细规则、模板、检查表、领域知识，按需加载 |
| `scripts/` | 稳定、可重复、适合程序执行的检查或辅助操作 |
| `assets/` | 模板、图片等最终输出资源，不作为主要推理上下文 |

---

## 🧠 维护原则

### 1. 一个 Skill 解决一类明确问题

如果两个 Skill 经常对同一请求同时“觉得自己该上”，优先重新划分触发边界，而不是继续往 description 里堆关键词。

### 2. `SKILL.md` 是控制面，不是知识仓库

核心流程放在 `SKILL.md`；大量规则、模板和背景知识放进 `references/`；确定性操作尽量交给 `scripts/`。

### 3. 不猜时效性事实

Release、下载地址、市场价格、竞品状态、法规、产品能力等会变化的信息，需要当前证据时就先验证。

### 4. 不为了“完整”而复制第三方 Skill

这个仓库只维护自己愿意长期负责的 Skill，不作为官方 Skill 或第三方插件缓存的镜像。

### 5. 修改后必须留下验证路径

一个 Skill 的改动应该能够通过 trigger tests、self-check 或 repository audit 中至少一种方式被重新检查。

---

## 🚧 维护边界

这个仓库**不负责长期维护**：

- Codex 官方系统 Skills，例如 `.codex/skills/.system`
- 插件缓存，例如 `.codex/plugins/cache`
- 没有明确维护理由的第三方 Skill 副本

第三方 Skill 更适合保留原始来源链接，而不是复制进本仓库后形成无法追踪的分叉版本。

---

## 📦 当前版本

**v2.0.0** 是当前统一 Skill 基线，重点完成了：

- Coding execution / engineering review / prompt polishing 职责拆分
- 中文内容审计兼容
- Trigger 边界测试整理
- 市场分析实时证据门
- Scoop upstream freshness gate
- 文档 Skill 的脚本路径可移植性
- 公众号配图 Skill 的图片工具解耦
- 每 Skill 独立 `VERSION`
- Repository-level `CHANGELOG.md`
- references / scripts 资源卫生检查

完整变更请看 [`skills/CHANGELOG.md`](skills/CHANGELOG.md)。

---

<div align="center">

**Make repeated good decisions reusable.**

<sub>Built for real project work, not prompt collecting.</sub>

</div>
