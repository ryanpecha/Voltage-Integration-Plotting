# Voltage-Integration-Plotting

## **Dependencies**

* Python 3.10.8
* All commands are listed for Powershell
* All dependencies are listed @ `requirements.txt`

### **Installing Dependencies**

```cmd
pip install -r .\requirements.txt
```

---

## **Plotting Data**

```cmd
python.exe .\Main.py
```

### **Arguments - Data Plotting**

| Arg Name | Default Arg Value      | Arg Value Type | Example                 |
| -------- | ---------------------- | -------------- | ----------------------- |
| iPath    | sampleIntegrations.csv | String         | -iPath myAblations.csv |
| aPath    | sampleAblations.csv    | String         | -aPath                  |

---

## **Generating Sample Data**

```cmd
python.exe .\GenerateSampleIntegrations.py
```

### **Arguments - Integration Data Generation**

| Arg Name         | Default Arg Value      | Arg Value Type | Example                    |
| ---------------- | ---------------------- | -------------- | -------------------------- |
| iPath            | sampleIntegrations.csv | string         | -iPath myIntegrations.csv |
| integrationCount | 10,000                 | int            | -integrationCount 100      |
| startTime        | 0                      | float          | -startTime 100             |
| timeStepMin      | 0.2                    | float          | -timeStepMin 0.25          |
| timeStepMax      | 0.2                    | float          | -timeStepMax 0.3          |
| voltageMin       | 0                      | float          | -voltageMin 0.1            |
| voltageMax       | 3.5                    | float          | -voltageMax 5              |
| voltageStepmax   | 0.1                    | float          | -voltageMaxStep 0.2        |

### **Arguments - Integration Data Generation**

| Arg Name | Default Arg Value   | Arg Value Type | Example                 |
| -------- | ------------------- | -------------- | ----------------------- |
| aPath    | sampleAblations.csv | string         | -aPath myAblations.csv |

---

## **Output Example**

```cmd
python.exe .\GenerateSampleData.py -iPath myIntegrations.csv -aPath myAblations.csv
python.exe .\Main.py -iPath myIntegrations.csv -aPath myAblations.csv
```

**EQUIVALENT TO:**

```cmd
python.exe .\GenerateSampleData.py
python.exe .\Main.py
```

**YIELDS:**

![Plot of Generated Sample Data](./Figure_1.png "Plot of Generated Sample Data")
