<div align="center">

# 🧰 self_skills

**面向 Codex / AI Agent 的个人 Skills 工作流仓库**

把反复出现的工程习惯、交付标准、商业判断和视觉工作流，沉淀成可复用、可审计、可持续迭代的 Skills。

工程开发 · Prompt · 文档治理 · 项目评审 · 商业化 · 客户交付 · Scoop · 内容视觉 · AI 生图

<p>
  <img src="https://img.shields.io/badge/Skill%20entries-18-2563eb?style=flat-square" alt="18 Skill entries" />
  <img src="https://img.shields.io/badge/Productionized-10-16a34a?style=flat-square" alt="10 Productionized Skills" />
  <img src="https://img.shields.io/badge/Visual%20Lab-7-f59e0b?style=flat-square" alt="7 Visual Lab Skills" />
  <img src="https://img.shields.io/badge/Core%20baseline-v2.0.0-0ea5e9?style=flat-square" alt="Core baseline v2.0.0" />
  <img src="https://img.shields.io/github/last-commit/nuoaner/self_skills?style=flat-square" alt="Last commit" />
</p>

**[简体中文](README.md) · [English](README_EN.md)**

[仓库定位](#-仓库定位) · [Skill 一览](#-skill-一览) · [怎么选](#-怎么选-skill) · [快速开始](#-快速开始) · [原创规则](#-第三方参考与原创规则) · [质量体系](#-质量体系) · [仓库结构](#-仓库结构)

<sub>Self-maintained · Chinese-first · Codex-oriented</sub>

</div>

---

## ✨ 仓库定位

`self_skills` 不是“提示词收藏夹”，也不是第三方 Skill 镜像站。

这个仓库保存的是我愿意长期维护的 AI 工作方式：把一类重复问题拆成明确职责、稳定流程、边界条件、验证路径和可复用资源，让 Codex / AI Agent 在真实项目里少猜、少跑偏、少重复造轮子。

当前 `skills/` 下共有 **18 个 Skill 条目**，按成熟度分为三层：

1. **Productionized（10）**：已按仓库工程规范整理，可作为正式工作流维护。
2. **Visual Lab（7）**：视觉能力实验区，先验证方法和职责边界，再逐步补齐完整 Skill 工程结构。
3. **Reference Index（1）**：外部优秀案例索引，只保留来源和选型信息，不把第三方内容冒充为本仓库原创 Skill。

> **核心原则：** 一个 Skill 负责一类明确问题；能复用就不重复，能验证就不猜，能抽象方法就不复制别人实现。

---

## 🧩 Skill 一览

### Productionized Skills

| 类别 | Skill | 主要用途 | 版本 |
|---|---|---|---|
| Engineering | [`ai-coding-discipline`](skills/ai-coding-discipline/SKILL.md) | 写功能、修 Bug、重构、调试时保持复用、边界和增量验证 | `2.0.0` |
| Engineering | [`ai-coding-paradigm`](skills/ai-coding-paradigm/SKILL.md) | 架构、测试、可观测性、安全、交付和技术风险评审 | `2.0.0` |
| Prompt | [`project-prompt-polisher`](skills/project-prompt-polisher/SKILL.md) | 把模糊需求整理成 Codex / Agent 可直接执行的任务说明 | `2.0.0` |
| Documentation | [`internal-project-doc-standardizer`](skills/internal-project-doc-standardizer/SKILL.md) | 创建、审查、拆分、同步或修复 README / docs / agent.md | `2.0.0` |
| Review | [`project-structure-review`](skills/project-structure-review/SKILL.md) | 交付、验收、交接前检查仓库结构、依赖和运行说明 | `2.0.0` |
| Delivery | [`client-technical-reporting`](skills/client-technical-reporting/SKILL.md) | 把迁移、改造、接口替换、问题定位整理成对客技术汇报 | `2.0.0` |
| Business | [`market-commercialization-strategist`](skills/market-commercialization-strategist/SKILL.md) | 定位、吸引力、留存、竞品、定价和商业化成熟度分析 | `2.0.0` |
| Packaging | [`app-to-scoop`](skills/app-to-scoop/SKILL.md) | 从 GitHub Release / 官网等来源生成或维护 Scoop manifest | `2.0.0` |
| Content | [`wechat-article-image-planner`](skills/wechat-article-image-planner/SKILL.md) | 为定稿公众号文章规划封面、插图、海报和生成提示词 | `2.0.0` |
| Visual AI | [`visual-story-image-director`](skills/visual-story-image-director/SKILL.md) | 把现有照片/场景转成故事化、编辑化、品牌化视觉资产 | `2.0.0` |

### Visual Lab

这些条目已经有明确能力方向，但目前属于**实验 / 细化阶段**，更适合显式点名使用或继续补齐，不应和已工程化 Skill 混为一谈。

| Skill | 能力方向 |
|---|---|
| [`creative-reference-analyzer`](skills/creative-reference-analyzer/SKILL.md) | 从参考图中提取构图、视觉语法和传播逻辑，不复制原图 |
| [`image-prompt-engineer`](skills/image-prompt-engineer/SKILL.md) | 把“高级一点、好看一点”之类模糊生图需求整理成结构化生成规格 |
| [`consistent-character-designer`](skills/consistent-character-designer/SKILL.md) | 管理人物 / IP / 吉祥物在多张图片中的身份与视觉一致性 |
| [`brand-visual-system-designer`](skills/brand-visual-system-designer/SKILL.md) | 从单张图升级到可重复使用的品牌视觉语言与生成规则 |
| [`ai-poster-art-director`](skills/ai-poster-art-director/SKILL.md) | 用传播目标、信息层级、视觉隐喻和版式空间指导 AI 海报 |
| [`product-visual-designer`](skills/product-visual-designer/SKILL.md) | 面向落地页、营销、电商等场景做产品价值表达和转化型视觉 |
| [`ai-image-quality-reviewer`](skills/ai-image-quality-reviewer/SKILL.md) | 从主体准确、构图、层级、一致性、可用性和情绪效果评审生成图 |

### Reference Index

- [`image-generation-collection`](skills/image-generation-collection/SKILL.md)：用于记录值得继续研究的外部 AI 生图 Skill / 仓库和选型信息。这里的第三方项目仍以**原始来源**为准，不复制其 Skill 内容到本仓库后冒充原创。

> 每个正式 Skill 的触发条件和执行规则，以对应目录中的 `SKILL.md` 为准；Visual Lab 条目当前以显式调用和方法验证为主。

---

## 🧭 怎么选 Skill

### 工程 / 项目工作

```text
直接修改、调试、重构代码
└─ ai-coding-discipline

不改代码，只评估架构、工程质量或风险
└─ ai-coding-paradigm

把口语化需求整理成 Codex 可执行任务
└─ project-prompt-polisher

README / docs / agent.md 需要治理
└─ internal-project-doc-standardizer

项目准备交付 / 验收 / 交接
└─ project-structure-review

技术工作完成，需要对客户汇报
└─ client-technical-reporting

评估产品定位、竞品、定价、商业闭环
└─ market-commercialization-strategist

把 Windows 应用整理成 Scoop manifest
└─ app-to-scoop
```

### 内容 / 视觉工作

```text
公众号文章已定稿，要规划整套封面和文中配图
└─ wechat-article-image-planner

已有照片 / 场景，要做故事化、杂志化、拼贴、品牌叙事视觉
└─ visual-story-image-director

先分析一张参考图为什么有效
└─ creative-reference-analyzer   [Lab]

需求太模糊，需要先整理成生图规格
└─ image-prompt-engineer         [Lab]

角色要跨多张图保持一致
└─ consistent-character-designer [Lab]

要建立品牌长期视觉语言
└─ brand-visual-system-designer  [Lab]

要做活动 / 宣传 / 社媒海报
└─ ai-poster-art-director        [Lab]

要做产品营销 / 落地页 / 电商视觉
└─ product-visual-designer       [Lab]

图片已经生成，需要做质量验收和迭代建议
└─ ai-image-quality-reviewer     [Lab]
```

一个常用的视觉链路可以是：

```text
参考分析 → 需求结构化 → 专项视觉设计 → 生成 / 编辑 → 质量评审
```

Visual Lab 的目标不是把流程越拆越碎，而是先验证这些职责是否值得独立成 Skill；出现明显重叠时优先合并，而不是继续堆 Skill 数量。

---

## 🚀 快速开始

### 1. 克隆仓库

```powershell
git clone https://github.com/nuoaner/self_skills.git
cd self_skills
```

### 2. 推荐：按需安装单个 Productionized Skill

例如安装 `visual-story-image-director`：

```powershell
$skill = "visual-story-image-director"
Copy-Item -Recurse ".\skills\$skill" "$env:USERPROFILE\.codex\skills\$skill" -Force
```

### 3. 不建议直接复制 `skills/*`

`skills/` 目录除了 Skill 文件夹，还包含 `README.md`、`CHANGELOG.md`、`TRIGGER_TESTS.md`，并且目前有 Visual Lab / Reference Index 条目。

因此更推荐：

- 只安装你实际要用的 Skill；
- 正式环境优先安装 Productionized Skills；
- Lab 条目先用于显式测试和能力验证，成熟后再补齐工程结构。

### 4. 更新

```powershell
git pull
```

更新后重新复制对应 Skill 目录，并重启 Codex 以重新加载元数据和指令。

---

## 🧪 典型调用示例

### 工程实现

```text
Use ai-coding-discipline to implement this feature in the existing project.
Reuse existing structures, keep the change narrow, and verify the result.
```

### Prompt 打磨

```text
用 project-prompt-polisher 把下面这段口语需求整理成 Codex 能直接执行的增量任务：
登录接口帮我完善一下，但不要影响现有权限逻辑。
```

### 照片故事化视觉

```text
用 visual-story-image-director 分析这张照片，保留人物和场景事实，
把它做成有杂志编辑感的故事视觉，并给出生成/编辑 brief 和 QA 标准。
```

### Visual Lab 显式测试

```text
用 creative-reference-analyzer 分析这张参考图。
只提炼构图、层级、材质、色彩和传播逻辑，不复制原图和原提示词。
```

---

## 🧬 第三方参考与原创规则

这个仓库允许研究优秀外部 Skill，但**不做换名字式搬运**。

### 可以借鉴

- 问题拆解方式
- 工作流阶段
- 质量评估维度
- 可迁移的设计 / 工程原则
- 值得验证的交互方式和边界设计

### 不应直接复制

- 第三方 `SKILL.md` 文案
- 原始 prompt block / 模板块
- 原案例文字与示例输出
- 独特术语体系和命名
- 为了“看起来不一样”而轻微改写的目录结构或执行步骤

### 纳入本仓库前应做到

1. 先判断仓库里是否已有相近能力，能整合就不重复创建。
2. 重新定义本仓库自己的目标用户、输入、输出、边界和触发条件。
3. 用自己的语言重写流程、规则、示例和术语。
4. 新增能够证明该 Skill 有独立价值的案例或验证路径。
5. 如果只是值得关注的外部项目，放进 Reference Index 并保留原始来源，不伪装成自研。

`visual-story-image-director` 已把这一原则写进自身 Core Rules：**Borrow principles, not implementation.**

---

## 🛡️ 质量体系

### Productionized Skill 的目标结构

```text
skill-name/
├─ SKILL.md          # YAML frontmatter + 核心流程 + 边界
├─ VERSION           # 语义版本
├─ agents/
│  └─ openai.yaml    # Agent / UI 元数据
├─ references/       # 可选：规则、模板、检查表、领域知识
├─ scripts/          # 可选：确定性检查或辅助操作
├─ examples/         # 可选：验证过的案例
└─ assets/           # 可选：最终输出所需静态资源
```

### Trigger 边界

[`skills/TRIGGER_TESTS.md`](skills/TRIGGER_TESTS.md) 用 `Should trigger / Should not trigger` 约束已工程化 Skill 的职责边界，减少过度触发、漏触发和 Skill 互抢。

### 仓库审计

```powershell
python .\scripts\audit_skills.py
```

审计目标包括目录命名、frontmatter、`agents/openai.yaml`、`VERSION`、引用资源、脚本说明、乱码和敏感字段等。

> **当前状态说明：** 2026-08-10 新增的 Visual Lab / Reference Index 条目尚未全部补齐 Productionized 结构，因此仓库级审计可能会把它们报告为待完善项。这是当前真实状态，不应在 README 中继续宣称“18 个条目全部通过 v2 工程审计”。

### 版本策略

- Productionized Skills 当前共享基线仍为 **`2.0.0`**。
- Lab 条目没有强行伪造版本号；等职责和结构稳定后再进入正式版本管理。
- 仓库级变更记录见 [`skills/CHANGELOG.md`](skills/CHANGELOG.md)。

---

## 🗂️ 仓库结构

```text
self_skills/
├─ README.md
├─ README_EN.md
├─ assets/
├─ scripts/
│  └─ audit_skills.py
└─ skills/
   ├─ README.md
   ├─ CHANGELOG.md
   ├─ TRIGGER_TESTS.md
   │
   ├─ # Productionized
   ├─ ai-coding-discipline/
   ├─ ai-coding-paradigm/
   ├─ app-to-scoop/
   ├─ client-technical-reporting/
   ├─ internal-project-doc-standardizer/
   ├─ market-commercialization-strategist/
   ├─ project-prompt-polisher/
   ├─ project-structure-review/
   ├─ visual-story-image-director/
   ├─ wechat-article-image-planner/
   │
   ├─ # Visual Lab
   ├─ ai-image-quality-reviewer/
   ├─ ai-poster-art-director/
   ├─ brand-visual-system-designer/
   ├─ consistent-character-designer/
   ├─ creative-reference-analyzer/
   ├─ image-prompt-engineer/
   ├─ product-visual-designer/
   │
   └─ image-generation-collection/   # Reference Index
```

---

## 🧠 维护原则

1. **一个 Skill 解决一类明确问题。** 触发边界比 Skill 数量更重要。
2. **`SKILL.md` 是控制面，不是知识仓库。** 大规则放 `references/`，确定性操作放 `scripts/`。
3. **时效性事实先验证。** Release、下载地址、市场价格、竞品状态、法规、产品能力都不能靠旧记忆猜。
4. **第三方只借鉴方法，不复制实现。** 需要保留原项目时用 Reference Index + 原始来源链接。
5. **先验证再工程化。** Visual Lab 通过真实任务验证后，再决定合并、删除或升级成 Productionized Skill。
6. **修改后留下复查路径。** Trigger tests、self-check、案例或 repository audit 至少有一种可重复验证方式。

---

## 🚧 维护边界

本仓库不负责长期维护：

- Codex 官方系统 Skills，例如 `.codex/skills/.system`
- 插件缓存，例如 `.codex/plugins/cache`
- 没有明确维护理由的第三方 Skill 副本
- 只为了增加数量而拆出来、但没有独立职责的 Skill

---

<div align="center">

**Make repeated good decisions reusable.**

<sub>Build our own workflows. Keep references traceable. Verify what matters.</sub>

</div>