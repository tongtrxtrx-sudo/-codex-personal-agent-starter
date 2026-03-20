# Copy Workflow Runner Interface

## Goal
Provide a script-driven interface that any agent can call without depending on local skill discovery.

## Runner
- Script path: [scripts/copy_workflow.py](D:/work/myclaw/codex-personal-agent-starter/scripts/copy_workflow.py)
- Preferred execution:

```powershell
uv run python scripts/copy_workflow.py <command> [options]
```

## Commands

### 1. `template`
Print a request template that matches the request contract.

### 2. `classify`
Read raw input and return:
- inferred scene
- inferred platforms
- inferred purpose
- minimal intake questions
- likely missing fields

### 3. `prompt`
Build a canonical prompt packet that another agent can use directly.

### 4. `validate-request`
Validate a JSON request file against the request contract.

### 5. `validate-response`
Validate a JSON response file against the response contract.

## Contracts
- Request contract: [copy-request.schema.json](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-request.schema.json)
- Response contract: [copy-output.schema.json](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-output.schema.json)

## Example

```powershell
uv run python scripts/copy_workflow.py classify --raw "我想在小红书发个育儿贴"
```

```powershell
uv run python scripts/copy_workflow.py prompt --raw "写一个端午放假通知" --scene internal_notice --platform wechat_work --platform email --platform sms
```

## Encoding Note
- For Chinese or long multi-line content, prefer `--input-file` over `--raw`.
- This avoids terminal encoding issues and keeps the runner packet stable across agents and shells.

## Design Rules
- The runner should not depend on any hosted model.
- It should prepare the workflow packet and contracts for other agents.
- It should stay deterministic and lightweight.
