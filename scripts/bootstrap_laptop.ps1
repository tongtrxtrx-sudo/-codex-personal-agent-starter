param(
    [switch]$ForceGlobalAgents
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

$requiredPaths = @(
    (Join-Path $repoRoot "AGENTS.md"),
    (Join-Path $repoRoot "AGENTS.global.example.md"),
    (Join-Path $repoRoot ".codex\config.toml"),
    (Join-Path $repoRoot ".agents\skills"),
    (Join-Path $repoRoot "memory\profile.md"),
    (Join-Path $repoRoot "memory\current_focus.md"),
    (Join-Path $repoRoot "commands.md")
)

$missing = @()
foreach ($path in $requiredPaths) {
    if (-not (Test-Path $path)) {
        $missing += $path
    }
}

if ($missing.Count -gt 0) {
    Write-Host "Missing required repository files:" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host "  $_" -ForegroundColor Red }
    exit 1
}

$globalCodexDir = Join-Path $HOME ".codex"
$globalAgentsTarget = Join-Path $globalCodexDir "AGENTS.md"
$globalAgentsSource = Join-Path $repoRoot "AGENTS.global.example.md"

New-Item -ItemType Directory -Force -Path $globalCodexDir | Out-Null

$copiedGlobalAgents = $false
if (-not (Test-Path $globalAgentsTarget)) {
    Copy-Item $globalAgentsSource $globalAgentsTarget -Force
    $copiedGlobalAgents = $true
} elseif ($ForceGlobalAgents) {
    Copy-Item $globalAgentsSource $globalAgentsTarget -Force
    $copiedGlobalAgents = $true
}

$hasCodex = $null -ne (Get-Command codex -ErrorAction SilentlyContinue)
$hasUv = $null -ne (Get-Command uv -ErrorAction SilentlyContinue)

Write-Host ""
Write-Host "Laptop bootstrap completed." -ForegroundColor Green
Write-Host ""
Write-Host "Repository root:" -ForegroundColor Cyan
Write-Host "  $repoRoot"
Write-Host ""
Write-Host "Repository-local assets verified:" -ForegroundColor Cyan
Write-Host "  AGENTS.md"
Write-Host "  .codex/config.toml"
Write-Host "  .agents/skills/"
Write-Host "  memory/profile.md"
Write-Host "  memory/current_focus.md"
Write-Host "  commands.md"
Write-Host ""

if ($copiedGlobalAgents) {
    Write-Host "Global Codex AGENTS installed:" -ForegroundColor Cyan
    Write-Host "  $globalAgentsTarget"
} else {
    Write-Host "Global Codex AGENTS left unchanged:" -ForegroundColor Yellow
    Write-Host "  $globalAgentsTarget"
}

Write-Host ""
Write-Host "Tool check:" -ForegroundColor Cyan
Write-Host ("  codex: " + ($(if ($hasCodex) { "found" } else { "missing" })))
Write-Host ("  uv:    " + ($(if ($hasUv) { "found" } else { "missing" })))

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Open a terminal in this repository."
Write-Host "  2. Run: codex --model gpt-5.4"
Write-Host "  3. If needed, review memory/profile.md and memory/current_focus.md."
Write-Host ""
Write-Host "Optional note:" -ForegroundColor Cyan
Write-Host "  OpenClaw local runtime config is not migrated by this script."
