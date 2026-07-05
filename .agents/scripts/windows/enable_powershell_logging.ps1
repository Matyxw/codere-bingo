$paths = @{
  'HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging' = @{ 'EnableScriptBlockLogging' = 1 }
  'HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ModuleLogging' = @{ 'EnableModuleLogging' = 1 }
}
foreach ($p in $paths.Keys) {
  if (-not (Test-Path $p)) { New-Item -Path $p -Force | Out-Null }
  $paths[$p].GetEnumerator() | ForEach-Object { Set-ItemProperty -Path $p -Name $_.Key -Value $_.Value }
}
'POWERSHELL_LOGGING_ENABLED'
