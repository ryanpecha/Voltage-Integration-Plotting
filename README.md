
[![GitHub](https://img.shields.io/github/license/ryanpecha/Voltage-Integration-Plotting?color=blueviolet)](https://github.com/ryanpecha/Voltage-Integration-Plotting/blob/main/LICENSE.txt)
![GitHub repo size](https://img.shields.io/github/repo-size/ryanpecha/Voltage-Integration-Plotting)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/ryanpecha/Voltage-Integration-Plotting)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ryanpecha/Voltage-Integration-Plotting)

# Voltage-Integration-Plotting

## **Dependencies**

* `Python 3.10`
* `tkinter` must be installed
* All commands are listed for `Powershell`
* UI variation indicates you are missing `PyQT5`
* All indices start at `0`, including index based args
* Data _**must**_ have more valid ablations than errors
* All dependencies are listed @ [`requirements.txt`](./requirements.txt)
* Start indices must _**not**_ include column header data

### **Installing Dependencies**

```cmd
pip install -r .\requirements.txt
```

---

## **Plotting Data - Easy Wizard** 

> Recommended for one time usage\
> Automatically prompts the user for necessary arguments

```cmd
python.exe .\EasyPlot.py
```

---

## **Plotting Data - Command Line**

> Recommended for reusable scripting\
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
