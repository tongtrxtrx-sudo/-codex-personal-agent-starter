# 笔记本迁移说明

## 目标

把这个仓库里的 Codex 工作台配置迁移到另一台笔记本上，并尽量减少重复配置成本。

## 仓库内已包含的内容

以下内容已经在仓库中版本化，会随着仓库一起迁移：

- `AGENTS.md`
- `AGENTS.global.example.md`
- `.codex/config.toml`
- `.agents/skills/`
- `memory/profile.md`
- `memory/current_focus.md`
- `inbox/`
- `commands.md`
- `scripts/`
- `specs/`

## 默认不随仓库迁移的内容

以下内容属于机器本地配置，不会因为复制仓库而自动迁移：

- `~/.codex/AGENTS.md`
- `~/.openclaw/`
- 本地应用登录状态
- 钉钉令牌、插件状态、频道绑定
- 系统级 Node.js、Python、`uv`、Codex CLI 安装

如果你还想复用旧笔记本的 OpenClaw 运行时行为，需要单独迁移 `~/.openclaw/`，并且先检查其中是否包含敏感信息。

## 推荐迁移路径

### 1. 迁移仓库

任选一种方式：

- 用 Git 克隆
- 直接复制仓库目录
- 打包成 zip 后在笔记本解压

### 2. 在笔记本安装基础工具

建议至少准备：

- Node.js
- Codex CLI
- Python
- `uv`

示例：

```powershell
npm i -g @openai/codex
```

### 3. 运行初始化脚本

在笔记本的仓库根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap_laptop.ps1
```

这个脚本会：

- 检查关键仓库文件是否齐全
- 在本机缺失时创建 `~/.codex/`
- 在合适情况下把 `AGENTS.global.example.md` 复制到 `~/.codex/AGENTS.md`
- 输出后续启动步骤

### 4. 在仓库中启动 Codex

```powershell
codex --model gpt-5.4
```

## 可选：复用已有全局 AGENTS

如果笔记本上已经有自己的 `~/.codex/AGENTS.md`，不要直接覆盖。

只有在你明确要替换全局默认规则时，才使用强制参数：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap_laptop.ps1 -ForceGlobalAgents
```

## 验证清单

迁移后建议确认这些项目：

- `codex` 能在仓库中正常启动
- 仓库级 `AGENTS.md` 能被识别
- `.agents/skills/` 存在
- `memory/profile.md` 和 `memory/current_focus.md` 存在
- `.codex/config.toml` 存在
- 如果你需要全局默认规则，`~/.codex/AGENTS.md` 已存在

## 说明

- 这份说明有意把 OpenClaw 看作单独的机器本地层。
- 仓库内配置应保持可移植。
- 本地敏感信息应单独迁移，并在复用前复核。
