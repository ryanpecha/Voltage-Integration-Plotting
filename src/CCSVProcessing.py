import pandas
from pandas import DataFrame
from pandas.core.indexing import _iLocIndexer


class CSVProcessing:
    @staticmethod
    def isValidRunFile(fpath: str) -> bool:
        return True
        pass

    @staticmethod
    def isValidTargetFile(fpath: str) -> bool:
        return False
        pass

    @staticmethod
    def loadDataFrameCSV(fpath: str) -> DataFrame:
        with open(fpath, "r") as openFile:
            dataframe = pandas.read_csv(
                openFile, engine="pyarrow", header=None, delimiter=","
            )
        return dataframe

    @staticmethod
    def extractRunTimes(runCSVDataFrame: DataFrame) -> _iLocIndexer:
        pass

    @staticmethod
    def extractRunVoltages(runCSVDataFrame: DataFrame) -> _iLocIndexer:
        pass
    
    @staticmethod
    def extractTarget(targetCSVDataFrame: DataFrame) -> _iLocIndexer:
        pass
    
