import csv
from abc import abstractmethod


class CSVData:
    def __init__(self, fpath: str, validBodyColCount: int) -> None:
        self.validBodyColCount = validBodyColCount
        with open(fpath, newline="") as openFile:
            csvReader = csv.reader(openFile)
            tempRows = [row for row in csvReader]
        self.rows: list[list] = []
        for row in reversed(tempRows):
            if len(row) != validBodyColCount:
                break
            self.rows.append(row)
        self.rows.reverse()

    def isValidData(self) -> bool:
        return len(self.rows) > 0

    @staticmethod
    @abstractmethod
    def isValidFile(fpath: str) -> bool:
        pass
