# 常用命令

## 启动
```bash
codex --model gpt-5.4
```

## 查看可用 skills
```text
/skills
```

## 显式调用 skills
```text
$quick-capture
$morning-brief
$file-triage
$copy-workflow
$image-workflow
$video-workflow
$ppt-workflow
```

## Copy Workflow CLI
```powershell
uv run python scripts/copy_workflow.py template
uv run python scripts/copy_workflow.py classify --raw "我想在小红书发个育儿贴"
uv run python scripts/copy_workflow.py prompt --raw "写一个端午放假通知" --scene internal_notice --platform wechat_work --platform email --platform sms
```

## 常用提示词示例

### 只记录
```text
用 quick-capture 记下：
以后所有输出都先给结论，再给步骤。
```

### 做晨报
```text
用 morning-brief 基于 memory/current_focus.md 和 inbox/capture.md，给我今天的极简工作简报。
```

### 预演文件整理
```text
显式使用 $file-triage，对 D:\work\myclaw 做 dry-run，只展示计划，不要执行。
```

### 更新规则
```text
更新你的规则：
默认回答更短一点；如果只是记录，就不要自动扩展成长文方案。
```
