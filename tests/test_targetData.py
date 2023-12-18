import os
import pickle
import pytest
import pytest_check as check
from src.components.CTargetData import TargetData


@pytest.mark.parametrize(
    "fpath,artifactPath",
    [
        [
            "./../samples/sample1_targets_scancsv.csv",
            "./artifacts/artifact_targetData.sample1.pickle",
        ],
        [
            "./../samples/sample2_targets_scancsv.csv",
            "./artifacts/artifact_targetData.sample2.pickle",
        ],
    ],
)
def test_targetData_sample(fpath: str, artifactPath: str):
    fpath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), fpath))
    targetData: TargetData = TargetData(fpath)
    artifactPath: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), artifactPath)
    )

    with open(artifactPath, "wb") as fopen:
        pickle.dump(targetData, fopen)
    with open(artifactPath, "rb") as fopen:
        artifact: TargetData = pickle.load(fopen)
    check.equal(targetData.rows, artifact.rows)
