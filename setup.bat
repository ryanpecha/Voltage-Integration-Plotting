cd %0"\.."
:: install py dependencies via pip
python3.11 -m pip install -r "./requirements.txt"
:: adding "Open with VIP" command to file explorer
set regKey="HKEY_CLASSES_ROOT\*\shell\Open with VIP"
reg add %regKey%
reg add %regKey%\command /t REG_SZ /d %0"\..\voltageIntegrationPlotter.bat"
:: TODO - icon reg key
:: adding shortcut to start menu
:: TODO - add to start menu
:: adding shortcut to desktop
:: TODO - add to desktop
pause
