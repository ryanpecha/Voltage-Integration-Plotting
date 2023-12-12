import os
import ctypes
from tkinter import Tk
from CRunData import RunData
from CCoordCalc import CoordCalc
from CTargetData import TargetData
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.widgets import Button
from tkinter.filedialog import askopenfilename


class VIPGUI:
    """ """

    def __init__(self, root: Tk) -> None:
        """ """
        self.root: Tk = root

        # gui settings
        self.figureShade: float = 0.75
        self.axesShade: float = 0.85

        # user gui params
        self.floorVal: float = 0

        # file data
        self.fpathRunData: str | None = None
        self.runData: RunData | None = None
        self.fpathTargetData: str | None = None
        self.targetData: TargetData | None = None
        #
        self.coordCalc: CoordCalc = CoordCalc()

        # gui refs
        self.figure, self.axes = plt.subplots()
        self.figurePlot = plt.gca()
        self.legend = plt.legend(
            facecolor=(self.figureShade, self.figureShade, self.figureShade)
        )
        # styling the plot
        self.figure.set_facecolor(
            (self.figureShade, self.figureShade, self.figureShade)
        )
        self.axes.set_facecolor((self.axesShade, self.axesShade, self.axesShade))

        # setup for plotting the primary integration data
        (self.plt_voltageLine,) = plt.plot(
            [],
            [],
            linewidth=1,
            label="Voltage V",
        )
        plt.subplots_adjust(bottom=0.2)
        plt.title("Ablations On Voltage Integrations")
        plt.xlabel(f"Time Secs [ {0} , {0} ]")
        plt.ylabel(f"Voltage V [ {0} , {0} ]")

        # initializing and drawing the floor line
        (self.plt_floorLine,) = plt.plot(
            [0, 0],
            [0, 0],
            color="purple",
            linewidth=1,
            linestyle="dashed",
            label=f"Floor V : {self.floorVal}",
        )

        # initializing the plot items and plot legend
        (self.plt_expectedAblationCount,) = plt.plot(
            [],
            [],
            "o",
            color="black",
            markersize=0,
            label=f"Expected Ablations : -",
        )
        (self.plt_detectedAblations,) = plt.plot(
            [], [], "x", color="green", markersize=5, label="Detected Ablations : -"
        )
        (self.plt_detectedAnomalies,) = plt.plot(
            [], [], "x", color="purple", markersize=5, label="Detected Anomalies : -"
        )
        (self.plt_detectedMissingAblations_flat,) = plt.plot(
            [], [], "x", color="red", markersize=5, label="Detected Missing : -"
        )
        (self.plt_detectedMissingAblations_intersect,) = plt.plot(
            [], [], "+", color="red", markersize=5, label="Detected Miss (Intersection)"
        )
        (self.plt_unidentifiedAblationCount,) = plt.plot(
            [], [], "o", color="black", markersize=0, label="Unidentified Ablations : -"
        )
        # init and ref to legend
        self.plt_legend = plt.legend(
            facecolor=(self.figureShade, self.figureShade, self.figureShade)
        )

        # alternating styles for every other plotted coord
        shade1 = 0.00
        shade2 = 0.20
        self.altColors = ((shade1, shade1, shade1), (shade2, shade2, shade2))
        self.altAlignments = ("top", "bottom")
        self.altStyles = ("normal", "italic")
        self.altSizes = (7, 8)

        # floor value slider
        left = 0.125
        bottom = 0.05
        width = 0.775
        height = 0.05
        pltFloorAxis = plt.axes([left, bottom, width, height])
        self.floorIncrement = 0.001
        self.plt_floorSlider = Slider(
            ax=pltFloorAxis,
            label="Floor V",
            valmin=-1,  # to be set on file selection
            valmax=1,  # to be set on file selection
            valinit=0,
            valstep=self.floorIncrement,
            track_color=(self.axesShade, self.axesShade, self.axesShade),
        )
        self.plt_floorSlider.on_changed(self.setFloor)

        # run csv file selection button
        left = 0
        bottom = 0
        width = 0.5
        height = 0.05
        pltFloorAxis = plt.axes([left, bottom, width, height])
        self.plt_buttonSelectRunFile = Button(
            ax=pltFloorAxis,
            label="Run File\n(SELECT)",
        )
        self.plt_buttonSelectRunFile.on_clicked(self.userSelectRunFile)

        # target csv file selection button
        left = 0.5
        bottom = 0
        width = 0.5
        height = 0.05
        pltFloorAxis = plt.axes([left, bottom, width, height])
        self.plt_buttonSelectTargetFile = Button(
            ax=pltFloorAxis,
            label="Target File\n(SELECT)",
        )
        self.plt_buttonSelectTargetFile.on_clicked(self.userSelectTargetFile)

    def setFloor(self, val):
        self.floorVal = val
        self.plt_legend.get_texts()[1].set_text(f"Floor V : {self.floorVal}")
        self.update()

    def plotFloor(self):
        self.plt_floorLine.set_ydata([self.floorVal, self.floorVal])
        if self.runData != None:
            self.plt_floorLine.set_xdata(
                [self.runData.timeStampMin, self.runData.timeStampMax]
            )

    def userSelectRunFile(self, event) -> None:
        """ """
        # csv of voltages after run
        initDir = (
            None if self.fpathRunData == None else os.path.dirname(self.fpathRunData)
        )
        fpath = askopenfilename(
            title="SELECT CSV RUN FILE",
            parent=self.root,
            initialfile=self.fpathRunData,
            initialdir=initDir,
        )
        if fpath == "":
            return
        if not RunData.isValidFile(fpath):
            ctypes.windll.user32.MessageBoxW(
                0,
                f"The selected file is not a valid CSV Run file :\n{fpath}",
                "Invalid Run File",
                1,
            )
            return
        self.setRunFile(fpath)

    def userSelectTargetFile(self, event) -> None:
        """ """
        # csv of targets for a run
        initDir = (
            None
            if self.fpathTargetData == None
            else os.path.dirname(self.fpathTargetData)
        )
        fpath = askopenfilename(
            title="SELECT CSV TARGET FILE",
            parent=self.root,
            initialfile=self.fpathTargetData,
            initialdir=initDir,
        )
        if fpath == "":
            return
        if not TargetData.isValidFile(fpath):
            ctypes.windll.user32.MessageBoxW(
                0,
                f"The selected file is not a valid CSV Target file :\n{fpath}",
                "Invalid Target File",
                1,
            )
            return
        self.setTargetFile(fpath)

    def setRunFile(self, fpath: str) -> None:
        """ """
        labelPath = os.path.basename(fpath)
        self.plt_buttonSelectRunFile.label.set_text(f"Run File\n({labelPath})")
        self.fpathRunData = fpath
        self.runData = RunData(fpath)
        self.update()

    def setTargetFile(self, fpath: str) -> None:
        """ """
        labelPath = os.path.basename(fpath)
        self.plt_buttonSelectTargetFile.label.set_text(f"Target File\n({labelPath})")
        self.fpathTargetData = fpath
        self.targetData = TargetData(fpath)
        self.update()

    def update(self) -> None:
        """ """
        self.plotFloor()

        if self.fpathRunData != None:
            # drawing floor line
            self.plt_floorLine.set_xdata(
                [self.runData.timeStampMin, self.runData.timeStampMax]
            )
            self.plt_floorLine.set_ydata([self.floorVal, self.floorVal])
            # updating slider range
            self.plt_floorSlider.valmin = self.runData.voltageMin
            self.plt_floorSlider.valmax = self.runData.voltageMax
            self.plt_floorSlider.ax.set_xlim(
                self.runData.voltageMin, self.runData.voltageMax
            )
            # drawing voltage data
            self.plt_voltageLine.set_xdata(self.runData.timeStamps)
            self.plt_voltageLine.set_ydata(self.runData.voltages)
            self.figurePlot.set_xlim(
                [self.runData.timeStampMin, self.runData.timeStampMax]
            )
            self.figurePlot.set_ylim([self.runData.voltageMin, self.runData.voltageMax])

            # updating coordinate calculations
            if self.fpathTargetData != None:
                self.coordCalc.update(
                    self.floorVal,
                    self.runData.voltages,
                    self.runData.timeStamps,
                    self.targetData.getTargetCount(),
                )
                # plotting detected ablations
                self.plt_detectedAblations.set_xdata(self.coordCalc.ablationCoordsX)
                self.plt_detectedAblations.set_ydata(self.coordCalc.ablationCoordsY)
                # plotting detected ablations
                self.plt_detectedAnomalies.set_xdata(self.coordCalc.anomalyCoordsX)
                self.plt_detectedAnomalies.set_ydata(self.coordCalc.anomalyCoordsX)
                # updating the value fields of the legend
                # index 0 - voltage (annotation only)
                # index 1 - floor (updated by setFloor())
                # index 2 - expected ablations
                self.plt_legend.get_texts()[2].set_text(
                    f"Expected Ablations : {self.targetData.getTargetCount()}"
                )
                # index 3 - detected ablations
                self.plt_legend.get_texts()[3].set_text(
                    f"Detected Ablations : {len(self.coordCalc.ablationCoordsX)}"
                )
                # index 4 - detected anomolies
                self.plt_legend.get_texts()[4].set_text(
                    f"Detected Anomalies : {len(self.coordCalc.anomalyCoordsX)}"
                )
                # index 5 - detected missing
                self.plt_legend.get_texts()[5].set_text(
                    f"Detected Missing : {len(self.coordCalc.missingCoordsX)}"
                )
                # index 6 - detected missing (intersection) (annotation only)
                # index 7 - unidentified ablations
                self.plt_legend.get_texts()[7].set_text(
                    f"Unidentified Ablations : {self.coordCalc.unidentifiedAblationCount}"
                )

        # redrawing UI canvas
        self.figure.canvas.draw_idle()

    def launch(self) -> None:
        """ """
        plt.show()
