import os
import pickle
import pytest
import pytest_check as check
from src.components.CCSVData import CSVData


@pytest.mark.parametrize(
    "fpath,artifactPath",
    [
        [
            "./../samples/sample1_run.csv",
            "./artifacts/artifact_csvData.sample1.pickle",
        ],
        [
            "./../samples/sample2_run.csv",
            "./artifacts/artifact_csvData.sample2.pickle",
        ],
    ],
)
def test_csvData_sample(fpath: str, artifactPath: str):
    fpath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), fpath))
    csvData: CSVData = CSVData(fpath)
    artifactPath: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), artifactPath)
    )
    with open(artifactPath, "rb") as fopen:
        artifact: CSVData = pickle.load(fopen)
    check.equal(csvData.validBodyColCount, artifact.validBodyColCount)
    check.equal(csvData.rows, artifact.rows)
