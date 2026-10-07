@echo off
title MITRSETU Billing - create shortcut
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0make-shortcut.ps1"
echo.
pause
