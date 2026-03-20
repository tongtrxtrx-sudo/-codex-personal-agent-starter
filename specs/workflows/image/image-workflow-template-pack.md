# 图片 Workflow 模板包

## 目标
给图片 workflow 提供一套可直接复用的最小模板资产，让团队能先把视觉方向说清楚、审清楚，再决定是否进入出图或设计执行。

## 模板组成
1. [visual-brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/visual-brief-extractor/assets/visual-brief-template.json)
2. [image-direction-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-prompt-generator/assets/image-direction-template.md)
3. [brand-review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brand-checker/assets/brand-review-checklist.md)
4. [image-brief-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-brief-required-fields.md)
5. [image-direction-quality-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-direction-quality-rules.md)

## 推荐使用顺序
### Step 1：整理视觉 Brief
- 先用 `visual-brief-template.json` 把主体、受众、场景、风格和负向限制整理出来
- 缺失信息不要猜，放进 `missing_info`

### Step 2：生成方向与 Prompt
- 用 `image-direction-template.md` 输出 3 个可比较方向
- 输出前先看必保留字段表
- 输出后再对照质量规则自检

### Step 3：做品牌审校
- 用 `brand-review-checklist.md` 逐项核对
- 先看受众和品牌，再看画面和标题

### Step 4：人工确认
- 选定方向前必须人工确认
- 促销信息、品牌关键表达和最终出图都不能跳过人工把关

## 最低落地标准
- 能稳定从原始需求整理出结构化视觉 brief
- 能稳定给出 3 个明显不同的方向
- 能稳定指出不适合品牌或受众的问题

## 后续可继续补的资产
- 行业化视觉示例
- 常见负向提示词库
- 版式占位建议
