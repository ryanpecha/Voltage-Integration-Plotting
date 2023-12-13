from CCSVData import CSVData
from matplotlib import pyplot as plt
from pandas.core.indexing import _iLocIndexer


class TargetData(CSVData):
    """ """

    def __init__(self, fpath: str) -> None:
        super().__init__(fpath)

    @staticmethod
    def isValidFile(fpath: str) -> bool:
        return CSVData(fpath).isValidData()

    def getTargetCount(self) -> int:
        return len(self.rows)
 