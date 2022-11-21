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
python.exe .\PlotIntegrations.py
```

### **Arguments - Data Plotting**

| Arg Name       | Default Arg Value      | Arg Value Type | Example                    | Description                                               |
| -------------- | ---------------------- | -------------- | -------------------------- | --------------------------------------------------------- |
| iPath          | sampleIntegrations.csv | string         | -iPath myIntegrations.csv | Path to your voltage integrations csv file                |
| aPath          | sampleAblations.csv    | string         | -aPath myAblations.csv     | Path to your ablations csv file                           |
| timeStampIndex | 0                      | int            | -timeStampIndex 11         | Column index of your voltage timeStamps (iPath)           |
| voltageIndex   | 1                      | int            | -voltageIndex 0            | Column index of your voltage values (iPath)              |
| vertexIndex    | 0                      | int            | -vertexIndex 5             | Column index of your ablation vertices (aPath)            |
| iStartRowIndex | 0                      | int            | -iStartRowIndex 20         | Starting row index of your integrations csv data (iPath) |
| aStartRowIndex | 0                      | int            | -aStartRowIndex 20         | Starting row index of your ablations csv (aPath)         |

## **Output Example**

```cmd
python.exe .\PlotIntegrations.py -timeStampIndex 11 -voltageIndex 1 -vertexIndex 5
```

**YIELDS:**

![Plot of Generated Sample Data](./Figure_1.png "Plot of Existing Sample Data")

**ZOOMED:**

![Plot of Generated Sample Data](./Figure_2.png "Plot of Existing Sample Data - ZOOMED")
