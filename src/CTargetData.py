from CCSVData import CSVData
from matplotlib import pyplot as plt
from pandas.core.indexing import _iLocIndexer


class TargetData(CSVData):
    """ """

    def __init__(self, fpath: str) -> None:
        super().__init__(fpath)
        # removing header
        if (
            len(self.rows) > 0
            and len(self.rows[0]) > 0
            and self.rows[0][0].strip() == "Scan Type"
        ):
            print("removing header : ", self.rows[0])
            self.rows = self.rows[1:]

    @staticmethod
    def isValidFile(fpath: str) -> bool:
        return CSVData(fpath).isValidData()

    def getTargetCount(self) -> int:
        return len(self.rows)
