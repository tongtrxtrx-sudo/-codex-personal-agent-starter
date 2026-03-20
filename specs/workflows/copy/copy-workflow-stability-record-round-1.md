# 文案 Workflow 第一轮稳定性记录

## 基本信息
- Workflow 名称：文案 Workflow
- 日期：2026-03-18
- 测试人：Codex
- 记录基础：基于仓库内已落地的 5 组样例链路
- 当前状态：第 1 轮，已覆盖 5 / 5 个案例

> 说明：Case 1 到 Case 3 主要用于暴露原始问题；Case 4 和 Case 5 是在新增“渠道必保留字段表”和“长度约束表”后补测的样例。

## Case 1
- 场景：教培招生
- 示例路径：[copy-summer-course-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-summer-course-demo)
- 是否正确触发：是
- 是否保留关键事实：是
- 是否结构稳定：是
- 是否有人工确认点：是
- 主要问题：
  - 朋友圈文案版本 2 缺少联系方式
  - 短信文案信息过密、长度偏长
- 当前判断：可复用，但必须保留审校和人工确认

## Case 2
- 场景：行政通知
- 示例路径：[copy-admin-holiday-notice-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-admin-holiday-notice-demo)
- 是否正确触发：是
- 是否保留关键事实：是
- 是否结构稳定：是
- 是否有人工确认点：是
- 主要问题：
  - 邮件通知遗漏节日期间紧急联系人
  - 短信提醒遗漏联系人与动作提示
- 当前判断：可复用，但内部通知类场景对“联系人”和“动作提示”敏感度更高

## Case 3
- 场景：活动推广
- 示例路径：[copy-weekend-promo-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weekend-promo-demo)
- 是否正确触发：是
- 是否保留关键事实：是
- 是否结构稳定：是
- 是否有人工确认点：是
- 主要问题：
  - 海报标题版本 3 过长
  - 朋友圈文案版本 2 缺少价格和截止时间
- 当前判断：可复用，但短标题压缩和关键信息保留仍需审校兜底

## Case 4
- 场景：培训通知
- 示例路径：[copy-training-notice-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-training-notice-demo)
- 是否正确触发：是
- 是否保留关键事实：是
- 是否结构稳定：是
- 是否有人工确认点：是
- 主要问题：
  - 没有出现关键字段遗漏
  - 没有出现明显超长问题
  - 仅存在标题优先级的微调空间
- 当前判断：新增 guardrails 后，内部通知场景的结构稳定性明显更好

## Case 5
- 场景：门店服务提醒
- 示例路径：[copy-member-service-reminder-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-member-service-reminder-demo)
- 是否正确触发：是
- 是否保留关键事实：是
- 是否结构稳定：是
- 是否有人工确认点：是
- 主要问题：
  - 没有出现关键字段遗漏
  - 没有出现标题或短信超长
  - 主要剩余问题转为卖点表达轻重调整
- 当前判断：新增 guardrails 后，服务提醒场景的漏项和超长问题得到明显压制

## 汇总判断
- 最容易出错的环节：Step 2 主结果生成，尤其是在多渠道改写和短文本压缩时
- 最常见问题：
  - 联系方式缺失
  - 截止时间或价格缺失
  - 标题或短信过长
  - 不同渠道对同一组关键信息保留不一致
- 是否适合继续复用：是，适合继续复用
- 复用前提：
  - 必须保留 `copy-reviewer`
  - 必须保留人工确认
  - 不应把初稿直接视为可外发成品
- 优化观察：
  - Case 1 到 Case 3 仍暴露出关键信息遗漏和长度问题
  - Case 4 和 Case 5 在新增 guardrails 后，没有再出现明显字段遗漏或超长问题
  - 当前问题开始从“结构性漏项”转向“表达优先级和文案细节优化”

## 下一步建议
1. 用新增 guardrails 回头重跑 Case 1 到 Case 3，确认旧案例是否也能同步改善
2. 为文案 workflow 增加“内部通知标题模板”和“服务提醒标题模板”
3. 把同样的 guardrail 思路迁移到图片、视频和 PPT workflow
