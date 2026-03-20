# 图片 Workflow

## 目标
先把视觉需求说清楚，再生成可评审的方向与 prompt，最后做品牌一致性检查，而不是直接把成败押在现场出图。

## 适用场景
- 活动海报主视觉
- 招生海报
- 社媒封面图
- 宣传图片方向探索

## 不适用场景
- 已有完整品牌规范且只需要执行设计
- 需要最终商业设计成稿而非方向探索
- 没有受众、场景和品牌调性的纯随机创意尝试

## 核心 Skills
1. [visual-brief-extractor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/visual-brief-extractor/SKILL.md)
2. [image-prompt-generator](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-prompt-generator/SKILL.md)
3. [brand-checker](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brand-checker/SKILL.md)

## 标准流程
### Step 1：视觉 Brief 抽取
- 输入：活动信息、受众、品牌调性、风格要求
- 输出：结构化视觉 brief
- 必须明确：主体、受众、场景、风格关键词、主色建议、必须出现元素、负向限制
- 生成前应先对照图片 Brief 必保留字段表

### Step 2：视觉方向与 Prompt 生成
- 输入：结构化视觉 brief
- 输出：2 到 3 个视觉方向
- 生成时应对照图片方向质量规则
- 每个方向应包含：
  - 方向名
  - 视觉描述
  - prompt
  - negative prompt
  - 主标题建议

### Step 3：品牌一致性检查
- 检查是否符合受众预期
- 检查是否存在廉价感、过度卡通、画面过挤等问题
- 检查主标题是否过长或过促销
- 检查必保留事实和负向限制是否仍被保留

### Step 4：人工确认
- 选定最终视觉方向前必须人工确认
- 涉及品牌关键表达、促销信息或对外正式传播时必须人工过目

## 最低交付物
- 一份结构化视觉 brief
- 2 到 3 个视觉方向
- 每个方向对应的 prompt 与 negative prompt
- 一份品牌检查建议

## 模板资产
- [visual-brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/visual-brief-extractor/assets/visual-brief-template.json)
- [image-direction-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-prompt-generator/assets/image-direction-template.md)
- [brand-review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brand-checker/assets/brand-review-checklist.md)
- [image-brief-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-brief-required-fields.md)
- [image-direction-quality-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-direction-quality-rules.md)
- [image-workflow-template-pack.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-workflow-template-pack.md)

## 人工确认清单
- [ ] 方向符合品牌调性
- [ ] 方向符合目标受众审美
- [ ] 没有廉价促销感
- [ ] 标题长度可用
- [ ] 对外传播风险可控

## 测试清单
- 连续运行 5 次，检查方向是否过于同质化
- 检查 prompt 是否足够具体
- 检查 negative prompt 是否能压住常见坏图风险
- 检查是否反复出现不适合品牌的方向
- 检查建议是否足够具体、可执行

## 完成标准
- 团队能在出图前选定明确方向
- prompt 可复用，不是一次性句子
- 品牌检查能提供可执行修改建议
