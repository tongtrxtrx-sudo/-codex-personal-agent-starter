param(
    [Parameter(Position = 0, Mandatory = $true)]
    [string]$Action,
    [Parameter(Position = 1)]
    [string]$InputFile
)

$ErrorActionPreference = "Stop"
$repo = "D:\work\myclaw\codex-personal-agent-starter"

function Pause-Exit {
    Write-Host ""
    Read-Host "Press Enter to exit" | Out-Null
}

function Select-InputFile {
    param(
        [string]$Title,
        [string]$Filter
    )

    try {
        Add-Type -AssemblyName System.Windows.Forms | Out-Null
        $dialog = New-Object System.Windows.Forms.OpenFileDialog
        $dialog.Title = $Title
        $dialog.Filter = $Filter
        $dialog.Multiselect = $false
        $dialog.RestoreDirectory = $true
        $result = $dialog.ShowDialog()
        if ($result -eq [System.Windows.Forms.DialogResult]::OK) {
            return $dialog.FileName
        }
    }
    catch {
        return $null
    }

    return $null
}

function Ensure-InputFile {
    param(
        [string]$CurrentValue,
        [string]$PromptText,
        [string]$DialogTitle = "Select input file",
        [string]$DialogFilter = "Text and Markdown (*.txt;*.md)|*.txt;*.md|All files (*.*)|*.*"
    )

    $value = $CurrentValue
    if ([string]::IsNullOrWhiteSpace($value)) {
        $value = Select-InputFile -Title $DialogTitle -Filter $DialogFilter
    }
    if ([string]::IsNullOrWhiteSpace($value)) {
        $value = Read-Host $PromptText
    }
    if (-not (Test-Path $value)) {
        throw "File not found: $value"
    }
    return (Resolve-Path $value).Path
}

function Invoke-UvCommand {
    param(
        [string[]]$CommandArgs
    )

    Push-Location $repo
    try {
        & uv @CommandArgs
    }
    finally {
        Pop-Location
    }
}

try {
    if (-not (Test-Path $repo)) {
        throw "Repo path not found: $repo"
    }

    if ($Action -eq "template") {
        Write-Host ""
        Write-Host "[Copy Workflow] Request template"
        Write-Host ""
        Invoke-UvCommand @("run", "python", "scripts/copy_workflow.py", "template")
    }
    elseif ($Action -eq "classify") {
        $resolved = Ensure-InputFile -CurrentValue $InputFile -PromptText "Enter txt/md file path" -DialogTitle "Select text or markdown file to classify"
        Write-Host ""
        Write-Host "[Copy Workflow] Classify input"
        Write-Host "Input file: $resolved"
        Write-Host ""
        Invoke-UvCommand @("run", "python", "scripts/copy_workflow.py", "classify", "--input-file", $resolved)
    }
    elseif ($Action -eq "prompt") {
        $resolved = Ensure-InputFile -CurrentValue $InputFile -PromptText "Enter txt/md file path" -DialogTitle "Select text or markdown file to build a prompt packet"
        $scene = Read-Host "Enter scene (optional)"
        $platformsRaw = Read-Host "Enter platform(s), comma-separated (optional)"
        $purpose = Read-Host "Enter purpose (optional)"
        $mode = Read-Host "Enter display mode: default or expanded (default: default)"
        if ([string]::IsNullOrWhiteSpace($mode)) {
            $mode = "default"
        }

        $cmdArgs = @("run", "python", "scripts/copy_workflow.py", "prompt", "--input-file", $resolved, "--display-mode", $mode)
        if (-not [string]::IsNullOrWhiteSpace($scene)) {
            $cmdArgs += @("--scene", $scene)
        }
        if (-not [string]::IsNullOrWhiteSpace($purpose)) {
            $cmdArgs += @("--purpose", $purpose)
        }
        if (-not [string]::IsNullOrWhiteSpace($platformsRaw)) {
            $platforms = $platformsRaw.Split(",") | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }
            foreach ($platform in $platforms) {
                $cmdArgs += @("--platform", $platform)
            }
        }

        Write-Host ""
        Write-Host "[Copy Workflow] Build prompt packet"
        Write-Host "Input file: $resolved"
        Write-Host ""
        Invoke-UvCommand -CommandArgs $cmdArgs
    }
    elseif ($Action -eq "validate-request") {
        $resolved = Ensure-InputFile -CurrentValue $InputFile -PromptText "Enter request JSON file path" -DialogTitle "Select request JSON file" -DialogFilter "JSON files (*.json)|*.json|All files (*.*)|*.*"
        Write-Host ""
        Write-Host "[Copy Workflow] Validate request JSON"
        Write-Host "Input file: $resolved"
        Write-Host ""
        Invoke-UvCommand @("run", "python", "scripts/copy_workflow.py", "validate-request", "--file", $resolved)
    }
    elseif ($Action -eq "validate-response") {
        $resolved = Ensure-InputFile -CurrentValue $InputFile -PromptText "Enter response JSON file path" -DialogTitle "Select response JSON file" -DialogFilter "JSON files (*.json)|*.json|All files (*.*)|*.*"
        Write-Host ""
        Write-Host "[Copy Workflow] Validate response JSON"
        Write-Host "Input file: $resolved"
        Write-Host ""
        Invoke-UvCommand @("run", "python", "scripts/copy_workflow.py", "validate-response", "--file", $resolved)
    }
    else {
        throw "Unknown action: $Action"
    }
}
catch {
    Write-Host ""
    Write-Host ("Run failed: " + $_.Exception.Message)
}

Pause-Exit
