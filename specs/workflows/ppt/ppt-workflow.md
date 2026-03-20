# PPT Workflow

## 目标
先解决汇报逻辑和页面结构，再写页面内容与演讲备注，减少从零开始做 PPT 的负担。

## 适用场景
- 项目汇报
- 活动方案汇报
- 培训课件初稿
- 管理层汇报结构整理

## 不适用场景
- 只需要做视觉美化排版
- 缺少核心数字和目标却要求直接出最终汇报
- 高风险对外材料且不允许人工审定

## 核心 Skills
1. [ppt-brief-extractor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/ppt-brief-extractor/SKILL.md)
2. [deck-outliner](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/deck-outliner/SKILL.md)
3. [slide-writer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/slide-writer/SKILL.md)

## 标准流程
### Step 1：汇报 Brief 抽取
- 输入：项目资料、汇报对象、汇报目标、预算、时间线、关键指标
- 输出：结构化 PPT brief
- 必须明确：汇报对象、核心信息、成功指标、预算、渠道、时间线、必须包含内容

### Step 2：目录结构生成
- 输入：结构化 PPT brief
- 输出：页级大纲
- 每页应包含：
  - 页码
  - 标题
  - 页面目标
  - 3 到 5 个要点
  - 图表或视觉建议

### Step 3：页面内容与备注生成
- 输入：页级大纲
- 输出：
  - 页面标题
  - 页面短句
  - 视觉建议
  - 演讲备注
- 原则：页面上短，备注里讲透

### Step 4：人工确认
- 汇报前必须人工确认所有数字、判断、预算和对外口径
- 面向老板、客户或管理层时，不允许跳过人工审定

## 最低交付物
- 一份结构化 PPT brief
- 一份页级大纲
- 一套页面初稿
- 一套演讲备注

## 人工确认清单
- [ ] 汇报对象与目标一致
- [ ] 关键数字无误
- [ ] 页间逻辑顺序合理
- [ ] 页面短句可直接上屏
- [ ] 备注足以支持口头汇报

## 测试清单
- 连续运行 5 次，检查目录是否稳定
- 检查是否存在页间重复
- 检查页面文本是否过长
- 检查备注是否空泛
- 检查是否出现未经确认的判断性结论

## 完成标准
- 团队能稳定拿到可讲的 PPT 初稿
- 页级逻辑清晰，不靠临场补救
- 数字和判断在人工确认后才进入最终汇报
