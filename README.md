# Voltage-Integration-Plotting

## **Dependencies**

* Python 3.10.8
* All commands are listed for Powershell
* All dependencies are listed @ `requirements.txt`
* UI variation indicates you are missing PyQT5

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

| Arg Name       | Default Arg Value      | Arg Value Type | Example                    |
| -------------- | ---------------------- | -------------- | -------------------------- |
| iPath          | sampleIntegrations.csv | string         | -iPath myIntegrations.csv |
| aPath          | sampleAblations.csv    | string         | -aPath myAblations.csv     |
| timeStampIndex | 0                      | int            | -timeStampIndex 11         |
| voltageIndex   | 1                      | int            | -voltageIndex 0            |
| vertexIndex  | 0                      | int            | -vertexIndex 5           |

---

## **Generating Sample Data**

```cmd
python.exe .\GenerateSampleIntegrations.py
```

### **Arguments - Integration Data Generation**

| Arg Name         | Default Arg Value      | Arg Value Type | Example                    |
| ---------------- | ---------------------- | -------------- | -------------------------- |
| iPath            | sampleIntegrations.csv | string         | -iPath myIntegrations.csv |
| aPath            | sampleAblations.csv    | string         | -aPath myAblations.csv     |
| startTime        | 0                      | float          | -startTime 100             |
| integrationCount | 10,000                 | int            | -integrationCount 100      |
| timeStep         | 0.2                    | float          | -timeStep 0.25             |
| voltageMin       | 0                      | float          | -voltageMin 0.1            |
| voltageMax       | 3.5                    | float          | -voltageMax 5              |
| voltageStepmax   | 0.1                    | float          | -voltageMaxStep 0.2        |

---

## **Output Example**

```cmd
python.exe .\PlotIntegrations.py -timeStampIndex 11 -voltageIndex 1 -vertexIndex 5
```

**YIELDS:**

![Plot of Generated Sample Data](./Figure_1.png "Plot of Existing Sample Data")

**ZOOMED:**

![Plot of Generated Sample Data](./Figure_2.png "Plot of Existing Sample Data - ZOOMED")
