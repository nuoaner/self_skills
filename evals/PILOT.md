# 第一批真实 Agent 评测 / Phase 2 Codex pilot

**目的：让“Skill 值不值得留”由真实任务结果决定，而不是靠提示词长度、章节数量和直觉。**

当前先测两个最有代表性的 Core：

| Skill | 真实问题 | 预期结果 | 非回归重点 |
|---|---|---|---|
| `project-prompt-polisher` | 机器人动作编辑器中文输入法无法正常输入 | 清晰、可交给 Codex 的修复提示词 | 不编造代码文件、不直接改代码、提供可验证的中文输入/英文输入回归检查 |
| `internal-project-doc-standardizer` | 很小的 Python 项目 README 存在失效链接和错误运行命令 | 基于真实文件的审计与精简修正建议 | 不强制创建 10 个空文档、不编造测试或 API、只审计不修改 |

第一个案例：`project-prompt-polisher-05`。第二个案例：`internal-project-doc-standardizer-05`；后者使用 [公开虚构夹具](fixtures/docs-small/README.md) 与 [实际入口文件](fixtures/docs-small/main.py)，故意包含坏链接和错误的运行命令。该夹具不包含私人数据。

## 为什么做 A / B / C？

| 分组 | 使用的内容 | 需要观察 |
|---|---|---|
| **A：无 Skill** | 同一模型、同一任务资料，没有目标 Skill | 模型已有能力是否足够 |
| **B：旧版 Skill** | 旧版固定 Git commit 的目标 Skill | 原 Skill 是否帮助还是拖累 |
| **C：候选 Skill** | 当前工作分支目标 Skill | 修改后是否真正改善 |

模型、提示词、沙盒与可用文件应完全一致；自动触发和显式调用要分开评估。先做**文本与只读任务**，不在公开测试中安装软件或访问客户资源。

## 第一步：免费检查计划（不执行模型）

从仓库根目录执行：

```bash
python scripts/pilot_codex_eval.py plan --case project-prompt-polisher-05
python scripts/pilot_codex_eval.py plan --case internal-project-doc-standardizer-05
```

会打印分组、旧版提交、预期调用数、沙盒和证据路径。**不会调用 Codex，不消耗模型额度，不写测试结果。**

## 第二步：仅在你明确同意额度消耗后执行

需要你自己的 **Codex CLI**、可用的模型及已配置的 `CODEX_ACCESS_TOKEN` 或 `OPENAI_API_KEY` 环境变量。不要将令牌粘贴到 Issue、README、聊天或提交中；脚本不会复制 `~/.codex/auth.json`。执行命令仅为示例，模型名称请替换为当前账号能够访问的实际型号。

```bash
# 先确认本机有 Codex，历史 Git commit 可读取
codex --version
git cat-file -e 071a082163d942e270b82e0e89ed2b8521fc21d7^{commit}

# 在已授权并知晓费用的环境中执行：每个案例 3 组 × 1 次 = 3 次真实模型调用
python scripts/pilot_codex_eval.py run \
  --case project-prompt-polisher-05 \
  --model YOUR_AVAILABLE_MODEL \
  --confirm-billable

# 文档审核任务也可单独进行
python scripts/pilot_codex_eval.py run \
  --case internal-project-doc-standardizer-05 \
  --model YOUR_AVAILABLE_MODEL \
  --confirm-billable
```

后续可用 `--repetitions 3` 取得更有价值的重复样本（9 次模型调用/案例）；脚本最多允许 3 次重复，且不会并发爆量执行。

**安全约束：** 以临时隔离的 `CODEX_HOME` 和工作目录执行，模型命令采用 `--sandbox read-only`。A 不安装 Skill；B 读取固定旧 commit 的 Skill；C 从当前仓库复制目标 Skill。该设置降低写盘风险，但**不能取代对模型、第三方 Skill、账号、网络权限和凭据暴露的审查**。请只运行可信材料。

## 第三步：独立验收，不自动打分

原始 `trace.jsonl`、`metadata.json`、错误信息会写在 git 忽略的 `evals/runs/` 下。脚本**只记录真实执行情况，绝不会根据关键词自动声称 Skill 已触发、成功或效率提升**。

运行结束后，至少检查：

1. **任务成功**：是否符合案例中预先写好的 `acceptance`？
2. **专业性**：是否识别中文输入组合态问题，或能辨认 fixture 中的实际运行入口和坏链接？
3. **安全和边界**：是否编造代码路径、测试结果，是否要求不必要权限或创建空文档？
4. **自主性**：是否出现不必要的确认和多余工作？
5. **效率**：根据真实 trace 计算工具调用、时间、可用时的 Token 消耗；有异常或失败也保留。

使用 [人工复核表](pilot-review-template.md) 记录**脱敏**评语。只有结果经过独立判定，才按 [正式结果格式](README.md) 填写 A/B/C 记录，并使用 `scripts/eval_cases.py report --results <your-file.jsonl>` 形成汇总。不要将原始 Prompt、商业代码、私人文件和 API Key 提交公开仓库。

## 当前真实状态

本阶段已经建立可复验的案例、固定旧版锚点、读取真实 fixture、隔离运行和证据留存通道。**截至目前未运行付费模型调用，尚没有可公开声称的质量改善比例。**

参考：[OpenAI 官方《Testing Agent Skills Systematically with Evals》](https://developers.openai.com/blog/eval-skills)；[Codex CLI 参考](https://learn.chatgpt.com/docs/cli/reference)。
