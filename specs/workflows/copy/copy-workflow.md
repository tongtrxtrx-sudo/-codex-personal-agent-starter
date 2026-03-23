# 文案 Workflow

## 目标
把杂乱活动需求稳定地转成可用文案初稿，并在对外发布前完成必要审校与人工确认。

先理解整体分类方式时，可先看 [文案 workflow 分类模型.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/文案 workflow 分类模型.md)。

## 展示模式
### 默认模式
- 只展示最终推荐版本
- 只展示必要备选版本
- 只展示待确认项

### 展开模式
- 当用户显式要求“展开链路”“显示完整流程”“调试模式”时，再展示：
  - 结构化 brief
  - 文案初稿
  - 审校结果
  - 待确认项

说明：
- 无论展示模式如何，workflow 内部都应完整执行 brief -> draft -> review -> human-check。
- 默认模式面向日常使用，展开模式面向测试、排错和流程优化。

## 适用场景
- 活动海报标题
- 朋友圈文案
- 社群通知
- 短信文案
- 多渠道通知类内容
- 小红书内容帖
- 微博文案
- 抖音配文
- 知乎回答类文案
- B站标题与简介
- 常见办公与业务场景文案

## 不适用场景
- 合同、法律、制度类正式文本
- 没有明确事实输入却要求直接生成最终稿
- 不允许人工确认的自动外发链路

## 核心 Skills
1. [brief-extractor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brief-extractor/SKILL.md)
2. [copy-generator](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-generator/SKILL.md)
3. [copy-reviewer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-reviewer/SKILL.md)

## 标准流程
### Step 1：Brief 抽取
- 输入：原始活动需求、聊天记录、语音转写、零散要点
- 输出：结构化 brief
- 必须保留：日期、价格、报名截止、联系方式、目标人群、核心卖点、风格要求
- 如果是平台内容，先按场景补问规则补齐最小字段

### Step 2：主结果生成
- 输入：结构化 brief
- 输出：按渠道拆分的文案初稿
- 生成前应先对照渠道必保留字段表
- 生成时应对照标题模板与版本选择规则
- 如果是社交媒体平台内容，应优先按平台原生结构输出
- 建议输出：
  - 海报标题 3 个版本
  - 朋友圈文案 2 个版本
  - 社群通知 1 个版本
  - 短信文案 1 个版本

### Step 3：审校与优化
- 检查是否漏掉关键事实
- 检查风格是否统一
- 检查不同渠道是否匹配长度与语气
- 检查是否存在夸张、模糊承诺或不适合对外发布的表达
- 检查不同渠道是否满足各自的必保留字段
- 检查标题、短信、通知类内容是否符合长度约束
- 检查不同版本职责是否清楚，并明确推荐采用版本
- 审校输出应遵循 [copy-review-output-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-review-output-template.md)

### Step 4：人工确认
- 对外发布前必须人工确认
- 如果涉及价格、日期、联系方式、品牌关键表达，必须逐项核对

## 最低交付物
- 一份结构化 brief
- 一组多渠道文案草稿
- 一份审校结果
- 一份人工确认后的最终稿或修改意见

## 默认对用户展示
- 最终推荐版本
- 必要备选版本
- 待确认项

## 输入不足时的处理
- 先按 [copy-scene-intake-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-scene-intake-rules.md) 识别场景
- 再只补问该场景最小必要字段
- 不要沿用活动推广模板去机械追问所有场景

## 模板资产
- [文案 workflow 分类模型.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/文案 workflow 分类模型.md)
- [brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brief-extractor/assets/brief-template.json)
- [copy-output-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-generator/assets/copy-output-template.md)
- [review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-reviewer/assets/review-checklist.md)
- [copy-runner-interface.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-runner-interface.md)
- [copy-scene-intake-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-scene-intake-rules.md)
- [copy-social-platform-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-social-platform-rules.md)
- [copy-work-scene-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-work-scene-rules.md)
- [copy-kindergarten-group-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-kindergarten-group-rules.md)
- [copy-channel-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-required-fields.md)
- [copy-channel-length-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-length-rules.md)
- [copy-title-templates.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-title-templates.md)
- [copy-version-selection-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-version-selection-rules.md)
- [copy-review-output-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-review-output-template.md)
- [copy-workflow-template-pack.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-workflow-template-pack.md)

## 人工确认清单
- [ ] 价格无误
- [ ] 日期和截止时间无误
- [ ] 联系方式无误
- [ ] 核心卖点没有夸大
- [ ] 品牌口径可对外使用

## 测试清单
- 连续运行 5 次，检查是否存在字段遗漏
- 检查不同版本是否丢失必须包含信息
- 检查标题是否过长
- 检查短信是否超长
- 检查是否出现风格漂移或营销过度

## 完成标准
- 生成结果可直接进入人工定稿
- 多渠道输出结构稳定
- 关键事实不丢失
- 审校结果能指出具体问题，而不是泛泛评价
