from matplotlib.text import Text
from matplotlib.axes import Axes


class CoordCalc:
    def __init__(self) -> None:
        # detected ablation coordinates
        self.ablationCoordsX: list[float] = []
        self.ablationCoordsY: list[float] = []
        # anomalous coordinates
        self.anomalyCoordsX: list[float] = []
        self.anomalyCoordsY: list[float] = []
        # list of timestamps indices where ablations were detected
        self.ablationTimeIndices: list[int] = []
        # error coordinates
        self.missingCoordsX: list[float] = []
        self.missingCoordsY: list[float] = []
        self.missingCoordsFlatY: list[float] = []
        # unkown trailing / preceding missing ablations
        self.unidentifiedAblationCount: int = 0
        # text labelling coords
        self.allCoordText: list[Text] = []
        # analysis properties
        self.ablationTimeStepMode: float = 0
        self.averageAblationY: float = 0

    def updateAblationsAndAnomalies(
        self,
        floorVal: float,
        voltages: list[float],
        timeStamps: list[float],
    ) -> None:
        # detected ablation coordinates
        self.ablationCoordsX = []
        self.ablationCoordsY = []
        # anomalous coordinates
        self.anomalyCoordsX = []
        self.anomalyCoordsY = []
        # list of timestamps indices where ablations were detected
        self.ablationTimeIndices = []
        # current saddle properties
        saddleSize = 0
        saddleIndex = 0
        # iterating over time and voltage
        for i in range(1, len(timeStamps) - 1):
            # grabbing current voltage
            voltage = voltages[i]
            # ignoring coord when already above the floor
            if voltage > floorVal:
                continue
            # voltage decreased, shifting the saddle right
            if voltages[i - 1] > voltage:
                saddleIndex = i
            # increased beyond floor
            if voltages[i + 1] > floorVal:
                # anomalous ablation with saddle of size 0
                if saddleSize == 0:
                    self.anomalyCoordsX.append(timeStamps[saddleIndex])
                    self.anomalyCoordsY.append(voltages[saddleIndex])
                # valid ablation, adding to the list of detected ablations
                else:
                    self.ablationCoordsX.append(timeStamps[saddleIndex])
                    self.ablationCoordsY.append(voltages[saddleIndex])
                    self.ablationTimeIndices.append(saddleIndex)
                # resetting saddle size
                saddleSize = 0
            # saddle has grown
            else:
                saddleSize += 1

    def updateMissingAndErrors(
        self, voltages: list[float], timeStamps: list[float], expectedAblationCount: int
    ):
        # missing ablation coordinates
        self.missingCoordsX = []
        self.missingCoordsY = []
        self.missingCoordsFlatY = []

        # cannot locate missing ablations with only one detected ablation
        if len(self.ablationCoordsX) <= 1:
            return

        # calculating mode and allowable step
        timeSteps = {}
        for i in range(len(self.ablationCoordsX) - 1):
            curTime = self.ablationCoordsX[i]
            nextTime = self.ablationCoordsX[i + 1]
            timeStep = nextTime - curTime
            if timeStep in timeSteps:
                timeSteps[timeStep] += 1
            else:
                timeSteps[timeStep] = 1
        curAvgFreq = 0
        ablationTimeStepMode = 0
        for timeStep in timeSteps:
            if timeSteps[timeStep] > curAvgFreq:
                curAvgFreq = timeSteps[timeStep]
                ablationTimeStepMode = timeStep

        # backup mode using avg timeStep
        if curAvgFreq <= 1:
            ablationTimeStepMode = (
                self.ablationCoordsX[-1] - self.ablationCoordsX[0]
            ) / (len(self.ablationCoordsX) - 1)
        self.ablationTimeStepMode = ablationTimeStepMode

        # scaling time step overlap by 1.5 to allow for step variation
        allowableTimeStep = ablationTimeStepMode * 1.5
        averageAblationY = 0
        for y in self.ablationCoordsY:
            averageAblationY += y
        averageAblationY /= len(self.ablationCoordsY)
        self.averageAblationY = averageAblationY

        # calculating missing ablations
        for i in range(0, len(self.ablationCoordsX) - 1):
            # grabbing current values from detected ablations
            curTime = self.ablationCoordsX[i]
            nextTime = self.ablationCoordsX[i + 1]
            distance = nextTime - curTime

            # identifying errors following from current ablation
            if distance > allowableTimeStep:
                missCount = int(distance / ablationTimeStepMode)
                timeIndex = self.ablationTimeIndices[i]

                # building misses following current ablation
                for m in range(1, missCount + 1):
                    # adding miss x
                    missTime = curTime + (ablationTimeStepMode * m)
                    self.missingCoordsX.append(missTime)
                    # calculating actual missing y value on plot
                    while timeStamps[timeIndex + 1] < missTime:
                        timeIndex += 1
                    x1 = timeStamps[timeIndex]
                    x2 = timeStamps[timeIndex + 1]
                    y1 = voltages[timeIndex]
                    y2 = voltages[timeIndex + 1]
                    slope = (y2 - y1) / (x2 - x1)
                    y = (slope * (missTime - x1)) + y1
                    # adding miss y
                    self.missingCoordsY.append(y)
                    self.missingCoordsFlatY.append(averageAblationY)

        # unkown trailing / preceding missing ablations
        self.unidentifiedAblationCount = (
            expectedAblationCount
            - len(self.missingCoordsX)
            - len(self.ablationCoordsX)
            - len(self.anomalyCoordsX)
        )

    def updateCoordText(self, figurePlot: Axes):
        # plot text attributes
        shade1 = 0.00
        shade2 = 0.20
        colors = ((shade1, shade1, shade1), (shade2, shade2, shade2))
        alignments = ("top", "bottom")
        styles = ("normal", "italic")
        sizes = (7, 8)
        # removing existing text from plot
        for text in self.allCoordText:
            text.remove()
        allCoordsText = []
        allCoordsX = sorted(
            self.ablationCoordsX + self.missingCoordsX + self.anomalyCoordsX
        )
        # ablations
        for i in range(len(self.ablationCoordsX)):
            x = self.ablationCoordsX[i]
            y = self.ablationCoordsY[i]
            globalIndex = allCoordsX.index(x)
            allCoordsText.append(
                figurePlot.text(
                    x=x,
                    y=y,
                    s=str(globalIndex),
                    fontsize=sizes[(globalIndex % 4) > 1],
                    color=colors[(globalIndex % 4) > 1],
                    verticalalignment=alignments[globalIndex % 2],
                    fontfamily="monospace",
                    fontstyle=styles[(globalIndex % 4) > 1],
                    alpha=0.75,
                )
            )
        # anomalies
        for i in range(len(self.anomalyCoordsX)):
            x = self.anomalyCoordsX[i]
            y = self.anomalyCoordsY[i]
            globalIndex = allCoordsX.index(x)
            allCoordsText.append(
                figurePlot.text(
                    x=x,
                    y=y,
                    s=str(globalIndex),
                    fontsize=sizes[(globalIndex % 4) > 1],
                    color=colors[(globalIndex % 4) > 1],
                    verticalalignment=alignments[globalIndex % 2],
                    fontfamily="monospace",
                    fontstyle=styles[(globalIndex % 4) > 1],
                    alpha=0.75,
                )
            )
        # errors / missing
        for i in range(len(self.missingCoordsX)):
            x = self.missingCoordsX[i]
            y = self.missingCoordsFlatY[i]
            globalIndex = allCoordsX.index(x)
            allCoordsText.append(
                figurePlot.text(
                    x=x,
                    y=y,
                    s=str(globalIndex),
                    fontsize=sizes[(globalIndex % 4) > 1],
                    color=colors[(globalIndex % 4) > 1],
                    verticalalignment=alignments[globalIndex % 2],
                    fontfamily="monospace",
                    fontstyle=styles[(globalIndex % 4) > 1],
                    alpha=0.75,
                )
            )
        # unidentified point labeling
        if self.unidentifiedAblationCount > 0:
            x = allCoordsX[-1] + (self.ablationTimeStepMode * 8)
            y = self.averageAblationY
            allCoordsText.append(
                figurePlot.text(
                    x=x,
                    y=y,
                    s=f"{self.unidentifiedAblationCount} UNIDENTIFIED",
                    fontsize=8,
                    color="red",
                    verticalalignment="bottom",
                    fontfamily="monospace",
                    fontstyle="normal",
                    alpha=1,
                )
            )
        # updating text ref
        self.allCoordText = allCoordsText
