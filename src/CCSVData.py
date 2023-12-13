import csv
from abc import abstractmethod


class CSVData:
    def __init__(
        self,
        fpath: str,
        validBodyColCount: None or int = None,
    ) -> None:
        self.validBodyColCount = validBodyColCount
        with open(fpath, newline="") as openFile:
            csvReader = csv.reader(openFile)
            tempRows = [row for row in csvReader]
        self.rows: list[list] = []
        # break when csv item count per row doesn't match valid count
        if validBodyColCount != None:
            for row in reversed(tempRows):
                if len(row) != validBodyColCount:
                    break
                self.rows.append(row)
        # break when change in csv item count per row
        else:
            prevRowLen: int = len(tempRows[-1])
            for row in reversed(tempRows):
                rowLen = len(row)
                if rowLen != prevRowLen:
                    break
                self.rows.append(row)
                prevRowLen = rowLen
        self.rows.reverse()

    def isValidData(self) -> bool:
        return len(self.rows) > 1

    @staticmethod
    @abstractmethod
    def isValidFile(fpath: str) -> bool:
        pass
