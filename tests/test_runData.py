import os
import pickle
import pytest
import pytest_check as check
from src.components.CRunData import RunData


@pytest.mark.parametrize(
    "fpath,artifactPath",
    [
        [
            "./../samples/sample1_run.csv",
            "./artifacts/artifact_runData.sample1.pickle",
        ],
        [
            "./../samples/sample2_run.csv",
            "./artifacts/artifact_runData.sample2.pickle",
        ],
    ],
)
def test_runData_sample(fpath: str, artifactPath: str):
    fpath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), fpath))
    runData: RunData = RunData(fpath)
    artifactPath: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), artifactPath)
    )
    with open(artifactPath, "rb") as fopen:
        artifact: RunData = pickle.load(fopen)
    check.equal(runData.timeStamps, artifact.timeStamps)
    check.equal(runData.voltages, artifact.voltages)
    check.equal(runData.timeStampMin, artifact.timeStampMin)
    check.equal(runData.timeStampMax, artifact.timeStampMax)
    check.equal(runData.voltageMin, artifact.voltageMin)
    check.equal(runData.voltageMax, artifact.voltageMax)
