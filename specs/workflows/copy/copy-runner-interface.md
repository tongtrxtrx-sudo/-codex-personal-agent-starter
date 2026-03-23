# 文案 Workflow Runner 接口说明

## 目标
提供一个脚本驱动的接口，让任何 agent 都可以在不依赖本地 skill 自动发现的情况下调用 `copy workflow`。

## Runner
- 脚本路径：[scripts/copy_workflow.py](D:/work/myclaw/codex-personal-agent-starter/scripts/copy_workflow.py)
- 推荐执行方式：

```powershell
uv run python scripts/copy_workflow.py <command> [options]
```

## 可用命令

### 1. `template`
打印符合请求契约的输入模板。

### 2. `classify`
读取原始输入并返回：
- 推断场景
- 推断平台
- 推断目的
- 最少补问字段
- 可能缺失字段

### 3. `prompt`
构建一个可被其他 agent 直接使用的标准 prompt packet。

### 4. `validate-request`
按请求契约校验一个 JSON 请求文件。

### 5. `validate-response`
按响应契约校验一个 JSON 响应文件。

## 契约文件
- 请求契约：[copy-request.schema.json](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-request.schema.json)
- 响应契约：[copy-output.schema.json](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-output.schema.json)

## 示例

```powershell
uv run python scripts/copy_workflow.py classify --raw "我想在小红书发个育儿贴"
```

```powershell
uv run python scripts/copy_workflow.py prompt --raw "写一个端午放假通知" --scene internal_notice --platform wechat_work --platform email --platform sms
```

## 编码说明
- 中文或长多行内容优先使用 `--input-file`，不要优先用 `--raw`
- 这样可以减少终端编码问题，也能让不同 agent 和 shell 下的结果更稳定

## 设计原则
- runner 不依赖任何托管模型
- runner 负责准备 workflow packet 和契约
- runner 应保持确定性和轻量化
