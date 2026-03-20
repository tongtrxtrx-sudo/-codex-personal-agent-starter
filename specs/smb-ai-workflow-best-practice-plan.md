# Specification: 中小企业 AI Workflow 最佳实践执行计划

## Metadata
- Version: 0.1.0
- Status: Draft
- Author: Codex
- Created: 2026-03-17
- Last Updated: 2026-03-17

## Problem
当前仓库里已经沉淀了多份关于 `Skill -> Workflow -> Agent` 的方法论、4 个 Demo 设计和培训包装材料，但这些内容仍以总结稿、讲稿和资料包为主，缺少一份可以直接执行的统一计划。  
本计划的目标，是把现有总结收束成一条适合中小企业场景的落地路径，避免一开始追求万能 Agent，而是先把高频、重复、可标准化、可培训的 AI Workflow 做稳。

## Context
- 现有资料来源：
  - `_sorted/docs/企业AI_Agent_Workflow_Skills_最佳实践方案.md`
  - `_sorted/docs/中小企业AI_Workflow_培训师完整版资料包_新版.md`
  - `_sorted/docs/4个Demo_详细实践版.md`
  - `_sorted/docs/4个Demo_逐字稿版.md`
  - `_sorted/docs/4个Demo_PPT页对应讲稿版.md`
- 当前定位判断来自 `inbox/capture.md`：
  - 先 Skill，再 Workflow，最后 Agent
  - 先做高频、重复、可标准化的工作流
  - 一条好用的 AI 工作流要经过需求整理、结果生成、审校优化、人工确认
  - 最适合切入的方向是中小企业 AI 工作流入门培训，以及行政办公与内容生产实操培训

## Scope
- In scope:
  - 明确对外定位与产品线
  - 固化首批 4 条 Workflow 与 12 个核心 Skills
  - 统一 Workflow 结构与人工确认机制
  - 建立测试、评估、试讲与交付标准
  - 形成 7 天可执行推进节奏
- Out of scope:
  - 一开始就做万能 Agent
  - 自动对外发布内容
  - 外部 API 集成、后台服务、复杂平台化建设
  - 同时扩展过多行业版和岗位版课程

## Requirements
### Functional
- FR-1: 必须将整体定位收束为“中小企业 AI 工作流培训与落地顾问”，而不是泛泛的 AI 工具培训。
- FR-2: 第一阶段必须只保留两类产品：
  - `中小企业 AI 工作流入门培训`
  - `行政办公与内容生产 AI 实操培训`
- FR-3: 第一阶段必须只覆盖 4 条 Workflow：
  - 文案 Workflow
  - 图片 Workflow
  - 视频 Workflow
  - PPT Workflow
- FR-4: 每条 Workflow 必须遵循统一结构：
  1. Brief 抽取
  2. 主结果生成
  3. 审校与优化
  4. 人工确认
- FR-5: 每条 Workflow 必须至少由 3 个职责单一的 Skills 组成，且每个 Skill 都要写清：
  - 名称
  - 适用场景
  - 不适用场景
  - 输入格式
  - 输出格式
  - 执行规则
  - 成功标准
  - 风险边界
- FR-6: 第一阶段必须固定首批 12 个 Skills：
  - 文案：`brief_extractor`、`copy_generator`、`copy_reviewer`
  - 图片：`visual_brief_extractor`、`image_prompt_generator`、`brand_checker`
  - 视频：`video_angle_generator`、`script_writer`、`storyboard_reviewer`
  - PPT：`ppt_brief_extractor`、`deck_outliner`、`slide_writer`
- FR-7: 所有涉及价格、日期、联系方式、品牌口径、预算建议、对外发布的内容，必须设置人工确认点，不允许直接视为最终稿。
- FR-8: 每条 Workflow 必须建立至少 5 次连续测试的评估机制，检查字段遗漏、格式漂移、风格波动、夸张表达和返工点。
- FR-9: 只有在 4 条 Workflow 都达到稳定可讲、可演示、可复用后，才允许加入总控 Agent 做路由演示。
- FR-10: 培训交付必须标准化为一套资料包，而不是只交一场讲课。

### Non-functional
- NFR-1: 方案必须保持轻量，不依赖复杂平台或额外基础设施。
- NFR-2: 方案必须强调可复用、可培训、可落地，而不是一次性演示效果。
- NFR-3: 所有关键步骤都必须保留清晰的安全边界和人工兜底。
- NFR-4: 产出结构必须足够稳定，便于后续复制到更多客户、岗位和行业场景。

## Execution Plan
### Phase 1: 定位与边界冻结
目标：停止继续发散，把对外表达与首批场景收束到最小可用集合。

执行项：
1. 固定一句对外定位：帮助中小企业把真实工作拆成可复用、可培训、可落地的 AI Workflow。
2. 固定两类产品线，不再同时扩更多服务形态。
3. 固定首批 4 条 Workflow，不在第一阶段新增第 5 条。
4. 固定共同原则：先 Skill，再 Workflow，最后 Agent。

### Phase 2: Workflow 与 Skill 标准化
目标：把方法论变成可演示、可训练、可复制的结构化资产。

执行项：
1. 为 4 条 Workflow 分别补齐 3 个核心 Skills 的统一模板。
2. 把所有 Workflow 都改造成统一的 4 步链路。
3. 为每条 Workflow 补齐人工确认点和高风险提醒。
4. 统一命名风格、输入字段和输出结构，降低后续培训和复用成本。

### Phase 3: 稳定性测试与讲法打磨
目标：验证这不是“看上去能讲”，而是真的能稳定演示和复用。

执行项：
1. 每条 Workflow 连跑 5 次，并记录问题清单。
2. 对出现频率最高的问题补充到 Reviewer 或 Checker 规则里。
3. 把每个 Demo 控制在 5-7 分钟。
4. 用统一案例串起 4 个 Demo，形成 30 分钟完整演示。

### Phase 4: 交付包与试讲验证
目标：把方法论和 Demo 转化为客户可感知的标准产品。

执行项：
1. 输出标准培训 PPT。
2. 输出讲师逐字稿。
3. 输出 4 个 Demo 示例。
4. 输出常用 Prompt 模板。
5. 输出企业 AI Workflow 落地建议。
6. 输出课后练习题与模板包。
7. 先做小范围试讲，再决定是否扩行业版或引入 Agent 路由演示。

## Milestones
### 7 天推进节奏
1. Day 1：冻结统一案例、产品定位、4 条 Workflow 边界。
2. Day 2：完成 4 个 Brief Extractor 的输入输出模板。
3. Day 3：完成 4 个主生成 Skills 的输出结构。
4. Day 4：完成 4 个 Reviewer / Checker Skills，并明确人工确认点。
5. Day 5：每条 Workflow 连跑 5 次，整理问题与修正项。
6. Day 6：完成一轮录屏与试讲，把单条 Demo 控制在 5-7 分钟。
7. Day 7：串成完整 30 分钟演示，打包形成标准交付资料。

## Deliverables
- D-1: 一页清晰的对外定位文案
- D-2: 两类产品的课程简介
- D-3: 4 条 Workflow 的结构说明
- D-4: 12 个 Skills 的标准定义
- D-5: 4 个 Demo 的演示脚本与逐字稿
- D-6: 标准培训 PPT
- D-7: Prompt 模板与课后练习
- D-8: 企业 AI Workflow 落地建议

## Acceptance Criteria
- 明确写出且内部一致的定位表述，不再混用“万能 Agent”“复杂平台”等高扩张话术。
- 两类产品线的对象、目标和内容边界清晰，不互相混淆。
- 4 条 Workflow 全部具备统一 4 步结构和人工确认点。
- 12 个 Skills 都有标准化定义，不再只有名称而没有边界。
- 每条 Workflow 都完成至少 5 次连续测试，并形成问题清单。
- 4 个 Demo 能串成一套 30 分钟左右的完整演示。
- 交付件至少包含 PPT、逐字稿、Demo、模板和落地建议。
- 在没有新增外部平台能力的前提下，也能完成首轮培训交付。

## Verification
- 人工检查本计划是否完整覆盖“先 Skill，再 Workflow，最后 Agent”的主线。
- 人工检查本计划是否完整覆盖文案、图片、视频、PPT 4 条 Workflow。
- 人工检查本计划是否包含测试、审校、人工确认和风险边界。
- 后续执行时，逐项对照 `Deliverables` 和 `Acceptance Criteria` 进行复核。

## Risks and Assumptions
- Risk: 过早扩展到更多行业和岗位版本，会稀释首轮交付质量。
- Risk: 过早强调 Agent，容易偏离中小企业真实落地需求。
- Risk: 如果跳过审校和人工确认，培训内容会显得“会生成，但不可靠”。
- Risk: 如果 Skill 定义不清，后续 Workflow 会失去稳定性和可培训性。
- Assumption: 首轮目标客户仍以中小企业老板、管理层和行政办公类岗位为主。
- Assumption: 第一阶段更看重可讲、可演示、可复制，而不是自动化程度。

## Change Log
| Date | Version | Description | Author |
| ---- | ------- | ----------- | ------ |
| 2026-03-17 | 0.1.0 | Initial draft | Codex |
