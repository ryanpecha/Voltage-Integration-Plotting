# Voltage-Integration-Plotting

All commands are listed for Powershell

---

## **Plotting Data**

```cmd
python.exe .\Main.py
```

### **Arguments - Data Plotting**

| Arg Name | Default Arg Value      | Arg Value Type | Example               |
| -------- | ---------------------- | -------------- | --------------------- |
| filePath | sampleIntegrations.txt | String         | -filePath myData.txt |

---

## **Generating Sample Data**

```cmd
python.exe .\GenerateSampleIntegrations.py
```

### **Arguments - Data Generation**

| Arg Name         | Default Arg Value      | Arg Value Type | Example               |
| ---------------- | ---------------------- | -------------- | --------------------- |
| filePath         | sampleIntegrations.txt | string         | -filePath myData.txt |
| integrationCount | 10,000                 | int            | -integrationCount 100 |
| startTime        | 0                      | float          | -startTime 100        |
| timeStepMin      | 0.2                    | float          | -timeStepMin 0.25     |
| timeStepMax      | 0.2                    | float          | -timeStepMax 0.3     |
| voltageMin       | 0                      | float          | -voltageMin 0.1       |
| voltageMax       | 3.5                    | float          | -voltageMax 5         |

---

## **Example**

```cmd
python.exe .\GenerateSampleIntegrations.py -filePath myData.csv
python.exe .\Main.py -filePath myData.csv
```

![Plot of Generated Sample Data](./Figure_1.png "Plot of Generated Sample Data")
