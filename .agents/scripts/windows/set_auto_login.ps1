param([string]$User='lucas_cardozo')
$reg = 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
Set-ItemProperty -Path $reg -Name 'AutoAdminLogon' -Value '1'
Set-ItemProperty -Path $reg -Name 'DefaultUsername' -Value $User
Set-ItemProperty -Path $reg -Name 'DefaultPassword' -Value ''
Set-ItemProperty -Path $reg -Name 'DefaultDomainName' -Value (Get-WmiObject Win32_ComputerSystem).DNSHostName
'AUTOLOGIN_CONFIGURED'
