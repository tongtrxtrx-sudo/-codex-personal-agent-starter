# 图片执行层设计

## 目标
在图片方向已经确认后，把“实际出图”和“结果复审”从当前方向探索 workflow 中拆出来，形成一层轻量但可复用的执行链路。

说明：
如果当前只有 ChatGPT Pro、没有 API key，优先走 [image-chatgpt-pro-manual-flow.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-chatgpt-pro-manual-flow.md)。本文件描述的是后续扩展到 API 执行层时的结构。

## 为什么要单独拆执行层
当前图片 workflow 更适合做方向探索：
- 先整理视觉 brief
- 再输出 2 到 3 个方向和 prompt
- 再做品牌审校
- 最后人工确认

这条链路的优势是稳，不会把“出图成败”直接压在第一轮 prompt 上。  
但如果团队真的要落到执行，就还缺两件事：
- 一个真正负责调用 OpenAI 图片能力的执行器
- 一个真正对生成结果做复审的结果审校器

## 推荐分层

### 第一层：方向探索层
沿用现有 [image-workflow.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-workflow.md)。

输出：
- `visual brief`
- `prompt directions`
- `brand review`
- `human-check items`

### 第二层：执行层
由 [image-executor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-executor/SKILL.md) 负责。

职责：
- 接收已经人工选定的方向
- 选择合适的 OpenAI 图片生成接口
- 保存生成参数、`revised_prompt` 和输出物

### 第三层：结果复审层
由 [image-result-reviewer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-result-reviewer/SKILL.md) 负责。

职责：
- 对照最初 brief 和已选方向检查生成结果
- 判断是“接受”“小修再生”“换方向重跑”

## OpenAI 接口选择建议

### 一次性生成 / 一次性编辑
优先用 OpenAI 的 Image API。

适合：
- 一次出 1 到 4 张候选图
- 已经明确 prompt
- 不需要对话式多轮上下文

### 多轮对话式修改
优先用 Responses API + `image_generation` 工具。

适合：
- 需要连续修改同一张图
- 需要保留上下文和前一轮输出
- 需要在更大的 agent / workflow 里把图片步骤嵌进去

## 模型建议
- 默认模型：`gpt-image-1.5`
- 快速试方向：`gpt-image-1-mini`
- 需要多轮对话式图片修改时，结合 Responses API 的图片生成工具

## 最低落地记录
每次执行至少保存：
- 选定方向
- prompt
- negative prompt
- model
- size
- quality
- format
- background
- 输入参考图或 mask
- 输出结果路径或 artifact
- `revised_prompt`

## 人工边界
- 首轮生成结果默认不视为最终成稿
- 涉及品牌正式传播的图，必须人工过目
- 如果结果偏廉价、偏卡通、过挤或偏离 brief，不要直接“勉强使用”
