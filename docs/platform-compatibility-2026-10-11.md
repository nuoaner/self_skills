# 已验证的 Skill 平台约定（2026-10-11）

以下区分官方文档、平台专有功能和本仓库选择；请勿把后两类冒充为通用协议。

| 项目 | 类别 | 已核实要点 |
|---|---|---|
| `SKILL.md` + `name` / `description` | Agent Skills / OpenAI API 基础 | 用于发现与路由；文件正文及其他资源按需加载 |
| `references/`、`scripts/`、`assets/` | 推荐组织方式 | 按需提供，不是每个 Skill 必须拥有 |
| `agents/openai.yaml` 中的 `interface` | ChatGPT/Plugin 扩展 | 用于 ChatGPT UI 元数据与部分依赖；不是所有运行环境共通的 frontmatter 字段 |
| `VERSION` | 本仓库自定义 | 方便人工追踪；不能宣称是通用 Skill 协议强制文件 |
| 单个 ZIP 含单个 Skill | OpenAI Skills API 格式 | 不应把仓库所有目录作为一项 Skill 上传 |
| ChatGPT 分享与安装 | 产品特定 | 以当前 Skills UI 与账号/工作空间权限为准，不能假设和 Codex 目录复制完全相同 |
| 执行脚本与外部工具 | 平台/环境能力 | 仅在实际具备权限、依赖和运行时使用；高风险写入另需保护 |
| 最大上传容量 | 依产品/入口而异 | OpenAI Skills API 文档说明 ZIP 50 MB；内置 Skill 创建工具可采用更严格的 25 MB 打包上限，不能混写 |

官方资料（本轮在线核验）：

- [OpenAI API Skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Plugins: Build skills](https://developers.openai.com/plugins/build/skills)
- [ChatGPT Skills Help](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)

**未核实：** 用户具体 ChatGPT 工作空间的安装权限、当前 Codex 客户端可搜索的技能目录、工具额度与是否支持远端真实 Agent 评测。相关环境未验证前，不在 CI 或文档中宣称完全兼容。
