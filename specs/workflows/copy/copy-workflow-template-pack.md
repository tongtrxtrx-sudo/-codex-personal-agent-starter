# 文案 Workflow 模板包

## 目标
给文案 Workflow 提供一套可以直接复用的最小模板资产，减少每次从零组织输入、输出和审校结果的成本。

## 模板组成
1. [brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brief-extractor/assets/brief-template.json)
2. [copy-output-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-generator/assets/copy-output-template.md)
3. [review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-reviewer/assets/review-checklist.md)
4. [copy-scene-intake-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-scene-intake-rules.md)
5. [copy-social-platform-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-social-platform-rules.md)
6. [copy-work-scene-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-work-scene-rules.md)
7. [copy-channel-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-required-fields.md)
8. [copy-channel-length-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-length-rules.md)
9. [copy-title-templates.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-title-templates.md)
10. [copy-version-selection-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-version-selection-rules.md)
11. [copy-review-output-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-review-output-template.md)

## 推荐使用顺序
### Step 1：整理原始需求
- 把用户原始描述、聊天记录、会议纪要或语音转写先收进 `brief-template.json`
- 先按场景补问规则判断要补哪些最小字段
- 缺失信息不要猜，放进 `missing_info`

### Step 2：生成多渠道文案
- 基于结构化 brief 输出文案
- 输出时优先贴合 `copy-output-template.md` 的结构
- 如果目标是社交媒体平台，优先按平台原生结构输出
- 输出前先看渠道必保留字段表
- 标题生成时先看标题模板
- 输出后再对照长度约束表做一次自检

### Step 3：做审校与修正
- 按 `review-checklist.md` 逐项核对
- 先核对事实，再核对语气，再核对发布风险
- 特别检查不同渠道是否漏掉了各自的必保留字段
- 特别检查标题和短信是否超出建议长度
- 明确推荐采用版本，避免把版本差异留给用户自己猜
- 按 `copy-review-output-template.md` 说明为什么推荐、为什么不推荐、下一步先改什么

### Step 4：人工确认
- 价格、日期、联系方式、品牌关键表达必须人工确认
- 审校通过不等于可直接外发

## 最低落地标准
- 能稳定从原始需求得到结构化 brief
- 能稳定产出海报标题、朋友圈文案、社群通知、短信文案
- 能稳定指出事实问题、语气问题和风险点

## 后续可继续补的资产
- 活动 brief 示例
- 行业化文案样例
- 常见错误示例库
