# Skill 与 Workflow 测试清单

## 目标
给当前仓库里的 skills 和 workflows 提供一套可重复使用的测试方法，避免只凭一次顺手输出就判断“已经可用”。

## 核心判断标准
测试 skill 或 workflow 时，不先问“写得顺不顺”，先问这 4 件事：

1. 能不能被正确触发
2. 输出是否稳定
3. 边界有没有守住
4. 结果能不能直接进入下一步

## 一、Skill 测试方法

### 每个 Skill 至少测 3 类输入

#### 1. 标准输入
目标：检查 skill 能否在信息较完整时按预期输出。

看点：
- 是否触发到正确 skill 职责
- 是否按模板或约定结构输出
- 是否保留关键事实

#### 2. 缺失输入
目标：检查 skill 是否会在缺信息时乱补。

看点：
- 是否明确标出缺失字段
- 是否使用 `null`、空值或待确认项
- 是否避免编造日期、价格、联系方式、指标

#### 3. 边界输入
目标：检查 skill 是否知道什么时候该停、该提醒、该交还给人。

看点：
- 是否标出高风险内容
- 是否要求人工确认
- 是否避免把高风险内容直接包装成最终稿

## 二、Skill 通用通过标准

每次测试都至少检查以下项目：

- [ ] 被正确触发，没有越权做别的事
- [ ] 输出结构符合模板或固定格式
- [ ] 关键事实没有丢
- [ ] 缺失信息没有乱补
- [ ] 结果可以直接交给下一个 skill
- [ ] 风险边界有体现
- [ ] 人工确认点没有消失

## 三、Workflow 测试方法

### Workflow 不要一句话“全自动跑完”
建议按链路拆成 4 步逐步测试：

1. 原始需求
2. Structured brief
3. 初稿输出
4. 审校结果
5. 人工确认

### 每条 Workflow 至少跑 5 次
不要只跑一次。  
建议最少覆盖 3 类案例：

- 教培招生
- 行政通知
- 内容推广

如果是 PPT 或视频 workflow，也要尽量换不同业务背景，而不是一直只用一个案例。

## 四、Workflow 通用通过标准

- [ ] Step 1 能稳定产出结构化输入
- [ ] Step 2 能稳定产出主结果
- [ ] Step 3 能稳定指出具体问题
- [ ] Step 4 仍保留人工确认
- [ ] 输出能从上一步自然进入下一步
- [ ] 连续多次运行时结构不漂移
- [ ] 关键事实不会在中间环节丢失

## 五、重点观察的失败信号

### 事实类失败
- 漏价格
- 漏日期
- 漏截止时间
- 漏联系方式
- 擅自补充不存在的事实

### 结构类失败
- 输出格式忽左忽右
- 字段名不稳定
- 不同轮次结果无法直接比较
- 不能直接交给下一个 skill

### 风格类失败
- 语气忽然变得很营销
- 不符合目标人群
- 夸大承诺
- 制造焦虑

### 边界类失败
- 明明高风险却没提醒人工确认
- 审校后直接被当作可发布
- 把不确定内容写成确定事实

## 六、最小测试流程

### 测单个 Skill
1. 准备标准输入
2. 准备缺失输入
3. 准备边界输入
4. 各跑 1 次
5. 用“Skill 通用通过标准”逐项打勾

### 测一条 Workflow
1. 选一个真实案例
2. 按 4 步链路逐步跑
3. 保存每一步产物
4. 用“Workflow 通用通过标准”打勾
5. 连续再换 2 到 4 个案例重复

## 七、建议保存的测试产物

每次 workflow 测试，至少保存以下 4 份结果：

- `raw-input`
- `structured-brief`
- `draft-output`
- `review-result`

如果是图片、视频、PPT workflow，也建议保留：

- `final-human-check`

## 八、5 次稳定性记录表

可直接复制下面这段做记录：

```md
# Workflow 稳定性记录

## Workflow 名称
- 名称：
- 日期：
- 测试人：

## Case 1
- 场景：
- 是否正确触发：
- 是否保留关键事实：
- 是否结构稳定：
- 是否有人工确认点：
- 主要问题：

## Case 2
- 场景：
- 是否正确触发：
- 是否保留关键事实：
- 是否结构稳定：
- 是否有人工确认点：
- 主要问题：

## Case 3
- 场景：
- 是否正确触发：
- 是否保留关键事实：
- 是否结构稳定：
- 是否有人工确认点：
- 主要问题：

## Case 4
- 场景：
- 是否正确触发：
- 是否保留关键事实：
- 是否结构稳定：
- 是否有人工确认点：
- 主要问题：

## Case 5
- 场景：
- 是否正确触发：
- 是否保留关键事实：
- 是否结构稳定：
- 是否有人工确认点：
- 主要问题：

## 汇总
- 最容易出错的环节：
- 最常见问题：
- 是否适合继续复用：
- 是否需要补模板或补审校规则：
```

如果你想直接看一份已填过的首轮记录，可以参考：

- [copy-workflow-stability-record-round-1.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-workflow-stability-record-round-1.md)

## 九、文案 Workflow 当前建议测法

对于当前仓库里已经落地的文案 workflow，建议这样开始：

1. 先用已有的暑期体验课案例再跑 1 次：
   [copy-summer-course-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-summer-course-demo)
2. 再换一个行政通知案例：
   [copy-admin-holiday-notice-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-admin-holiday-notice-demo)
3. 再换一个活动推广案例：
   [copy-weekend-promo-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weekend-promo-demo)
4. 每轮都保留：
   - `raw-input`
   - `structured-brief`
   - `copy-draft`
   - `review-result`

## 十、不要这样测

- [ ] 只测 1 次就判断可用
- [ ] 只看文字顺不顺，不看事实有没有丢
- [ ] 跳过缺失输入测试
- [ ] 跳过边界输入测试
- [ ] 让 workflow 一步出最终稿
- [ ] 把“审校通过”当成“可以直接外发”

## 十一、完成标准

你可以认为一个 skill 或 workflow 进入“可继续复用”状态，当且仅当：

- 连续多次运行结构稳定
- 关键事实不容易丢
- 缺失输入不会乱补
- 高风险内容会提示人工确认
- 输出能直接进入下一步
- 常见问题已经被模板、规则或审校机制吸收
