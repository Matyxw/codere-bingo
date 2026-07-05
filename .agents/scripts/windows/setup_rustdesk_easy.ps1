param()
$ErrorActionPreference='SilentlyContinue'
$dest = "$env:USERPROFILE\Downloads\rustdesk-setup.exe"
$url = 'https://github.com/rustdesk/rustdesk/releases/latest/download/rustdesk-setup.exe'
if (-not (Test-Path $dest)) {
  Invoke-WebRequest -Uri $url -OutFile $dest
}
Start-Process -FilePath $dest -ArgumentList '--silent' -Wait
'RUSTDESK_INSTALLER_LAUNCHED'
