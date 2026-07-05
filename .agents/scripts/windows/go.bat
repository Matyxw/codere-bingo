@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\temp\enable_powershell_logging.ps1"
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\temp\set_auto_login.ps1"
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\temp\setup_canary.ps1"
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\temp\backup_config.ps1"
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\temp\recovery_5min.ps1"
