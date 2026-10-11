---
name: discover-course-ppt
description: Create or revise branded technical teaching PowerPoint decks for DISCOVER Robotics / 求之科技 courses, using supplied course materials, the bundled reference deck, and bundled brand assets. Use when the user asks to turn a lesson plan, DOCX, Markdown, technical notes, experiment logs, screenshots, data, or an existing PPT into a classroom-ready .pptx; when they ask to extend a course series in the same style; or when they ask to audit a course deck for teaching clarity, brand consistency, diagrams, sources, layout density, or speaker notes.
---

# 求之科技课程 PPT

把课程材料转成可以直接授课的技术课件。优先保证：知识讲清楚、关系画准确、品牌统一、来源可追溯、页面可投影、讲师能照着备注讲。

## P0 质量合同

以下 10 条是不可降级规则。任何一条不满足，都不能视为完成：

1. **先完整覆盖知识，再决定页数。** 先做知识清单与覆盖映射，不得先定页数后删减内容。
2. **一个概念必须解释职责、输入、输出和工作机制。** 若某项不适用，用作用对象、依赖条件或判定方式替代，但不能只放术语。
3. **抽象知识优先配图，不只放术语。** 架构、闭环、时间尺度、训练循环、状态关系和参数影响优先视觉化。
4. **流程、闭环逐节点解释，箭头必须语义准确。** 每条边先写成 `源节点 --[传递内容]--> 目标节点` 再绘制。
5. **组成关系、流程关系、状态关系不能混画。** 先判定关系类型，再选择分组、树状、流程、状态机或反馈闭环。
6. **页面要饱满，但靠教学信息丰富，不靠堆文字。** 普通内容页目标占用正文安全区约 65%–85%；不足时优先补职责、输入输出、机制、条件、判据、案例或视觉。
7. **缺图时保留设计好的图片/图表占位区。** 占位区必须写明需要什么素材、建议画面/字段、比例和来源状态。
8. **所有外部事实、数据、图表和计算结果必须可追溯。** 来源与知识点同时规划；没有来源就标 `待补`，不得猜。
9. **先定页面视觉语法，再摆元素。** 每页只能有一个主视觉结构；先确定关系类型、阅读路径和主图，再放卡片、文字和箭头。禁止“几个知识点就画几个框”的散点式卡片墙。
10. **教师模板优先于自由排版。** 正式课程 PPT 优先套用教师模板的固定网格和成熟页型；只有基础页型无法准确表达知识关系时，才自定义架构图、闭环图或时间轴。

执行细节见 `references/content-coverage-contract.md`。

## 资源导航

开始制作前按需读取：

- 教师模板约束（正式版式最高优先级）：`references/teacher-template-contract.md`
- 教师原始模板说明（需要精确命名/交付细节时读取）：`references/teacher-template-usage.md`
- 品牌与版式：`references/brand-guidelines.md`
- 参考课件拆解：`references/template-analysis.md`
- 内容覆盖与页面规划：`references/content-coverage-contract.md`
- 教学写作规则：`references/teaching-writing-rules.md`
- 页面构图语法：`references/page-composition-grammar.md`
- 页面类型与版式：`references/slide-archetypes.md`
- 图示、箭头、图片与图表：`references/visual-and-diagram-rules.md`
- 图示语义案例与反例：`references/diagram-semantics-examples.md`
- 数据、图片与事实来源：`references/citation-rules.md`
- 讲师备注：`references/speaker-notes.md`
- 交付前检查：`references/quality-checklist.md`

输出时使用：

- 教师正式模板：`assets/teacher-course-template.pptx`
- 扩展教学参考：`assets/reference-deck.pptx`
- 品牌图片：`assets/brand/`
- 元数据修正：`scripts/apply_ppt_metadata.py`
- PPT 自动检查：`scripts/validate_course_ppt.py`

## 工作流

### 1. 先锁定材料边界

1. 读取用户提供的教案、课件、Markdown、实验数据、截图、日志和图片。
2. 把内容分为：用户材料明确支持、需要解释但可从材料推导、材料未提供。
3. 保留原材料的术语、结构和口径。不要擅自替换、纠正或补齐用户材料中的事实。
4. 用户明确要求外部研究、核实或扩展时，才加入外部信息，并与课程材料来源明确区分。
5. 缺数据、缺图片、缺实验结果时，保留设计位或标记“待补”，不得编造。

### 2. 先做知识覆盖表，再设计教学链和页数

1. 按 `references/content-coverage-contract.md` 把材料拆成可独立教学的知识点。
2. 为每个知识点记录来源、重要级、前后关系、视觉形式和页面去向。
3. 先确保所有主知识点都有去向，再决定总页数。不得先限定页数再压缩、合并或删除关键知识。
4. 把知识点组织成适合授课的链路，不要机械地一页对应一段原文。常用顺序：

`课程定位 → 学习目标 → 前置知识 → 核心概念/机制 → 完整流程 → 操作画面/案例 → 参数或数据 → 原因分析 → 故障与边界 → 验收 → 场景迁移 → 总结与下节衔接`

只使用当前课程真正需要的页面。内容不足且逻辑连续时合并；知识量大时允许自然增加页数。

### 3. 每个知识点必须在页面内讲明白

页面上的知识不能只出现名词。每个实质性概念、模块或机制至少要让学生看懂：**职责、输入、输出、工作机制**。若某项对该概念不适用，用作用对象、依赖条件或判定方式替代。

对一眼看不懂的内容，再补充必要的定义、位置、原因、判断标准、例子或图示。抽象知识优先视觉化，不要为了“简洁”删除解释。

流程、闭环、系统架构尤其需要说明：

- 每个节点负责什么；
- 输入是什么，输出是什么；
- 箭头表示数据、控制命令、物理动作还是反馈；
- 条件分支何时发生；
- 闭环如何回到前面的节点。

不要用一个名词替代讲解。详细规则见 `references/teaching-writing-rules.md` 和 `references/visual-and-diagram-rules.md`。

### 4. 先选教师模板页型，再决定是否需要自定义图示

正式课件先读取 `references/teacher-template-contract.md`。对每页先判断是否能直接落入教师模板的成熟页型：

`封面 / 学习目标 / 分节页 / 左文右图 / 双栏对比 / 图表+解读 / 故障网格 / 小结与预告`。

能够表达清楚时，优先使用这些固定页型，不要为了“视觉丰富”重新发明复杂构图。基础页型无法准确表达架构、闭环、时间尺度或多对一汇合时，才读取 `references/page-composition-grammar.md` 写“页面构图卡”。

自定义图示仍强制遵守：

- 一页只有一个主视觉结构；
- 视觉层级最多两层：主视觉 + 辅助解释；
- 主节点默认 3–6 个，主连接线不超过 7 条；超出时优先拆页；
- 同级节点必须同尺寸、同对齐、同连接方式；
- 多输入必须通过明确汇合点进入共同输出；
- 禁止散点式卡片墙、蛇形箭头和“所有文字都装进圆角框”；
- 页面关系不明确时，先重构知识关系，不通过增加卡片来掩盖问题。

例如 FSM 与 Policy 页面：FSM 状态应先放入同一个“模式集合”容器，再由“当前模式”作用于 Policy；不得把 `INIT → IDLE → LOCO → FAULT → Policy` 画成一条连续流程。

### 5. 标题短，结论清楚

每页使用两级标题：

- 左上栏目标题：中文优先 2–8 个字，尽量不超过 10 个字；只负责分类，如“核心概念”“流程”“参数”“案例”“验收”。
- 页面主标题：单行 28–32 pt，优先表达本页要讲清楚的结论或问题。

标题过长时先改写，其次拆页。不要靠持续缩小字号解决。

### 6. 语言保持教师自然讲解感

可见文字和 Speaker Notes 都禁用“不是……而是……”句式。避免通过贬低 A 来拔高 B。

优先写成：

- “A 负责……，B 负责……”
- “A 适用于……；B 适用于……”
- “在当前场景中重点关注……”

避免空泛拔高、营销口号和明显 AI 腔。不要写“这不仅是……更是……”“真正重要的是……”“开启全新时代”等没有教学信息的句子。

### 7. 视觉内容优先于无意义留白

页面需要图、图表、截图、设备实拍或流程图时，按以下优先级使用：

1. 用户提供的真实图片、截图、实验图；
2. 与知识点匹配的品牌资产；
3. 根据材料制作的示意图、流程图、结构图或基于真实数据制作的图表；
4. 没有合适素材时，保留“设计型图片占位区”。

设计型占位区不是空白矩形。必须写清：

- 待补素材类型；
- 建议展示内容；
- 建议比例或构图；
- 来源状态，例如“来源：待补”。

示例：`【实拍图待补｜夹爪闭合并成功夹住方块的状态】`。

不要因为没有图片就把整页变成纯文字，也不要为了填满页面编造图片或数据。

### 8. 图表保留为可复用设计

有真实数据时，选择能回答本页问题的图表，并保留图表标题、单位、必要的比较标签和数据来源。

图表旁必须有解释，至少说明“看到了什么”和“为什么”。优先使用：

- 类别比较：柱状图；
- 时间变化：折线图；
- 单次构成且类别较少：饼图；
- 两个数值变量关系：散点图。

如果原始材料没有数据，不得生成伪数据图。保留图表占位区，写明需要补充的数据字段和来源。

### 9. 连线必须同时满足“语义正确 + 几何准确”

画任何流程、闭环、架构或控制图之前，先写出边清单：`源节点 --[传递内容]--> 目标节点`。只有语义成立时才画线。

每条线同时满足：

- 起点贴到源节点边界，终点箭头贴到目标节点边界；不要让箭头悬空在两个卡片之间；
- 箭头方向与真实信息流、控制流或物理动作一致；
- 边标签写“这条线正在传递什么”，不要写成下一节点才产生的结果；
- 反馈线明确回到具体输入节点，不能只回到一片区域；
- 并行关系不用串行箭头强行连接；
- 多输入汇合时显示汇合关系；
- 条件跳转在边上标出条件；
- 走线尽量水平/垂直，避免穿过文本、卡片和其他箭头；
- 同一页的边距、箭头头型、线宽、标签位置保持一致。

绘图完成后逐边复核一次：从箭尾读到箭头，口头说出“谁把什么送给谁”。说不通、看不出连接对象、标签与传递物不一致，均视为未通过。详细规则见 `references/visual-and-diagram-rules.md`；遇到架构、状态机、PD/控制闭环时同时读取 `references/diagram-semantics-examples.md`。

### 10. 按品牌系统排版

默认使用 `references/brand-guidelines.md` 中的求之科技规范：白底、主青短横条、右上 DISCOVER Robotics 标识、左下页码细线、页底出处。

优先直接使用 `assets/brand/` 中的原始品牌文件，不拉伸、不重绘、不自行改色。

主题匹配时自动调用：

- 机械臂本体：`assets/brand/airbot_play_render.png`
- 夹爪：`assets/brand/gripper_render.png`
- 产品字标：`assets/brand/airbot_wordmark.png`
- 普通白底标识：`assets/brand/discover_logo.png`
- 深色底标识：`assets/brand/discover_logo_white.png`

正式版式优先以 `assets/teacher-course-template.pptx` 为母版参考；`assets/reference-deck.pptx` 只参考教学展开深度与实训内容组织。复制设计语言，不复制无关课程内容。

### 11. 控制页面信息密度，避免“内容缩在上半页”

避免两种极端：大面积没有教学作用的留白，以及靠小字号硬塞满页面。

普通技术内容页默认让“有教学作用的内容块”占安全内容区约 65%–85%。除封面、章节过渡和刻意留白页外：

- 不要把主体图、流程或卡片缩在页面上半部，下面留下半页空白；
- 主视觉/主流程应占正文区约 50%–70% 的宽或高，确保投影时一眼能看清；
- 页面至少形成两层信息：`主知识对象` + `解释/例子/判断/参数/易错点/数据解读` 中至少一层；
- 当材料有足够信息时，优先补充节点职责、输入输出、为什么、怎么判断、案例或关键参数，而不是扩大空白；
- 当材料不足以支撑更多事实时，用设计型图片/图表/案例占位区明确“需要补什么”，不要编造；
- 图表、流程图、示意图旁边保留必要解释，不能出现“小图 + 大空白”；
- 内容仍然不足时，宁可合并为更完整的一页，也不要强行拆成稀疏的多页。

正文应在教室投影条件下可读；来源可以更小，但正文和表格不得因内容过多持续缩小。一页出现两个互不依赖的大知识点时再优先拆页。

### 12. 所有数据和外部素材可追溯

出现实验数据、行业数据、论文结论、统计图、第三方图片或外部事实时，按 `references/citation-rules.md` 标注来源。

没有来源时写“来源：待补”，不要猜出处。

### 13. 每页生成 Speaker Notes

备注用于教师真正授课，不是把页面文字重复一遍。至少包含：

- 建议讲解顺序；
- 关键数字或结论；
- 容易混淆的点；
- 必要的课堂提问与参考回答；
- 与前后页的衔接。

详见 `references/speaker-notes.md`。

### 14. 区分草稿与正式交付

默认把用户明确要求“交付/送审/正式课件”的任务视为 `formal`，其余首次试制可按 `draft`。

- `draft`：允许带明确说明的图片/图表占位、`待补/待核实`、内部短文件名；仍禁止虚构数据和错误关系。
- `formal`：优先消除泛化占位框；页码总数、来源、真机待补、品牌色、标识尺寸、文件命名和元数据必须完整；逐页渲染检查后再交付。
- 用户明确要求保留占位时，用户要求优先，但占位必须说明待补内容和来源状态。

详细规则见 `references/teacher-template-contract.md`。

### 15. 生成并检查 PPTX

用户要求成品 PPT 时，必须生成可下载的 `.pptx`，不能只交提纲。

完成后：

1. 用 `scripts/apply_ppt_metadata.py` 写入规范元数据；
2. 用 `scripts/validate_course_ppt.py` 做自动检查；
3. 逐页渲染检查可视结果；
4. 修复重叠、裁切、文字过密、空白过大、箭头错误、来源缺失和占位区不明确的问题；
5. 再交付最终文件。

## 关键硬约束

以下问题视为未通过：

- 先定页数导致主知识点被删、被一句话带过或没有页面去向；
- 实质性概念只有定义/术语，没有职责、输入、输出、机制（或等价解释）；
- 抽象知识本可用图讲清，却只剩名词列表且没有合理原因；
- 使用“不是……而是……”；
- 左上栏目标题明显过长；
- 流程或闭环只标名词，没有解释节点；
- 箭头方向或含义无法解释；
- 数据或第三方图片没有来源；
- 缺图时留下无意义的大块空白；
- 普通内容页主体只占上半页/一角，导致明显失衡；
- 一页存在两个以上互相争夺注意力的主视觉结构；
- 明明可用教师模板成熟页型表达，却自行堆叠复杂卡片、胶囊和多套流程；
- 学习目标页被拆成多个装饰卡片，未按“动作 + 对象 + 量化标准”形成清晰列表；
- 图表页同时放多组数据/多张同权重图表，导致主结论不明确；
- 多个同级概念采用散点式卡片布局，没有规则网格、父容器、主轴或明确中心；
- 同级节点尺寸、对齐或连接方式明显不一致；
- 多输入汇合没有明确共同出口/汇合节点，只是把线画到某个模块附近；
- 流程图或架构图的连线悬空、连错节点、标签错位或边语义不成立；
- 缺数据时自行编造图表；
- 品牌 Logo 变形、变色或错用；
- 页面正文小到不适合课堂投影；
- Speaker Notes 只是重复页面；
- 未做最终视觉检查就交付。

## Engineering QA gates (mandatory for PPTX delivery)

Treat course quality and PPTX engineering as separate responsibilities. Preserve all teaching rules above, then apply these additional gates before delivery.

1. Before using any teacher/customer template, run `scripts/pptx_template_inventory.py` and map content to mature existing archetypes first.
2. Run `scripts/pptx_content_audit.py` to catch generic placeholders, empty slides, and accidental repeated titles.
3. Run `scripts/pptx_font_preflight.py` and review any font substitutions that could affect wrapping or fit.
4. Run `scripts/validate_course_ppt.py`. When derived from a template, pass `--original <template.pptx>` so inherited package defects are separated from new regressions.
5. The course validator now includes PPTX package-integrity checks for broken relationships, slide/layout references, notes reuse, content-type coverage, and other structural risks.
6. Render the latest file and inspect every slide after the structural checks pass.
7. After any XML-level or template-structure edit, repeat structural validation and visual QA.

Use `references/pptx-engineering-gates.md` for the complete workflow. The final acceptance model is: teaching semantics correct + PPTX package stable + rendered appearance clean.
