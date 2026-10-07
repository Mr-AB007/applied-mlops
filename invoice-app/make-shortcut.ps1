# Creates a "MITRSETU Billing" shortcut on the Desktop and in the Start Menu.
# It opens index.html in its own app window (no tabs or address bar) with the MITRSETU icon.
$dir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$html = Join-Path $dir 'index.html'
$icon = Join-Path $dir 'mitrsetu.ico'
$url  = ([System.Uri]$html).AbsoluteUri

# Chrome first (keeps your saved bills folder and invoice counter), then Edge.
$browsers = @(
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
  "$env:LocalAppData\Google\Chrome\Application\chrome.exe",
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe"
)
$browser = $browsers | Where-Object { $_ -and (Test-Path $_) } | Select-Object -First 1

$shell = New-Object -ComObject WScript.Shell
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
  $lnk.WorkingDirectory = $dir
  $lnk.Description      = 'MITRSETU Bill Maker'
  $lnk.Save()
}

Write-Host ''
Write-Host 'Done! "MITRSETU Billing" is now on your Desktop and in the Start Menu.'
if ($browser) { Write-Host "It opens with: $browser" } else { Write-Host 'Chrome/Edge not found - it will open in your default browser.' }
Write-Host 'Do not move or rename this folder, or the shortcut will stop working.'
Write-Host '(If you move it, just run "Create Desktop Shortcut" again.)'
