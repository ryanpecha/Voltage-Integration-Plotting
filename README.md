
[![GitHub](https://img.shields.io/github/license/ryanpecha/Voltage-Integration-Plotting?color=blueviolet)](https://github.com/ryanpecha/Voltage-Integration-Plotting/blob/main/LICENSE.txt)

# Voltage-Integration-Plotting

## **Dependencies**

* Python 3.10.8
* Python must be installed with tkinter
* All commands are listed for Powershell
* All dependencies are listed @ `requirements.txt`
* UI variation indicates you are missing PyQT5
* Data must have more valid ablations than errors
* All indices start at 0, including index based args
* Start indices must not include column header data

### **Installing Dependencies**

```cmd
pip install -r .\requirements.txt
```

---

## **Plotting Data - Easy**

> Automatically prompts the user for necessary arguments

```cmd
python.exe .\EasyPlot.py
```

---

## **Plotting Data - Command Line**

> Requires the user to pass arguments via command line

```cmd
python.exe .\PlotIntegrations.py
```

## **Arguments - Data Plotting**

| Argument       | Default Value | Example                    | Description                                               |
| -------------- | ---------------------- | -------------------------- | --------------------------------------------------------- |
| iPath *string*         | sampleIntegrations.csv | -iPath myInts.csv | Path to your voltage integrations csv file                |
| aPath *string*         | sampleAblations.csv | -aPath myAbls.csv     | Path to your ablations csv file                           |
| iTimeStampIndex *int* | 0 | -iTimeStampIndex 11         | Column index of your voltage timeStamps |
| iVoltageIndex *int*   | 1 | -iVoltageIndex 0            | Column index of your voltage values |
| iStartRowIndex *int* | 0 | -iStartRowIndex 20         | Starting row index of your integration csv data |
| aStartRowIndex *int* | 0  | -aStartRowIndex 20         | Starting row index of your ablation csv data |

## **Run Example**

```cmd
python.exe .\PlotIntegrations.py -iTimeStampIndex 11 -iVoltageIndex 1
```

**YIELDS:**

![Plot of Generated Sample Data](./Figure_1.png "Plot of Existing Sample Data")

**ZOOMED:**

![Plot of Generated Sample Data](./Figure_2.png "Plot of Existing Sample Data - ZOOMED")
