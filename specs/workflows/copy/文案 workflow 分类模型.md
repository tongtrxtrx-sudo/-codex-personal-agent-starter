# 文案 Workflow 分类模型

## 目标
把文案 workflow 的分类体系理顺成 3 层，避免把“工作 / 社交 / 娱乐”和“小红书 / 微博 / 抖音”混在同一层使用。

## 结论
文案 workflow 最合理的分类方式是：

1. 场景层：决定要补问什么、输出什么结构
2. 平台层：决定怎么写、写多长、写成什么样
3. 目的层：决定语气、转化强度和表达重心

## 一、场景层

> 这是 workflow 真正的主分类。

### 已覆盖场景
- 活动推广
- 内部通知
- 培训通知
- 服务提醒
- 会议通知
- 工作汇报 / 周报总结
- 会议纪要 / 会后同步
- 招聘文案
- 客户跟进 / 服务通知
- 社交媒体内容帖
- 娱乐内容 / 视频简介

### 场景层负责什么
- 决定最少需要补问哪些字段
- 决定输出结构应该是什么
- 决定哪些信息必须保留
- 决定哪些地方必须人工确认

### 对应规则
- [copy-scene-intake-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-scene-intake-rules.md)
- [copy-work-scene-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-work-scene-rules.md)

## 二、平台层

> 这是适配层，不是主分类。

### 已覆盖平台
- 小红书
- 朋友圈
- 微博
- 抖音
- 知乎
- B站
- 微信公众号
- 视频号
- 快手

### 平台层负责什么
- 决定输出格式
- 决定长度和节奏
- 决定标题写法
- 决定互动或 CTA 的强弱

### 对应规则
- [copy-social-platform-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-social-platform-rules.md)
- [copy-channel-length-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-length-rules.md)

## 三、目的层

> 这是表达层，用来调语气，不直接替代场景层。

### 推荐目的分类
- 通知 / 同步
- 推广 / 转化
- 分享 / 表达
- 互动 / 传播
- 记录 / 包装

### 目的层负责什么
- 决定语气轻重
- 决定是否强调动作
- 决定是否适合弱引导还是强引导
- 决定信息是偏完整还是偏情绪

## 四、工作 / 社交 / 娱乐 应该放在哪一层

### 正确用法
- `工作 / 社交 / 娱乐` 适合做导航分类
- 不适合直接做 workflow 的执行主分类

### 原因
- `工作` 太大，不足以直接决定补问字段
- `社交` 更像传播属性，不像稳定场景
- `娱乐` 更像内容气质，不像固定流程

### 推荐映射
- `工作`
  - 对应到：通知、汇报、会议纪要、招聘、客户跟进等场景
- `社交`
  - 对应到：小红书、朋友圈、微博、视频号等平台
- `娱乐`
  - 对应到：B站、抖音、快手等平台下的内容包装场景

## 五、执行顺序

每次处理文案需求时，建议按这个顺序判断：

1. 先判定场景层
2. 再判定平台层
3. 最后判定目的层

一句话记法：

`先看这是什么事，再看发到哪，最后看想达到什么效果。`

## 六、示例

### 例 1
“端午节放假通知”
- 场景层：内部通知
- 平台层：企业微信 / 邮件 / 短信
- 目的层：通知 / 同步

### 例 2
“小红书育儿经验帖”
- 场景层：社交媒体内容帖
- 平台层：小红书
- 目的层：分享 / 表达

### 例 3
“B站视频标题和简介”
- 场景层：娱乐内容 / 视频简介
- 平台层：B站
- 目的层：记录 / 包装

### 例 4
“AI 项目周报”
- 场景层：工作汇报 / 周报总结
- 平台层：企业微信 / 邮件
- 目的层：通知 / 同步

## 七、与现有文案 Workflow 的关系

这份分类模型不是替代现有规则，而是给现有规则提供总导航。

对应关系如下：
- 场景补问：看 [copy-scene-intake-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-scene-intake-rules.md)
- 工作场景：看 [copy-work-scene-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-work-scene-rules.md)
- 平台适配：看 [copy-social-platform-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-social-platform-rules.md)
- 执行入口：看 [copy-workflow.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-workflow.md)

## 八、使用建议

- 日常判断需求类型时，先看这份分类模型
- 真正执行时，再进入具体规则文档
- 如果以后新增平台或场景，先补这份分类模型，再补规则和案例
