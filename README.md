# self_skills

**个人与团队优先、成熟后公开的 Agent 专业能力库。** Skill 只保留有独立价值的知识、工具、专业流程与验收依据。不会因为模型发布新版本就机械重写所有 Skill。

## 从哪里开始

完整名单与去留判断以 [Skill 能力清单](skills/CATALOG.md) 为准；它由 [唯一分类数据源](skills/catalog.json) 自动生成。历史版本曾将 10 项标为工程化、7 项标为 Visual Lab、1 项标为参考索引；**现在重新采用 Core / Lab / Reference 分层**，两种统计口径不能混用。

- **Core（核心维护候选）**：优先服务真实工作；有明确职责与可复用资源，但仍须通过 Agent 效果评测，不代表已经验证性能提升。
- **Lab（实验与整合区）**：显式测试；包括原先正式但独立价值有待验证的 Skill，以及尚未具备安装元数据的视觉草案。带有迁移意向的不直接删除。
- **Reference（参考索引）**：收录外部素材与来源，**不作为 Skill 安装**。

## 快速查看和验证

```bash
git clone https://github.com/nuoaner/self_skills.git
cd self_skills
python scripts/catalog.py list
python scripts/catalog.py check
python scripts/catalog.py check-docs
python scripts/audit_skills.py
python scripts/eval_cases.py validate
python -m unittest discover -s tests -v
```

上述测试验证清单、文件结构和确定性脚本，**不能证明 Agent 实际效果提升**。可复现的 A/B/C 对比方式见 [效果评测](evals/README.md)。

## 如何使用

通过 [核心清单](skills/CATALOG.md) 找到需要的单个 Skill；**只安装实际使用的核心项**。在 Codex 支持的技能目录放置完整技能文件夹；ChatGPT 则按当前界面中的技能创建／上传流程逐个安装。不同平台的安装入口、元数据和容量限制不应混为一个统一协议。实验草案若缺少 `SKILL.md` frontmatter，则不可当作可安装技能。

本仓库原有的 `skills/<name>` 路径和调用名称保持不变；合并候选目前只记录迁移方向，**未执行删除**。参见 [分层与淘汰规则](docs/portfolio-policy.md) 和 [平台兼容性说明](docs/platform-compatibility-2026-10-11.md)。

## 贡献、质量与安全

- 新增或修改 Skill，先说明相较无 Skill 的**独立收益**；不要因为可以描述一个流程，就创建一个新的 Skill。
- `SKILL.md` 保留清晰触发边界；领域资料、模板和确定性操作按需放到 `references/`、`assets/`、`scripts/`，不要求每个 Skill 都具备所有目录。
- 发布前核查第三方授权、个人／公司信息、凭据与素材来源。只借鉴方法，不把外部项目换名后宣称原创。
- 真实测试需保留相同模型与工具条件、脱敏证据、质量评判与失败案例。没有数据就标为“未测”，不编造提升比例。
- 高风险操作需明确授权；Scoop manifest 测试默认为只读，禁止测试脚本自动卸载应用。

仓库升级在 [PR #4](https://github.com/nuoaner/self_skills/pull/4) 独立审核，未直接覆盖 `main`。历史改动见 [CHANGELOG](skills/CHANGELOG.md)。
