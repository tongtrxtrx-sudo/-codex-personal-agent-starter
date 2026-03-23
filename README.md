# Codex 个人智能体起步仓库

这个仓库的目标不是做一个重型代理平台，而是帮你用 ChatGPT Pro + Codex 快速搭起一个轻量、可扩展、适合个人长期使用的本地智能体工作台。

## 仓库结构

- `AGENTS.md`：仓库级行为规则，Codex 进入项目后会自动读取
- `AGENTS.global.example.md`：可复制到 `~/.codex/AGENTS.md` 的全局规则样板
- `.agents/skills/`：仓库级 skills，Codex 会自动发现
- `memory/`：长期偏好与当前重点
- `inbox/`：原始记录与快速收集区
- `commands.md`：常用启动命令与提示词示例
- `PERSONAL_AGENT_PLAYBOOK.md`：后续如何使用和培育这个智能体的长期手册

## 推荐启动流程

### 1. 安装并登录 Codex
```bash
npm i -g @openai/codex
codex
```

### 2. 复制全局规则模板
POSIX shell:
```bash
mkdir -p ~/.codex
cp AGENTS.global.example.md ~/.codex/AGENTS.md
```

PowerShell:
```powershell
New-Item -ItemType Directory -Force $HOME/.codex
Copy-Item AGENTS.global.example.md $HOME/.codex/AGENTS.md
```

### 3. 进入仓库目录
```bash
cd codex-personal-agent-starter
codex --model gpt-5.4
```

### 4. 优先修改这几个核心文件
- `AGENTS.md`
- `memory/profile.md`
- `memory/current_focus.md`

如果你想把这套系统真正培育成“自己的智能体”，这三个文件是最关键的入口。

## 建议的使用方式

### 快速记录
```text
用 quick-capture 记下：
以后所有输出都先给结论，再给步骤。
```

### 生成晨报
```text
用 morning-brief 基于当前本地文件给我今天的工作简报。
```

### 预演文件整理
```text
显式使用 $file-triage，先对 D:\work\myclaw 做 dry-run，只展示计划，不要直接执行。
```

## 设计原则

1. 轻量优先：能用短规则 + 小脚本解决，就不要做复杂平台。
2. 一 skill 一职责：每个 skill 尽量只负责一个稳定工作流。
3. 安全优先：删除、移动、重命名、联网、安装依赖都先确认。
4. 上下文节制：长期偏好放 `memory/`，不要全部挤进 `AGENTS.md`。
5. 从真实使用中成长：先用起来，再根据摩擦收紧规则和技能。

## 推荐下一步

- 连续一周每天使用 `quick-capture`
- 每次真实开工前跑一次 `morning-brief`
- 在多次 dry-run 后再逐步收紧 `file-triage`
- 当某类任务重复出现时，再新增 skill

## 长期入口

如果你之后忘了该怎么继续使用或培育这套智能体，直接打开：

`PERSONAL_AGENT_PLAYBOOK.md`
