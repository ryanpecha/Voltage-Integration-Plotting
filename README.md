# Voltage-Integration-Plotting

## **Dependencies**

* Python 3.10.8
* All commands are listed for Powershell
* All dependencies are listed @ `requirements.txt`
* UI variation indicates you are missing PyQT5
* Data must have more valid ablations than errors
* All indices start at 0, including index based args
* Start indices should not include column header data

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

| Arg Name       | Default Arg Value      | Arg Value Type | Example                    | Description                                                                           |
| -------------- | ---------------------- | -------------- | -------------------------- | ------------------------------------------------------------------------------------- |
| iPath          | sampleIntegrations.csv | string         | -iPath myIntegrations.csv | Path to your voltage integrations csv file                                            |
| aPath          | sampleAblations.csv    | string         | -aPath myAblations.csv     | Path to your ablations csv file                                                       |
| timeStampIndex | 0                      | int            | -timeStampIndex 11         | Column index of your voltage timeStamps (indices start at 0) (file @ iPath)           |
| voltageIndex   | 1                      | int            | -voltageIndex 0            | Column index of your voltage values (indices start at 0) (file @ iPath)              |
| vertexIndex    | 0                      | int            | -vertexIndex 5             | Column index of your ablation vertices (indices start at 0) (file @ aPath)            |
| iStartRowIndex | 0                      | int            | -iStartRowIndex 20         | Starting row index of your integrations csv data (indices start at 0) (file @ iPath) |
| aStartRowIndex | 0                      | int            | -aStartRowIndex 20         | Starting row index of your ablations csv (indices start at 0) (file @ aPath)         |

---

## **Generating Sample Data**

```cmd
python.exe .\GenerateSampleIntegrations.py
```

### **Arguments - Integration Data Generation**

| Arg Name         | Default Arg Value      | Arg Value Type | Example                    | Description                                                          |
| ---------------- | ---------------------- | -------------- | -------------------------- | -------------------------------------------------------------------- |
| iPath            | sampleIntegrations.csv | string         | -iPath myIntegrations.csv | Path to your voltage integrations csv file                           |
| aPath            | sampleAblations.csv    | string         | -aPath myAblations.csv     | Path to your ablations csv file                                      |
| startTime        | 0                      | float          | -startTime 100             | Initial time for your generated data in seconds                      |
| integrationCount | 10,000                 | int            | -integrationCount 100      | Quantity of voltage integrations to generate                         |
| timeStep         | 0.2                    | float          | -timeStep 0.25             | Time distance between voltage integrations in seconds                |
| voltageMin       | 0                      | float          | -voltageMin 0.1            | Minimum voltage value of any integration (inclusive)                 |
| voltageMax       | 3.5                    | float          | -voltageMax 5              | Maximum voltage value of any integration (inclusive)                 |
| voltageStepmax   | 0.1                    | float          | -voltageMaxStep 0.2        | Maxmimum change in voltage between adjacent integrations (inclusive) |

---

## **Output Example**

```cmd
python.exe .\PlotIntegrations.py -timeStampIndex 11 -voltageIndex 1 -vertexIndex 5
```

**YIELDS:**

![Plot of Generated Sample Data](./Figure_1.png "Plot of Existing Sample Data")

**ZOOMED:**

![Plot of Generated Sample Data](./Figure_2.png "Plot of Existing Sample Data - ZOOMED")
