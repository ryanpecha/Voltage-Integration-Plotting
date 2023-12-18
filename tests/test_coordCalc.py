import os
import pickle
import pytest
import pytest_check as check
from matplotlib import pyplot as plt
from src.components.CRunData import RunData
from src.components.CCoordCalc import CoordCalc
from src.components.CTargetData import TargetData


@pytest.mark.parametrize(
    "fpath_runFile,fpath_targetFile,artifactPath",
    [
        [
            "./../samples/sample1_run.csv",
            "./../samples/sample1_targets_scancsv.csv",
            "./artifacts/artifact_coordCalc.sample1.pickle",
        ],
        [
            "./../samples/sample2_run.csv",
            "./../samples/sample2_targets_scancsv.csv",
            "./artifacts/artifact_coordCalc.sample2.pickle",
        ],
    ],
)
def test_coordCalc_sample(fpath_runFile: str, fpath_targetFile: str, artifactPath: str):
    fpath_runFile: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), fpath_runFile)
    )
    fpath_targetFile: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), fpath_targetFile)
    )
    artifactPath: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), artifactPath)
    )
    runData: RunData = RunData(fpath_runFile)
    targetData: TargetData = TargetData(fpath_targetFile)
    coordCalc: CoordCalc = CoordCalc()
    floorVal: float = 0.182
    coordCalc.updateAblationsAndAnomalies(
        floorVal=floorVal, voltages=runData.voltages, timeStamps=runData.timeStamps
    )
    coordCalc.updateMissingAndErrors(
        voltages=runData.voltages,
        timeStamps=runData.timeStamps,
        expectedAblationCount=targetData.getTargetCount(),
    )
    figurePlot = plt.gca()
    coordCalc.updateCoordText(figurePlot)
    with open(artifactPath, "rb") as fopen:
        artifact: CoordCalc = pickle.load(fopen)
    check.equal(coordCalc.ablationCoordsX, artifact.ablationCoordsX)
    check.equal(coordCalc.ablationCoordsY, artifact.ablationCoordsY)
    check.equal(coordCalc.anomalyCoordsX, artifact.anomalyCoordsX)
    check.equal(coordCalc.anomalyCoordsY, artifact.anomalyCoordsY)
    check.equal(coordCalc.ablationTimeIndices, artifact.ablationTimeIndices)
    check.equal(coordCalc.missingCoordsX, artifact.missingCoordsX)
    check.equal(coordCalc.missingCoordsY, artifact.missingCoordsY)
    check.equal(coordCalc.missingCoordsFlatY, artifact.missingCoordsFlatY)
    check.equal(coordCalc.unidentifiedAblationCount, artifact.unidentifiedAblationCount)
    for coordCalcText, artifactText in zip(
        coordCalc.allCoordText, artifact.allCoordText
    ):
        check.equal(coordCalcText.get_text(), artifactText.get_text())
    check.equal(coordCalc.ablationTimeStepMode, artifact.ablationTimeStepMode)
    check.equal(coordCalc.averageAblationY, artifact.averageAblationY)
