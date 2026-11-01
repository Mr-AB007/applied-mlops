# MITRSETU Billing - installer
# Copies the app to this PC (no admin rights needed), creates Desktop + Start Menu icons and opens the app.
# Running it again updates the app; your bills, invoice numbers and settings are kept.
$ErrorActionPreference = 'Stop'
try {
  $here = Split-Path -Parent $MyInvocation.MyCommand.Path
  $src  = Join-Path $here 'app'
  $dest = Join-Path $env:LOCALAPPDATA 'MITRSETU Billing'

  Write-Host ''
  Write-Host '  Installing MITRSETU Billing ...'
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  Copy-Item -Path (Join-Path $src '*') -Destination $dest -Recurse -Force
  Get-ChildItem -Path $dest -Recurse -File | Unblock-File -ErrorAction SilentlyContinue

  $html = Join-Path $dest 'index.html'
  $icon = Join-Path $dest 'mitrsetu.ico'
  $url  = ([System.Uri]$html).AbsoluteUri

  # Chrome first, then Edge (Edge is on every Windows 10/11 PC).
  $browsers = @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LocalAppData\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe"
  )
  $browser = $browsers | Where-Object { $_ -and (Test-Path $_) } | Select-Object -First 1

  $shell  = New-Object -ComObject WScript.Shell
  $places = @(
    [Environment]::GetFolderPath('Desktop'),
    (Join-Path ([Environment]::GetFolderPath('StartMenu')) 'Programs')
  )
  foreach ($place in $places) {
    $lnk = $shell.CreateShortcut((Join-Path $place 'MITRSETU Billing.lnk'))
    if ($browser) {
      $lnk.TargetPath = $browser
      $lnk.Arguments  = "--app=`"$url`""
    } else {
      $lnk.TargetPath = $html
    }
    $lnk.IconLocation     = "$icon,0"
    $lnk.WorkingDirectory = $dest
    $lnk.Description      = 'MITRSETU Billing - GST / Non-GST bills and quotations'
    $lnk.Save()
  }

  Write-Host ''
  Write-Host '  DONE! MITRSETU Billing is installed.' -ForegroundColor Green
  Write-Host "  Installed in : $dest"
  if ($browser) { Write-Host "  Opens with   : $browser" } else { Write-Host '  Chrome/Edge not found - it will open in your default browser.' }
  Write-Host '  Open it any time from the "MITRSETU Billing" icon on your Desktop or in the Start Menu.'
  Write-Host ''

  if ($browser) { Start-Process -FilePath $browser -ArgumentList "--app=`"$url`"" } else { Start-Process -FilePath $html }
}
catch {
  Write-Host ''
  Write-Host '  Installation failed:' -ForegroundColor Red
  Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
  Write-Host '  Please send a photo of this window for help.'
}
