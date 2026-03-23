# Workflow 顶层入口

## 目标
给 Codex、OpenClaw 或其他智能体提供统一的一句话 workflow 调用入口，不要求用户手动拆到底层 skills。

## 推荐原则
- 日常使用：调用顶层 workflow
- 测试排错：再拆到底层 skills
- 如果智能体支持 skill 发现，就用 `$workflow-name`
- 如果不支持 skill 发现，就直接引用 workflow 文档路径

## 1. 文案 Workflow

### Skill 入口
```text
显式使用 $copy-workflow。按文案 workflow 处理下面需求，默认只输出最终推荐版本、备选版本、待确认项；如果我说“展开链路”，再显示结构化 brief、文案初稿、审校结果。
```

### 通用文档入口
```text
按 D:\work\myclaw\codex-personal-agent-starter\specs\workflows\copy\copy-workflow.md 处理下面需求，默认只输出最终推荐版本、备选版本、待确认项；如果我说“展开链路”，再显示结构化 brief、文案初稿、审校结果。
```

适用输入现在包括：
- 活动推广
- 内部通知
- 培训通知
- 服务提醒
- 会议通知
- 工作汇报 / 周报总结
- 招聘文案
- 客户跟进
- 小红书 / 朋友圈 / 微博 / 抖音 / 知乎 / B站 / 微信公众号 / 视频号 / 快手 内容帖

## 2. 图片 Workflow

### Skill 入口
```text
显式使用 $image-workflow。按图片 workflow 处理下面需求，输出 visual brief、3个视觉方向、brand review、待确认项。
```

### 通用文档入口
```text
按 D:\work\myclaw\codex-personal-agent-starter\specs\workflows\image\image-workflow.md 处理下面需求，并输出视觉 brief、方向 prompts、品牌审校、待确认项。
```

## 3. 视频 Workflow

### Skill 入口
```text
显式使用 $video-workflow。按视频 workflow 处理下面需求，输出选题方向、脚本、分镜审校、待确认项。
```

### 通用文档入口
```text
按 D:\work\myclaw\codex-personal-agent-starter\specs\workflows\video\video-workflow.md 处理下面需求，并输出选题方向、脚本初稿、分镜审校、待确认项。
```

## 4. PPT Workflow

### Skill 入口
```text
显式使用 $ppt-workflow。按 PPT workflow 处理下面需求，输出 presentation brief、目录结构、页面初稿、待确认项。
```

### 通用文档入口
```text
按 D:\work\myclaw\codex-personal-agent-starter\specs\workflows\ppt\ppt-workflow.md 处理下面需求，并输出 presentation brief、目录结构、页面初稿、待确认项。
```

## 使用建议
- 如果你只想一句话调用，用上面任一入口即可
- 如果结果不稳，再拆到底层 skills 单独测试
- 顶层 workflow 的输出应该始终保留最终人工确认项
- 顶层 workflow 默认应优先交付结果，内部节点只在调试或显式展开时展示
- 如果你先想判断“这是哪类文案需求”，先看 [文案 workflow 分类模型.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/文案 workflow 分类模型.md)
- 如果你只想最快复制一句来调用，直接看 [文案 workflow 最省力调用模板.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/文案 workflow 最省力调用模板.md)
- 如果你想让任何 agent 通过 CLI 调用，直接看 [copy-runner-interface.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-runner-interface.md)
