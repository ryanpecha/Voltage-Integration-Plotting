from CCSVData import CSVData
from matplotlib import pyplot as plt
from pandas.core.indexing import _iLocIndexer


class TargetData(CSVData):
    """ """

    validBodyColCount: int = 9

    def __init__(self, fpath: str, plot: plt) -> None:
        self.plot = plot
        super().__init__(fpath, TargetData.validBodyColCount)

    @staticmethod
    def isValidFile(fpath: str) -> bool:
        return CSVData(fpath, TargetData.validBodyColCount).isValidData()

    def getTargetCount(self) -> int:
        return len(self.rows)

    def update() -> None:
        pass

    def plot(self) -> None:
        pass
