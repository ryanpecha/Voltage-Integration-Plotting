cd %0"\.."
::python3.11 "./src/VoltageIntegrationProcessor.py" --hideTerminal %*
python3.11 "./src/VoltageIntegrationProcessor.py" %1
pause