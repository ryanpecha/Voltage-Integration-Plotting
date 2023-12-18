from .CCSVData import CSVData


class RunData(CSVData):
    """ """

    validBodyColCount: int = 13

    def __init__(
        self,
        fpath: str,
    ) -> None:
        super().__init__(fpath, RunData.validBodyColCount)
        # extracted
        self.timeStamps = self.extractTimeStamps()
        self.voltages = self.extractVoltages()
        # calculated
        self.timeStampMin = min(self.timeStamps)
        self.timeStampMax = max(self.timeStamps)
        self.voltageMin = min(self.voltages)
        self.voltageMax = max(self.voltages)

    @staticmethod
    def isValidFile(fpath: str) -> bool:
        return CSVData(fpath, RunData.validBodyColCount).isValidData()

    def extractTimeStamps(self) -> list[float]:
        timeStampColIndex: int = 11
        return [float(row[timeStampColIndex]) for row in self.rows]

    def extractVoltages(self) -> list[float]:
        voltageColIndex: int = 1
        return [float(row[voltageColIndex]) for row in self.rows]
