# Skill Trigger Test Examples

这些样例用于人工或脚本审计 skill 触发边界。每个 skill 至少包含 should-trigger 和 should-not-trigger，用来避免过度触发或漏触发。

## wechat-article-image-planner

Should trigger:
- "This is my finalized WeChat article. Please plan the cover image and three inline illustrations."
- "公众号文章已经定稿了，帮我做配图规划，输出 imagegen2 prompts。"
- "根据这篇文章生成公众号封面和文中插图，用 imagegen2。"

Should not trigger:
- "帮我从零写一篇公众号长文，先不用考虑配图。"
- "生成一张普通产品海报，不是公众号文章配图。"

## ai-coding-discipline

Should trigger:
- "帮我把这个功能工程化实现，代码写稳一点，不要重复造轮子。"
- "这个模块需要重构，但要先设计边界和验证方式。"
- "请按规范写代码，注意错误处理、复用和可维护性。"

Should not trigger:
- "解释一下这段代码是什么意思，不需要修改。"
- "给我写一段市场推广文案。"

## ai-coding-paradigm

Should trigger:
- "帮我评估这个项目的工程成熟度和架构边界。"
- "这个系统的测试、可观测性和安全姿态怎么样？"
- "帮我分析一下模块设计和实现 tradeoff。"

Should not trigger:
- "把这个 README 翻译成英文。"
- "生成一张产品宣传海报。"

## app-to-scoop

Should trigger:
- "用 app-to-scoop 把这个 GitHub Release 做成 Scoop manifest。"
- "帮我把这个官网下载页打包成 bucket/app.json，并补 checkver 和 autoupdate。"
- "这个 Scoop manifest 安装报 Hash check failed，帮我修一下。"

Should not trigger:
- "解释一下 Scoop 是什么。"
- "帮我写一个 winget manifest。"

## client-technical-reporting

Should trigger:
- "帮我整理一份给甲方看的技术汇报，说明本次做了什么、怎么迁移、后续接口在哪改。"
- "把这次联调进展整理成客户能看懂的交付说明。"
- "给客户写迁移总结，包含问题定位和后续确认事项。"

Should not trigger:
- "帮我写内部日报，越口语越好。"
- "优化这个登录接口的参数校验。"

## internal-project-doc-standardizer

Should trigger:
- "帮我把这个项目 README 标准化，并把详细内容拆到 docs。"
- "检查项目文档是否符合内部规范。"
- "初始化一套标准 README、docs 和 agent.md。"

Should not trigger:
- "帮我修复一个前端按钮错位问题。"
- "帮我写一份销售转化分析。"

## market-commercialization-strategist

Should trigger:
- "从市场经理角度看看这个产品怎么吸引用户并形成商业闭环。"
- "帮我评估这个功能是否适合商用，怎么定价和推广。"
- "优化 landing page 的用户吸引、留存和转化路径。"

Should not trigger:
- "帮我写单元测试。"
- "把项目目录结构整理成树形图。"

## project-prompt-polisher

Should trigger:
- "帮我把这个需求改成更清晰的 Codex 执行 prompt。"
- "这个提示词太散了，帮我优化成可交给另一个智能体执行的版本。"
- "把我的中文任务描述润色成实现级 prompt，包含验收标准。"

Should not trigger:
- "直接帮我实现这个功能，不需要改 prompt。"
- "解释一下 prompt engineering 是什么。"

## project-structure-review

Should trigger:
- "帮我审查这个项目结构是否符合交付规范。"
- "准备提交前检查目录、README、依赖说明和架构图是否完整。"
- "帮我把仓库结构标准化，适合交付或评审。"

Should not trigger:
- "帮我写一个接口。"
- "帮我设计产品商业化路线。"
