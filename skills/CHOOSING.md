# 我该选哪个 Skill？ / Choose a Skill

> 这里按**用户要完成的任务**组织，而不是按照技术术语堆名字。仓库采用 [Core / Lab / Reference 分层](catalog.json)，本页只说明能力和限制，不代表所有条目都已通过效果验证。

[回到中文首页](../README.md) · [English homepage](../README_EN.md) · [工程验证与效果评测](../evals/README.md)

## 优先尝试：Core（5 项）

Core = 优先维护、有完整可安装结构的候选能力；尚无真实 A/B/C 对照成绩。

| 你要完成的事 | Skill | 适合提供的输入 | 可以期待的交付 | 不适合的情况 |
|---|---|---|---|---|
| 模糊需求整理成 Codex / Agent 任务 | [project-prompt-polisher](project-prompt-polisher/SKILL.md) | 口语需求、截图文字、已有项目约束 | 清晰任务目标、范围、不应改动的内容、验收方法 | 已明确让 Agent **直接修改代码** |
| 项目 README、docs 规范化或交接 | [internal-project-doc-standardizer](internal-project-doc-standardizer/SKILL.md) | 项目目录、现有 README、开发文档 | 按项目规模选择精简/完整文档，标出缺口和检查记录 | 单纯写营销文章、修复代码 |
| 制作 Windows Scoop 软件清单 | [app-to-scoop](app-to-scoop/SKILL.md) | 官方软件页、GitHub Release、manifest 或报错 | manifest、下载与架构选择、可验证的 Hash / 待确认项 | 只想了解 Scoop 是什么或直接安装它 |
| 用现有照片制作视觉叙事 | [visual-story-image-director](visual-story-image-director/SKILL.md) | 原照片、要保留的主体与用途 | 源场景分析、视觉方向、可执行编辑/生成 brief、质量复核 | 没有源图、只要求解释图像工具 API |
| 根据文章内容安排封面与配图 | [wechat-article-image-planner](wechat-article-image-planner/SKILL.md) | 定稿/接近定稿的公众号文章 | 封面与文中图片清单、插入位置、不同图片的提示词 | 文章还没写，只要帮忙构思选题 |

## 还在验证：Lab（12 项）

> Lab 不代表“差”，而是**独立价值、触发范围或可安装性还没有得到充分验证**。有些仍是草案，仅用于查阅；有些保留兼容调用名称。谨慎使用。

### 工程审查与交付

| Skill | 想解决的事 | 预期帮助 | 当前去向 |
|---|---|---|---|
| [ai-coding-paradigm](ai-coding-paradigm/SKILL.md) | 评估架构、测试、安全和交付风险 | 基于证据的技术风险清单和修复建议 | 增强后测量 |
| [ai-coding-discipline](ai-coding-discipline/SKILL.md) | 开发时复用现有代码、控制改动边界 | 约束回归风险、保留安全边界 | 考虑转入项目级 `AGENTS.md` |
| [project-structure-review](project-structure-review/SKILL.md) | 判断仓库是否便于交接和验收 | README、依赖、入口与目录检查 | 候选合入工程评审能力 |

### 角色、海报与品牌

| Skill | 想解决的事 | 预期帮助 | 当前去向 |
|---|---|---|---|
| [consistent-character-designer](consistent-character-designer/SKILL.md) | 多张图保持同一人物/IP 特征 | 固定身份特征、管理场景变量 | 补样本与一致性实测 |
| [brand-visual-system-designer](brand-visual-system-designer/SKILL.md) | 长期维持统一品牌视觉风格 | 统一配色、布局和资产规则 | 补品牌系统范例 |
| [ai-poster-art-director](ai-poster-art-director/SKILL.md) | 活动、宣传海报的内容层级与视觉方向 | 信息优先级、排版与留字区域 | 实验与打样 |
| [product-visual-designer](product-visual-designer/SKILL.md) | 产品主图、落地页视觉表达 | 突出产品价值和传播目标 | 需要验证商业场景增益 |

### 图像方法与质量

| Skill | 想解决的事 | 预期帮助 | 当前去向 |
|---|---|---|---|
| [creative-reference-analyzer](creative-reference-analyzer/SKILL.md) | 分析参考图的构图和视觉语言 | 提取可借鉴的设计逻辑 | 候选合入故事化视觉能力 |
| [ai-image-quality-reviewer](ai-image-quality-reviewer/SKILL.md) | 诊断生成图与目标不符的问题 | 检查主体、构图、一致性和可用性 | 候选作为共享 QA 参考 |
| [image-prompt-engineer](image-prompt-engineer/SKILL.md) | 将模糊生图需求组织成提示词 | 视觉目标与约束说明 | 候选退出独立 Skill |

### 商业分析与客户沟通

| Skill | 想解决的事 | 预期帮助 | 当前去向 |
|---|---|---|---|
| [market-commercialization-strategist](market-commercialization-strategist/SKILL.md) | 产品定位、市场、留存及定价策略 | 区分事实、推断和假设的行动建议 | 需要和通用 Agent 做对照 |
| [client-technical-reporting](client-technical-reporting/SKILL.md) | 向客户说明项目迁移、接口和遗留问题 | 客户可理解的交付报告 | 候选转为按需报告模板 |

## Reference（1 项）

[image-generation-collection](image-generation-collection/SKILL.md) 是第三方 AI 图像项目的**外部资料索引**，不是可安装的独立 Skill。所链接项目的授权、维护状态和实际质量以原始来源为准。

## 怎么决定要不要安装？

1. **使用场景是否符合？** 没有源照片就不必装故事化视觉；只问什么是 Scoop 就不必装打包 Skill。
2. **不用 Skill 是否已经足够？** 如果模型能稳定完成任务，优先直接提问。
3. **有专业资产或工具吗？** 对特殊领域知识、脚本、模板、可验证检查有需求时，Skill 才可能带来独立增益。
4. **只安装一个实际需要的条目。** 不建议复制整个 `skills/` 目录；实验草案可能缺少 frontmatter，无法正常触发。
5. **提出反馈时给具体例子。** 用户输入、期待结果、实际结果与可公开的脱敏证据，比“感觉不好用”更利于修复。

**质量依据**：[GitHub Actions](https://github.com/nuoaner/self_skills/actions/workflows/skill-integrity.yml) 检查的是结构与确定性脚本；[35 条评测案例](../evals/cases.jsonl) 仍需真实 Agent 执行。**不以本页的能力描述宣称已经测得性能提升。**

返回：[中文首页](../README.md) · [English homepage](../README_EN.md)
