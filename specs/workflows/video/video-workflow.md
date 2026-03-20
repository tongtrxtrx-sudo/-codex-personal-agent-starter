# 视频 Workflow

## 目标
先把视频策划链路做稳，包括选题、脚本、分镜和发布文案，再谈更重的自动化和剪辑。

## 适用场景
- 短视频选题策划
- 口播脚本生成
- 分镜草案整理
- 发布文案和评论区引导语准备

## 不适用场景
- 直接自动生成完整视频成片
- 没有统一 brief 的随机内容输出
- 法务、医疗、金融等高风险内容的自动发布

## 核心 Skills
1. [video-angle-generator](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/video-angle-generator/SKILL.md)
2. [script-writer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/script-writer/SKILL.md)
3. [storyboard-reviewer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/storyboard-reviewer/SKILL.md)

## 标准流程
### Step 1：选题方向生成
- 输入：活动 brief、目标受众、平台、卖点
- 输出：3 个左右可比较的视频方向
- 每个方向包含：标题、钩子、核心卖点、情绪风格

### Step 2：脚本生成
- 输入：选定方向 + 活动 brief
- 输出：30 到 60 秒可口播脚本
- 建议结构：
  - 前 3 秒钩子
  - 痛点或共鸣
  - 课程或方案亮点
  - 报名信息
  - CTA

### Step 3：分镜与发布检查
- 输入：脚本 + 活动 brief
- 输出：
  - 分镜表
  - 封面标题
  - 发布文案
  - 评论区引导语
- 同时检查脚本是否好拍、是否好讲、是否便于发布

### Step 4：人工确认
- 拍摄前确认脚本与分镜
- 发布前确认文案、CTA、封面标题和关键信息

## 最低交付物
- 一组视频方向
- 一条脚本
- 一份分镜表
- 一条发布文案
- 一条评论区引导语

## 人工确认清单
- [ ] 钩子不过度夸张
- [ ] 价格、日期、联系方式正确
- [ ] 脚本适合口播
- [ ] 分镜可执行，不抽象
- [ ] 发布文案适合平台和品牌口径

## 测试清单
- 连续运行 5 次，检查选题是否重复
- 检查脚本是否自然可说
- 检查分镜是否可拍
- 检查 CTA 是否清晰
- 检查是否出现夸张或不当承诺

## 完成标准
- 团队能稳定产出“选题 -> 脚本 -> 分镜 -> 发布文案”链路
- 每一环都有明确可检查结果
- 内容上线前有明确人工把关点
