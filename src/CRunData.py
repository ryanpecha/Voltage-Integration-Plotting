from CCSVData import CSVData
from matplotlib import pyplot as plt


class RunData(CSVData):
    """ """

    validBodyColCount: int = 13

    def __init__(
        self,
        fpath: str,
        floorVal: float,
        figurePlot,
        plt_floorLine,
        plt_floorSlider,
        plt_voltageLine,
    ) -> None:
        self.figure = figurePlot
        self.plt_floorLine = plt_floorLine
        self.plt_floorSlider = plt_floorSlider
        self.plt_voltageLine = plt_voltageLine

        super().__init__(fpath, RunData.validBodyColCount)

        self.timeStamps = self.extractTimeStamps()
        self.voltages = self.extractVoltages()
        self.timeStampMin = min(self.timeStamps)
        self.timeStampMax = max(self.timeStamps)
        self.voltageMin = min(self.voltages)
        self.voltageMax = max(self.voltages)
        self.update(floorVal)

    @staticmethod
    def isValidFile(fpath: str) -> bool:
        return CSVData(fpath, RunData.validBodyColCount).isValidData()

    def extractTimeStamps(self) -> list[float]:
        timeStampColIndex: int = 11
        return [float(row[timeStampColIndex]) for row in self.rows]

    def extractVoltages(self) -> list[float]:
        voltageColIndex: int = 1
        return [float(row[voltageColIndex]) for row in self.rows]

    def update(self, floorVal: float) -> None:
        # drawing voltage data
        self.plt_voltageLine.set_xdata(self.timeStamps)
        self.plt_voltageLine.set_ydata(self.voltages)
        self.figure.set_xlim([self.timeStampMin, self.timeStampMax])
        self.figure.set_ylim([self.voltageMin, self.voltageMax])

        # drawing floor line
        self.plt_floorLine.set_xdata([self.timeStampMin, self.timeStampMax])
        self.plt_floorLine.set_ydata([floorVal, floorVal])
        
        # updating slider range
        self.plt_floorSlider.valmin = self.voltageMin
        self.plt_floorSlider.valmax = self.voltageMax
        self.plt_floorSlider.ax.set_xlim(self.plt_floorSlider.valmin,self.plt_floorSlider.valmax)
