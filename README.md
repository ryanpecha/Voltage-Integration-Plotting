# Voltage-Integration-Plotting

## Generating Sample Data

```cmd
python.exe .\GenerateSampleIntegrations.py`
```

### Arguments

| Arg Name | Default Arg Value      | Arg Value Type | Example               |
| -------- | ---------------------- | -------------- | --------------------- |
| filePath | sampleIntegrations.txt | String         | -filePath myData.txt |

## Plotting Data

```cmd
python.exe .\Main.py`
```

### Arguments

| Arg Name         | Default Arg Value      | Arg Value Type | Example               |
| ---------------- | ---------------------- | -------------- | --------------------- |
| filePath         | sampleIntegrations.txt | string         | -filePath myData.txt |
| integrationCount | 10,000                 | int            | -integrationCount 100 |
| startTime        | 0                      | float          | -startTime 100        |
| timeStepMin      | 0.2                    | float          | -timeStepMin 0.25     |
| timeStepMax      | 0.2                    | float          | -timeStepMax 0.3     |
| voltageMin       | 0                      | float          | -voltageMin 0.1       |
| voltageMax       | 3.5                    | float          | -voltageMax 5         |
