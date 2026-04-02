# 图片 Workflow 最佳解决方案

## 目标
基于当前仓库已有的图片 workflow 资产，结合 OpenAI 官方图片能力和 GitHub 官方仓库的公开实现模式，形成一套更完整、但仍然轻量的图片解决方案。

## 当前状态判断
当前图片 workflow 已经具备一条完整的方向探索链路：
1. 视觉 brief 抽取
2. 视觉方向与 prompt 生成
3. 品牌一致性检查
4. 人工确认

这说明图片 workflow 已经不是零散想法，而是一条可测试、可演示、可复用的结构化流程。  
但它当前更偏“方向探索层”，还没有把“实际出图”和“结果复审”正式纳入体系。

## 外部最佳实践结论

### 来自 OpenAI 官方文档的关键信息
1. OpenAI 当前支持两类主用图片生成路径：
   - Image API：适合一次性生成或编辑
   - Responses API + `image_generation` 工具：适合对话式、多轮修改
2. 图片生成支持的关键输出参数包括：
   - `size`
   - `quality`
   - `format`
   - `compression`
   - `background`
   - `action`
3. 图片生成工具会返回 `revised_prompt`，这对复盘和复现很重要。
4. 图片 prompt 的稳定写法，应该明确：
   - scene
   - subject
   - key details
   - overlay facts
   - constraints

### 来自 GitHub 官方仓库的关键信息
1. [openai/openai-cookbook](https://github.com/openai/openai-cookbook) 提供了图片生成、图片编辑、多轮修改等例子，适合作为实现样板。
2. [openai/openai-python](https://github.com/openai/openai-python) 是当前最直接的 Python SDK 主线，适合仓库后续做脚本执行层。
3. [openai/openai-agents-python](https://github.com/openai/openai-agents-python) 说明多 agent 编排、tracing、human-in-the-loop 已有官方实现方向，但当前仓库不需要立刻引入整套 agent 化结构。

## 推荐目标架构

### A. 保留现有方向探索层
继续沿用 [image-workflow.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-workflow.md)。

职责：
- 把视觉需求说清楚
- 产出 2 到 3 个可评审方向
- 过滤掉明显不适合品牌的方向

### B. 新增执行层
用 [image-executor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-executor/SKILL.md) 承接人工确认后的方向。

职责：
- 选择 Image API 或 Responses API
- 记录生成配置
- 保存输出物和 `revised_prompt`

### C. 新增结果复审层
用 [image-result-reviewer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-result-reviewer/SKILL.md) 检查真实生成结果。

职责：
- 检查是否符合最初 brief
- 检查是否偏廉价、偏卡通、过挤
- 决定接受、小修还是重跑

### D. 新增最小补问层
用 [image-minimal-intake.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-minimal-intake.md) 统一处理视觉输入不足的问题。

职责：
- 在 brief 不足时先补最少必要信息
- 避免直接用空泛风格词写 prompt

## 为什么这是最适合当前仓库的方案
1. 不推翻现有 workflow，延续现有 4 步统一结构
2. 不提前把系统做成重型多 agent 平台
3. 能和 OpenAI 官方图片能力自然衔接
4. 把“方向探索”和“实际出图”清楚分层，维护成本更低

## 当前默认落地路径
如果当前只有 ChatGPT Pro，而没有 API key，默认优先走：

1. [image-workflow.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-workflow.md) 产出方向
2. [image-chatgpt-pro-manual-flow.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-chatgpt-pro-manual-flow.md) 整理 ChatGPT 可直接使用的成图输入
3. 在 ChatGPT 中手动出图
4. 再把选中结果带回仓库做记录或复审

API 执行层是后续可扩展项，不是当前默认前提。

## 推荐默认执行策略

### 方向探索阶段
- 输出 `visual brief`
- 输出 3 个方向
- 每个方向含 prompt、negative prompt、主标题建议、风险提醒
- 强制人工选择方向

### 执行阶段
- 一次性生成或编辑：优先 Image API
- 对话式多轮修改：优先 Responses API + `image_generation`
- 默认模型：`gpt-image-1.5`
- 快速试方向：`gpt-image-1-mini`

### 结果复审阶段
- 对照 brief 和方向做复审
- 输出明确结论：
  - 接受
  - 小修再生
  - 换方向重跑

## 建议新增的仓库资产
- `.agents/skills/image-executor/`
- `.agents/skills/image-result-reviewer/`
- `specs/workflows/image/image-minimal-intake.md`
- `specs/workflows/image/image-execution.md`

## 建议下一步
1. 先按 ChatGPT Pro 路径把方向探索链路跑顺
2. 先补第二个、第三个真实案例
3. 再决定是否需要脚本化执行层
4. 最后才评估是否要引入多 agent 编排

补充：
- 如果需要把外部 prompt 库的洞察转成仓库内的演进路线，先看 [image-subscene-planning.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-subscene-planning.md)

## 参考来源
- [OpenAI Image generation guide](https://platform.openai.com/docs/guides/images/image-generation)
- [OpenAI Image generation tool guide](https://platform.openai.com/docs/guides/tools-image-generation)
- [OpenAI GPT Image cookbook example](https://developers.openai.com/cookbook/examples/generate_images_with_gpt_image)
- [openai/openai-cookbook](https://github.com/openai/openai-cookbook)
- [openai/openai-python](https://github.com/openai/openai-python)
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
