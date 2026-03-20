# Laptop Migration Guide

## Goal

Move the repository-local Codex workspace configuration to another laptop with the smallest possible setup cost.

## Included In This Repository

The following items are already versioned in this repository and should move with the repository itself:

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

## Not Included By Default

The following items are machine-local and do not automatically move with the repository:

- `~/.codex/AGENTS.md`
- `~/.openclaw/`
- local app logins
- DingTalk tokens, plugin states, and channel bindings
- system-level Node.js, Python, `uv`, or Codex CLI installation

If you also want the old laptop's OpenClaw runtime behavior, migrate `~/.openclaw/` separately and review secrets before reuse.

## Recommended Migration Path

### 1. Move The Repository

Use one of these options:

- clone from Git
- copy the repository folder directly
- create a zip and extract it on the laptop

### 2. Install Required Tools On The Laptop

Recommended minimum:

- Node.js
- Codex CLI
- Python
- `uv`

Example:

```powershell
npm i -g @openai/codex
```

### 3. Run The Bootstrap Script

From the repository root on the laptop:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap_laptop.ps1
```

This script will:

- verify that key repository files exist
- create `~/.codex/` if missing
- copy `AGENTS.global.example.md` to `~/.codex/AGENTS.md` when appropriate
- print the next commands to run

### 4. Start Codex In This Repository

```powershell
codex --model gpt-5.4
```

## Optional: Reuse Existing Global AGENTS

If the laptop already has a custom `~/.codex/AGENTS.md`, do not overwrite it blindly.

Use the bootstrap script with force only when you intentionally want to replace the laptop's global Codex defaults:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap_laptop.ps1 -ForceGlobalAgents
```

## Verification Checklist

After setup, verify these items:

- `codex` starts successfully in the repository
- repository `AGENTS.md` is detected
- `.agents/skills/` is present
- `memory/profile.md` and `memory/current_focus.md` are present
- `.codex/config.toml` is present
- `~/.codex/AGENTS.md` exists if you want global defaults

## Notes

- This guide intentionally treats OpenClaw as a separate machine-local layer.
- Repository-local configuration should stay portable.
- Machine-local secrets should be migrated manually and reviewed before reuse.
