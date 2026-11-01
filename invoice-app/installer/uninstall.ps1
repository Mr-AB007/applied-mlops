# MITRSETU Billing - uninstaller. Removes the app and its icons.
# Your saved PDF bills (in the Bills folder you chose) are NOT touched.
$dest = Join-Path $env:LOCALAPPDATA 'MITRSETU Billing'
Write-Host ''
$ans = Read-Host '  Remove MITRSETU Billing from this PC? Your saved PDF bills are kept. (Y/N)'
if ($ans -notmatch '^[Yy]') { Write-Host '  Nothing was removed.'; return }
$links = @(
  (Join-Path ([Environment]::GetFolderPath('Desktop')) 'MITRSETU Billing.lnk'),
  (Join-Path (Join-Path ([Environment]::GetFolderPath('StartMenu')) 'Programs') 'MITRSETU Billing.lnk')
)
foreach ($l in $links) { if (Test-Path $l) { Remove-Item -LiteralPath $l -Force } }
if (Test-Path $dest) { Remove-Item -LiteralPath $dest -Recurse -Force }
Write-Host '  MITRSETU Billing was removed. Your PDF bills are still in your Bills folder.' -ForegroundColor Green
