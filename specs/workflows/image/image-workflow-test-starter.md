# 图片 Workflow 测试起步清单

## 目标
给图片 workflow 提供一份最小测试入口，帮助你先验证结构是否稳定，再决定要不要继续扩示例和场景。

## 最先要测的 4 件事
- [ ] 视觉 brief 是否完整
- [ ] 3 个方向是否真的不同
- [ ] prompt 和 negative prompt 是否足够具体
- [ ] 品牌审校是否能给出明确推荐和风险点

## 当前推荐测试案例
1. [summer-course-poster-demo](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/examples/summer-course-poster-demo)

## 测试产物
- `raw-input.md`
- `visual-brief.json`
- `prompt-directions.md`
- `brand-review.md`

## 通过标准
- 方向不是同义改写
- 标题不过长
- 画面方向不廉价、不失真
- 审校意见可以直接指导下一步选择
