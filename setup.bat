cd %0"\.."
set regKey="HKEY_CLASSES_ROOT\*\shell\Open with VIP"
python3.11 -m pip install -r "./requirements.txt"
reg add %regKey%
reg add %regKey%\command /t REG_SZ /d %0"\..\voltageIntegrationPlotter.bat"
pause
