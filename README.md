<div align="center">

# self_skills

**让 Agent 在真正需要专业能力时更可靠。**

为个人创作、研发和团队交付沉淀的 Skills：只保留有明确使用场景、可复用知识或工具、可检查交付标准的能力。先解决实际问题，再决定是否对外发布。

[简体中文](README.md) · [English](README_EN.md) · [按需求找 Skill](#按需求选-skill) · [查看全部能力](skills/CHOOSING.md) · [质量与验证](#质量如何证明)

</div>

---

## 按需求选 Skill

**先看你想完成什么，再选 Skill。** 以下 5 个是优先维护的 Core 候选（不是已经通过模型效果认证）。

| 你现在想做什么 | 推荐 Skill | 它能帮你解决什么 | 主要交付 |
|---|---|---|---|
| **需求说不清楚，想交给 Codex / Agent 执行** | [需求提示词整理 · `project-prompt-polisher`](skills/project-prompt-polisher/SKILL.md) | 把口语化需求变成边界清楚、不会无故扩大修改范围的任务 | 可复制的执行提示词、验收条件 |
| **README 很乱，项目文档需要整理或交接** | [项目文档治理 · `internal-project-doc-standardizer`](skills/internal-project-doc-standardizer/SKILL.md) | 梳理现有事实、修复文档缺口，小项目不强制生成一堆空文档 | README / docs 改动、缺口清单、检查结果 |
| **把 Windows 软件整理成 Scoop 安装包配置** | [Scoop 打包 · `app-to-scoop`](skills/app-to-scoop/SKILL.md) | 选择可信下载资源，规划版本、校验值、启动入口及更新规则 | Scoop manifest、验证步骤、待确认信息 |
| **已有照片，想做成有故事感的视觉作品** | [故事化视觉设计 · `visual-story-image-director`](skills/visual-story-image-director/SKILL.md) | 保留人物、场景事实和视觉识别点，规划拼贴 / 杂志风等视觉方向 | 图片分析、生成或编辑方案、质量检查；工具可用时可继续生成 |
| **公众号文章写完了，需要封面和文中配图** | [公众号配图规划 · `wechat-article-image-planner`](skills/wechat-article-image-planner/SKILL.md) | 根据文章段落规划图片种类、风格和插入位置，避免无意义配图 | 封面与插图清单、具体位置、生成提示词 |

> **如果只是修一个 Bug、解释概念或回答简单问题，通常直接向 Agent 提问即可。** 不用为了调用 Skill 而增加步骤。所有 Core 均可按需独立安装。

### 复制一句话试试

<details>
<summary><strong>① 把口语需求变成可执行任务</strong></summary>

```text
使用 project-prompt-polisher，把下面的需求整理成 Codex 可执行的任务提示词；
请明确修改范围、不能改动的内容和验收方法，不要直接修改代码：
“动作编辑器输入框打不出中文，需要修好，但其他功能不要受影响。”
```

</details>

<details>
<summary><strong>② 检查和整理项目 README</strong></summary>

```text
使用 internal-project-doc-standardizer 检查这个项目的 README 和 docs。
先按项目真实规模判断需要哪些文档，指出缺失或过时的内容；
不要虚构接口、开发状态和测试结果。
```

</details>

<details>
<summary><strong>③ 从 Release 制作 Scoop manifest</strong></summary>

```text
使用 app-to-scoop，根据这个项目的官方 Release 制作 Windows Scoop manifest：
<项目链接>。核实版本、资产和 SHA256，无法验证的字段明确标注；
不要执行安装或卸载。
```

</details>

<details>
<summary><strong>④ 把照片转成杂志风叙事视觉</strong></summary>

```text
使用 visual-story-image-director，分析我给的照片并制作旅行记忆风格的视觉方案。
保持人物身份与场景事实，说明构图、风格和编辑约束。
```

</details>

<details>
<summary><strong>⑤ 给定稿公众号文章配置插图</strong></summary>

```text
使用 wechat-article-image-planner，为这篇已经定稿的公众号文章规划封面和配图。
标清图片插在什么段落、为什么需要这张图，并给出不同的生成提示词。
```

</details>

## 还有哪些能力？

除 Core 外，仓库还保留 **12 个 Lab 条目**，用于研究、对照和合并验证，其中有些只是初步方法草案，**不建议直接批量安装**。

| 方向 | 可以探索的能力 |
|---|---|
| **研发与评审** | [工程质量审查](skills/ai-coding-paradigm/SKILL.md)、[代码执行纪律](skills/ai-coding-discipline/SKILL.md)、[项目结构评审](skills/project-structure-review/SKILL.md) |
| **品牌与图片设计** | [角色一致性](skills/consistent-character-designer/SKILL.md)、[品牌视觉系统](skills/brand-visual-system-designer/SKILL.md)、[海报设计](skills/ai-poster-art-director/SKILL.md)、[产品视觉](skills/product-visual-designer/SKILL.md) |
| **视觉分析与通用工具** | [参考图分析](skills/creative-reference-analyzer/SKILL.md)、[图片质量评审](skills/ai-image-quality-reviewer/SKILL.md)、[生图提示词](skills/image-prompt-engineer/SKILL.md) |
| **业务与客户交付** | [商业化分析](skills/market-commercialization-strategist/SKILL.md)、[客户技术报告](skills/client-technical-reporting/SKILL.md) |

另有 [AI 生图外部资源索引](skills/image-generation-collection/SKILL.md)，只供阅读，不是独立可安装 Skill。**[查看 18 项完整的用途、交付内容和成熟度说明 →](skills/CHOOSING.md)**

## 质量如何证明？

我们把「工程检查合格」与「实际让 Agent 做得更好」分开记录，不用文档长度或 Skill 数量当质量评分。

| 检查层级 | 当前结果 | 证据 |
|---|---|---|
| **工程与安全** | 最近一次基线的 Python 回归、目录结构和 Windows 只读测试均通过；最新结果以 CI 为准 | [GitHub Actions](https://github.com/nuoaner/self_skills/actions/workflows/skill-integrity.yml)、[测试代码](tests/) |
| **触发与任务用例** | 已建立 **35 条**中英文正例、反例和代表任务；这是用例集，不是模型运行成绩 | [测试案例](evals/cases.jsonl)、[评测方法](evals/README.md) |
| **实际效果（A/B/C）** | **尚未取得可信的模型对照结果**。不会凭静态测试宣称成功率、速度或 Token 提升 | [评测记录与限制](evals/README.md) |
| **技能去留** | 5 Core 候选 / 12 Lab / 1 参考索引；去留决定可回退，未贸然删除已有调用名称 | [机器可检查的目录](skills/catalog.json)、[维护政策](docs/portfolio-policy.md) |

> 看见“Core”表示**优先维护且具备可安装结构**，不等于第三方认证，也不等于实战效果已经得到证明。公开复用前仍需验证、审核引用资源和明确授权范围。

## 如何开始使用

### 1. 按需安装单个 Skill（Codex 示例）

```bash
git clone https://github.com/nuoaner/self_skills.git
cd self_skills
mkdir -p ~/.codex/skills
cp -R skills/project-prompt-polisher ~/.codex/skills/
```

这是类 Unix 环境的示例；请以本机 Codex 版本实际支持的技能目录为准。安装后可以用上面的自然语言示例调用，**不要直接把整个 `skills/` 目录全部装进去**。

### 2. 在 ChatGPT 中使用

如当前 ChatGPT 工作空间支持自定义 Skill，可先将一个 Core 单独打包，再通过 Skills 界面上传：

```bash
python scripts/package_selected.py project-prompt-polisher --output ./skill.zip
```

这条命令**只生成文件**，不会自动安装、上传、执行代码或修改你的 ChatGPT 设置。不同账号、版本和平台的安装入口可能不同。

### 3. 验证仓库工程质量

```bash
python scripts/catalog.py check
python scripts/audit_skills.py
python scripts/eval_cases.py validate
python -m unittest discover -s tests -v
```

通过这些命令不意味着真实 Agent 效果优秀。想参与实测，可阅读 [首轮真实任务试验与安全执行方法](evals/PILOT.md)。

## 维护与公开范围

仓库遵循 **个人和团队优先使用 → Lab 验证 → Core 维护 → 有证据后公开推广** 的顺序。通用原则交还给模型；只有专业知识、脚本、领域规范、素材与验收约束有真实价值，才值得成为独立 Skill。合并／废弃候选先给迁移方案，不直接破坏原名称。详见 [治理与退出标准](docs/portfolio-policy.md)。

**许可说明：** 仓库虽然公开可读，但目前尚未声明统一的开源许可证；请不要据此推定所有内容都允许复制、修改或商业再分发。引用的第三方资源以原许可为准。

有实际使用反馈、误触发案例或改善建议？欢迎通过 [Issues](https://github.com/nuoaner/self_skills/issues) 提供**脱敏的**问题、预期结果和实际结果。

<div align="center">

*Keep what helps. Test what matters.*

</div>
