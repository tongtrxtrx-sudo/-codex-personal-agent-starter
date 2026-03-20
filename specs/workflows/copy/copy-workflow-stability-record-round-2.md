# 文案 Workflow 第二轮稳定性记录

## 基本信息
- Workflow 名称：文案 Workflow
- 日期：2026-03-18
- 测试人：Codex
- 记录基础：对第一轮中问题最明显的 3 个旧案例进行 guardrail 重跑
- 当前状态：第 2 轮，已完成 3 / 3 个旧案例回跑

## Case 1
- 场景：教培招生
- 原始案例：[copy-summer-course-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-summer-course-demo)
- 重跑初稿：[copy-draft-guardrail-rerun.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-summer-course-demo/copy-draft-guardrail-rerun.md)
- 重跑审校：[review-result-guardrail-rerun.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-summer-course-demo/review-result-guardrail-rerun.md)
- 优化前问题：
  - 朋友圈文案版本 2 缺少联系方式
  - 短信文案信息过密、长度偏长
- 优化后结果：
  - 朋友圈文案两个版本都保留了联系方式
  - 短信已压缩到关键字段最小集合
- 当前判断：明显改善

## Case 2
- 场景：行政通知
- 原始案例：[copy-admin-holiday-notice-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-admin-holiday-notice-demo)
- 重跑初稿：[copy-draft-guardrail-rerun.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-admin-holiday-notice-demo/copy-draft-guardrail-rerun.md)
- 重跑审校：[review-result-guardrail-rerun.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-admin-holiday-notice-demo/review-result-guardrail-rerun.md)
- 优化前问题：
  - 邮件通知遗漏紧急联系人
  - 短信提醒缺少联系人和动作提示
- 优化后结果：
  - 邮件通知保留了联系人
  - 短信同时保留了时间、动作和联系人
- 当前判断：明显改善

## Case 3
- 场景：活动推广
- 原始案例：[copy-weekend-promo-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weekend-promo-demo)
- 重跑初稿：[copy-draft-guardrail-rerun.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weekend-promo-demo/copy-draft-guardrail-rerun.md)
- 重跑审校：[review-result-guardrail-rerun.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weekend-promo-demo/review-result-guardrail-rerun.md)
- 优化前问题：
  - 海报标题版本 3 过长
  - 朋友圈文案版本 2 缺少价格和报名截止时间
- 优化后结果：
  - 海报标题版本 3 已压到长度约束内
  - 朋友圈文案版本 2 已补齐价格和截止时间
  - 短信保留了截止时间、动作和报名入口
- 当前判断：明显改善

## 第二轮汇总
- 核心变化：
  - “关键信息遗漏”从高频问题降为低频问题
  - “标题和短信超长”得到直接压制
  - 输出开始更稳定地遵守渠道边界
- 当前剩余问题：
  - 标题版本的优先级选择
  - 同一场景下不同版本的表达风格轻重
  - 仍然需要人工确认最终对外入口和正式口径
- 当前判断：
  - 文案 workflow 已从“容易漏项”提升到“结构基本稳定”
  - 继续保留 `copy-reviewer` 和人工确认后，可以进入更大范围复用

## 下一步建议
1. [x] 把“标题模板”继续细分为招生、通知、提醒三类
2. [x] 为文案 workflow 增加“版本选择规则”，减少版本过多但优先级不清的问题
3. 把同样的 guardrail 方法迁移到图片、视频和 PPT workflow
