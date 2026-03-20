# 文案 Workflow 示例索引

当前目录下的示例都用于测试和演示文案 workflow 的完整链路。

## 已有示例
1. [copy-summer-course-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-summer-course-demo)
   - 场景：教培招生
   - 类型：对外推广

2. [copy-admin-holiday-notice-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-admin-holiday-notice-demo)
   - 场景：行政通知
   - 类型：内部通知

3. [copy-weekend-promo-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weekend-promo-demo)
   - 场景：活动推广
   - 类型：对外推广

4. [copy-training-notice-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-training-notice-demo)
   - 场景：培训通知
   - 类型：内部通知

5. [copy-member-service-reminder-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-member-service-reminder-demo)
   - 场景：门店服务提醒
   - 类型：对外提醒

6. [copy-xiaohongshu-parenting-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-xiaohongshu-parenting-demo)
   - 场景：小红书育儿内容帖
   - 类型：社交媒体内容

7. [copy-weekly-report-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weekly-report-demo)
   - 场景：工作汇报 / 周报总结
   - 类型：工作场景

8. [copy-video-channel-preview-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-video-channel-preview-demo)
   - 场景：视频号活动预告
   - 类型：社交媒体内容

9. [copy-bilibili-video-intro-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-bilibili-video-intro-demo)
   - 场景：B站视频标题与简介
   - 类型：娱乐内容

10. [copy-meeting-followup-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-meeting-followup-demo)
   - 场景：会议纪要 / 会后同步
   - 类型：工作场景

11. [copy-wechat-article-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-wechat-article-demo)
   - 场景：微信公众号文章
   - 类型：社交媒体内容

12. [copy-weibo-short-post-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-weibo-short-post-demo)
   - 场景：微博短文案
   - 类型：社交媒体内容

13. [copy-douyin-short-caption-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/examples/copy-douyin-short-caption-demo)
   - 场景：抖音短视频配文
   - 类型：娱乐 / 短内容

## 统一文件结构
- `raw-input.md`
- `structured-brief.json`
- `copy-draft.md`
- `review-result.md`

对于需要做前后对比的旧案例，还会补：
- `copy-draft-guardrail-rerun.md`
- `review-result-guardrail-rerun.md`

## 推荐用法
- 先用教培招生案例做熟流程
- 再用行政通知案例测边界与渠道变化
- 再用活动推广案例测不同风格下的稳定性
- 再用培训通知和服务提醒案例验证新增 guardrails 是否生效
- 再用小红书内容帖案例验证平台型内容的补问和输出结构
- 再用周报、视频号和 B站案例检查工作 / 社交 / 娱乐覆盖是否完整
- 再用会议纪要、公众号、微博、抖音案例检查平台与场景覆盖是否均衡
