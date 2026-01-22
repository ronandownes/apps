# PowerShell script to push E:\Apps to GitHub
# Save this as push_apps.ps1

# Change to E: drive
Set-Location E:\

# Change to Apps directory
Set-Location E:\Apps

# Git operations
Write-Host "=== Starting Git Operations ===" -ForegroundColor Green

# Add all changes
git add .

# Commit with timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Auto-push from E:\Apps - $timestamp"

# Push to remote
git push origin main  # or use 'master' if that's your branch name

# Check status
git status

Write-Host "=== Push Complete! ===" -ForegroundColor Green
Write-Host "Repository: RonanDownes/Apps" -ForegroundColor Cyan