:: install py dependencies via pip
python3 -m pip install -r %0"/../requirements.txt"
:: adding "Open with VIP" command to file explorer
set regKey="HKEY_CLASSES_ROOT\*\shell\Open with VIP"
reg add %regKey%
reg add %regKey%\command /t REG_EXPAND_SZ /d """%0\..\VoltageIntegrationPlotter.bat"" """%%1""""
:: adding shortcut to desktop
@echo off
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%userprofile%\Desktop\voltageIntegrationPlotter.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%~dp0\voltageIntegrationPlotter.bat" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs
:: adding shortcut to start menu
@echo off
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\voltageIntegrationPlotter.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%~dp0\voltageIntegrationPlotter.bat" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs
pause
