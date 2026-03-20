# 企业 AI Agent / Workflow / Skills 最佳实践方案

## 1. 方案定位

本方案面向中小企业 AI 入门培训、行政办公 AI 实操培训，以及基于 Agent / Workflow / Skills 的内容生产场景落地。

适用范围包括：

- 文案生成
- 图片创意与提示词生成
- PPT 结构与页面内容生成
- 视频选题、口播稿、分镜与发布文案生成

本方案的核心目标不是一开始就搭建“万能 Agent”，而是先建立：

**可复用的 Skills → 稳定的 Workflow → 必要时再由 Agent 进行调度。**

---

## 2. 一句话总原则

**能固定就 Workflow，需判断才 Agent；能复用就做成 Skill；先评估再扩张；高风险必须审批和人工兜底。**

---

## 3. 三层方法论

### 3.1 Skill 定义

Skill 是一个**最小可复用能力单元**，用于完成单一、明确、可重复的任务。

例如：

- 活动 brief 提取
- 文案初稿生成
- 文案审校
- 图片提示词生成
- PPT 目录生成
- 视频口播稿生成

Skill 不应该是“万能助手”，而应该是一把清晰的小工具。

#### Skill 的标准组成

每个 Skill 建议包含：

- `name`
- `description`
- 适用场景
- 不适用场景
- 输入格式
- 输出格式
- 执行规则
- 成功标准
- 风险边界

---

### 3.2 Workflow 定义

Workflow 是将多个 Skills 按照固定顺序串联形成的处理流程。

它适合：

- 步骤相对稳定
- 输出标准相对明确
- 可以通过模板和结构化字段传递上下文的任务

例如：

- 活动需求 → 文案 → 审稿
- 活动需求 → 视觉方向 → 图片提示词
- 汇报资料 → PPT 目录 → 页面内容
- 活动信息 → 视频选题 → 口播稿 → 分镜

---

### 3.3 Agent 定义

Agent 是“任务调度者”，用于：

- 理解用户任务
- 判断调用哪条 Workflow
- 决定是否需要多条 Workflow 并行
- 在关键节点触发人工确认
- 管理工具调用边界

Agent 不应一开始就覆盖所有环节。第一阶段更建议：

**先做 4 条稳定 Workflow，再做 1 个总控 Agent。**

---

## 4. 总体实施顺序

推荐采用以下落地路径：

### 第一步：选定高频业务场景

优先选择：

- 高频
- 可标准化
- 人工重复度高
- 输出结果易评估
- 风险较低

推荐首批场景：

- 活动文案生成
- 海报图视觉方向生成
- 汇报 PPT 生成
- 视频脚本生成

---

### 第二步：先做结构化 Brief 提取

不要直接从用户原始文本进入主生成环节。

正确顺序是：

**原始需求 → Brief 抽取 Skill → 结构化字段 → 主生成 Skill**

这样做的好处：

- 输出更稳定
- 可减少信息遗漏
- 便于后续复用
- 更方便排查问题
- 更利于安全控制

---

### 第三步：搭建单条 Workflow

每条 Workflow 最少包含 3 个 Skill：

1. Brief 提取
2. 主结果生成
3. 审校/改写/优化

---

### 第四步：加入人工确认点

所有 Workflow 都必须保留人工确认点，尤其涉及：

- 对外发布
- 面向客户
- 带价格/日期/政策信息
- 品牌口径
- 预算或决策建议

原则：

**AI 先出 80 分初稿，人负责最后 20 分判断。**

---

### 第五步：跑测试与评估

每条 Workflow 建议至少连续测试 5 次，检查：

- 是否漏掉关键字段
- 是否丢失价格、日期、联系方式
- 是否风格不稳定
- 是否输出格式漂移
- 是否存在不当夸张表述

---

### 第六步：再加总控 Agent

当 4 条 Workflow 都稳定后，再加入 Agent 负责路由。

---

## 5. 系统架构建议

推荐第一版架构如下：

- 4 条内容生产 Workflow
- 每条 Workflow 3 个核心 Skills
- 1 个总控 Agent

### 5.1 四条 Workflow

1. 文案 Workflow
2. 图片 Workflow
3. 视频 Workflow
4. PPT Workflow

### 5.2 十二个 Skills

#### 文案 Workflow
- `brief_extractor`
- `copy_generator`
- `copy_reviewer`

#### 图片 Workflow
- `visual_brief_extractor`
- `image_prompt_generator`
- `brand_checker`

#### 视频 Workflow
- `video_angle_generator`
- `script_writer`
- `storyboard_reviewer`

#### PPT Workflow
- `ppt_brief_extractor`
- `deck_outliner`
- `slide_writer`

---

## 6. 统一演示案例

为了培训时更容易讲清楚，建议 4 个演示都使用同一个商业案例：

## 案例：某中小教培机构“暑期体验课招生活动”

基础信息：

- 机构类型：少儿英语机构
- 活动主题：暑期体验课
- 时间：7 月 6 日至 7 月 20 日
- 报名截止：7 月 5 日
- 价格：9.9 元
- 人群：5-10 岁孩子家长
- 卖点：表达能力、自信开口、小班教学
- 联系方式：138xxxx8888
- 风格：亲切、可信、不过度夸张

这样做的好处：

- 所有 Demo 可以串成完整业务链
- 便于讲解“同一需求如何拆成 4 条 AI Workflow”
- 降低备课复杂度
- 演示逻辑更连贯

---

## 7. 四个演示脚本方案

# 7.1 Demo 1：文案 Workflow

## 演示目标

将活动需求转成：

- 海报标题
- 朋友圈文案
- 社群通知
- 短信文案

## 流程设计

### Skill 1：`brief_extractor`

作用：把原始需求转成结构化活动 brief。

建议输出字段：

- campaign_name
- date_range
- deadline
- audience
- core_selling_points
- tone
- must_include
- forbidden
- channels

### Skill 2：`copy_generator`

作用：基于 brief 生成多渠道文案。

输出内容：

- 海报标题 3 个版本
- 朋友圈文案 2 个版本
- 社群通知 1 个版本
- 短信文案 1 个版本

### Skill 3：`copy_reviewer`

作用：审校并改写文案。

审查维度：

- 信息是否缺失
- 风格是否统一
- 是否夸张
- 是否适合目标受众
- 是否保留关键信息

## 培训讲解重点

- 第一轮不追求完美，先出可用初稿
- 第二轮用审校 Skill 做质量提升
- 文案不是一次性问答，而是一条可复用流程

---

# 7.2 Demo 2：图片 Workflow

## 演示目标

将活动信息转成：

- 3 个视觉方向
- 1 组高质量图片提示词
- 1 套海报标题建议

## 流程设计

### Skill 1：`visual_brief_extractor`

输出视觉 brief：

- subject
- audience
- scene
- style_keywords
- brand_tone
- primary_colors
- must_show_elements
- text_overlay
- negative_constraints

### Skill 2：`image_prompt_generator`

输出：

- 方向名
- 视觉描述
- 图片模型 prompt
- negative prompt
- 海报主标题

### Skill 3：`brand_checker`

检查：

- 是否符合品牌调性
- 是否适合家长人群
- 是否过度卡通或廉价
- 标题是否过长
- 是否建议微调

## 培训讲解重点

- 图片工作流的核心不是“会画图”
- 而是“把视觉需求说清楚”
- 第一版重点展示视觉方向与提示词，不把成功押在现场出图上

---

# 7.3 Demo 3：视频 Workflow

## 演示目标

将活动需求转成：

- 3 个短视频选题方向
- 1 条口播脚本
- 1 份分镜表
- 1 条发布文案

## 流程设计

### Skill 1：`video_angle_generator`

输出：

- 标题
- 开头钩子
- 核心卖点
- 情绪风格

### Skill 2：`script_writer`

生成 45-60 秒口播稿，包含：

- 前 3 秒钩子
- 问题共鸣
- 课程亮点
- 报名信息
- CTA

### Skill 3：`storyboard_reviewer`

输出：

- 6 镜头分镜表
- 封面标题 3 个
- 发布文案 1 条
- 评论区引导语 1 条

## 培训讲解重点

- 第一版先做“选题 → 脚本 → 分镜 → 发布文案”
- 不要一上来追求自动生成完整视频
- 企业更需要稳定的内容策划链路

---

# 7.4 Demo 4：PPT Workflow

## 演示目标

将活动资料转成：

- 8 页 PPT 目录
- 每页标题与要点
- 演讲备注
- 图表建议

## 流程设计

### Skill 1：`ppt_brief_extractor`

输出 PPT brief：

- presentation_goal
- audience
- core_message
- success_metrics
- budget
- channels
- timeline
- must_include

### Skill 2：`deck_outliner`

输出 8 页 PPT 目录，每页包括：

- 页码
- 页面标题
- 页面目标
- 3-5 个要点
- 图表或视觉建议

### Skill 3：`slide_writer`

展开指定页面，输出：

- 页面标题
- 页面正文短句
- 可直接放入 PPT 的内容
- 演讲备注

## 培训讲解重点

- PPT 工作流先解决逻辑，不先纠结排版
- AI 最有价值的是帮你摆脱空白页
- 结构清晰比页面华丽更重要

---

## 8. 总控 Agent 设计建议

当 4 条 Workflow 稳定后，再增加一个总控 Agent。

## Agent 目标

根据用户需求判断调用哪条 Workflow。

## 可路由的 Workflow

- copy_workflow
- image_workflow
- video_workflow
- ppt_workflow

## 路由原则

- 写通知、文案、活动文案 → 文案 Workflow
- 海报、主视觉、封面图 → 图片 Workflow
- 口播、分镜、短视频 → 视频 Workflow
- 汇报、方案、培训课件 → PPT Workflow

## 标准输出

建议输出：

- selected_workflows
- reason
- required_inputs

## 最佳实践

- 总控 Agent 只做路由，不直接承担所有生成任务
- 路由结果必须可解释
- 遇到高风险需求应提示人工确认

---

## 9. 技术与提示设计最佳实践

### 9.1 每条 Workflow 都先做 Brief 抽取

不要让杂乱输入直接驱动主生成。

### 9.2 节点间尽量使用结构化输出

比如使用：

- JSON
- 固定字段
- 枚举值
- 明确的缺失值表示

### 9.3 主生成后必须接审校节点

不要只做“生成”，还要做“检查与改写”。

### 9.4 每个 Skill 的职责要单一

一个 Skill 只做一件事。

### 9.5 Skill 的命名要清晰

例如：

- `copy_generator`
- `ppt_brief_extractor`
- `storyboard_reviewer`

不要使用模糊命名。

### 9.6 所有发布型内容必须人工过目

包括：

- 文案
- 海报标题
- 视频脚本
- PPT 对外汇报内容

---

## 10. 风险控制与治理

### 10.1 必须人工确认的场景

- 对外发布
- 报价、价格、时间
- 政策与制度解释
- 合同与法律内容
- 品牌关键表达
- 预算与经营判断

### 10.2 安全边界

不能只靠 Prompt 控制安全。

应该同时具备：

- 权限控制
- 审批机制
- 工具白名单
- 外发前确认
- 数据分级

### 10.3 不建议第一阶段做的事

- 一开始做万能 Agent
- 让 Agent 直接自动外发内容
- 不留人工确认点
- 不做评估就扩展场景
- 把多个能力混在一个 Skill 里

---

## 11. 培训中的标准讲法

你在企业培训中可以这样表达：

### 讲法一：面向老板

“企业不是在买一个会聊天的 AI，而是在搭建一套能稳定复用的 AI 工作流。”

### 讲法二：面向员工

“我们不是让大家随便问一句 AI，而是教大家把高频工作变成固定流程。”

### 讲法三：面向管理层

“先把高频、低风险、重复性强的任务做成 Workflow，再在必要时用 Agent 做调度。”

---

## 12. 适合你的产品化包装

### 产品一：中小企业 AI 工作流入门培训

适合对象：

- 老板
- 管理层
- 部门负责人

核心内容：

- Agent / Workflow / Skills 的企业化理解
- 哪些场景适合先上 Workflow
- 哪些场景才需要 Agent
- AI 应用风险与治理
- 小型内容生产工作流示范

### 产品二：行政办公与内容生产 AI 实操培训

适合对象：

- 行政
- 文员
- 助理
- 教务
- 人事
- 运营人员

核心内容：

- 文案 Workflow
- 图片 Workflow
- 视频 Workflow
- PPT Workflow
- 结构化提问与审校
- 常见错误与风险提醒

---

## 13. 一周搭建计划

### 第 1 天
确定统一案例与 4 条 Workflow。

### 第 2 天
完成 4 个 Brief Extractor。

### 第 3 天
完成 4 个主生成 Skills。

### 第 4 天
完成 4 个 Reviewer / Checker Skills。

### 第 5 天
每条 Workflow 连跑 5 次，检查稳定性。

### 第 6 天
做录屏与试讲，单条控制在 5-7 分钟。

### 第 7 天
将 4 个 Demo 串成完整 30 分钟演示。

---

## 14. 最终结论

这套最佳实践方案的关键不在于“做出一个最聪明的 Agent”，而在于：

- 把任务拆小
- 把能力做稳
- 把流程跑顺
- 把风险管住
- 把结果做成可复用的企业工作方式

最终建议可以总结为：

**先 Skill，后 Workflow，再 Agent；先结构化，后生成；先人工兜底，再逐步自动化。**

这就是最适合中小企业、也最适合你当前培训与演示阶段的最佳实践路径。
