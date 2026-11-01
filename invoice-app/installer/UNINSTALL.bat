@echo off
title MITRSETU Billing - Uninstall
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0uninstall.ps1"
echo.
pause
