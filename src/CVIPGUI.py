import os
import sys
import ctypes
import matplotlib
import pandas as pd
from tkinter import Tk
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox
from CCSVProcessing import CSVProcessing
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
        self.floor: float = 0

        # file data
        self.fpathRun: str | None = None
        self.fpathTargets: str | None = None
        self.expectedAblationCount: int = 0

        # gui refs
        figure, axes = plt.subplots()

        # styling the plot
        figure.set_facecolor((self.figureShade, self.figureShade, self.figureShade))
        axes.set_facecolor((self.axesShade, self.axesShade, self.axesShade))

        # setup for plotting the primary integration data
        plt.plot([], [], linewidth=1, label="Voltage")
        plt.subplots_adjust(bottom=0.2)
        plt.title("Ablations On Voltage Integrations")
        plt.xlabel(f"Time Secs [ {0} , {0} ]")
        plt.ylabel(f"Voltage V [ {0} , {0} ]")

        # initializing and drawing the floor line
        self.floorCoordXs = [0, 0]
        self.floorCoordYs = [0, 0]
        (self.floorLine,) = plt.plot(
            self.floorCoordXs,
            self.floorCoordYs,
            color="purple",
            linewidth=1,
            linestyle="dashed",
            label=f"Floor V : {self.floor}",
        )

        # initializing the plot items and plot legend
        (self.pltList_expectedAblationCount,) = plt.plot(
            [],
            [],
            "o",
            color="black",
            markersize=0,
            label=f"Expected Ablations : -",
        )
        (self.pltList_unidentifiedAblationCount,) = plt.plot(
            [], [], "o", color="black", markersize=0, label="Unidentified Ablations : -"
        )
        (self.pltList_detectedAblations,) = plt.plot(
            [], [], "x", color="green", markersize=5, label="Detected Ablations : -"
        )
        (self.pltList_detectedAnomalies,) = plt.plot(
            [], [], "x", color="purple", markersize=5, label="Detected Anomalies : -"
        )
        (self.pltList_detectedMissingAblations_flat,) = plt.plot(
            [], [], "x", color="red", markersize=5, label="Detected Missing : -"
        )
        (self.pltList_detectedMissingAblations_intersect,) = plt.plot(
            [], [], "+", color="red", markersize=5, label="Detected Miss (Intersection)"
        )
        # init and ref to legend
        self.pltLegend = plt.legend(
            facecolor=(self.figureShade, self.figureShade, self.figureShade)
        )

        # alternating styles for every other plotted coord
        shade1 = 0.00
        shade2 = 0.20
        self.altColors = ((shade1, shade1, shade1), (shade2, shade2, shade2))
        self.altAlignments = ("top", "bottom")
        self.altStyles = ("normal", "italic")
        self.altSizes = (7, 8)

        #
        left = 0.125
        bottom = 0.05
        width = 0.775
        height = 0.05
        pltFloorAxis = plt.axes([left, bottom, width, height])
        self.floorIncrement = 0.001
        self.pltFloorSlider = Slider(
            ax=pltFloorAxis,
            label="Floor V",
            valmin=-1,
            valmax=1,
            valinit=0,
            valstep=self.floorIncrement,
            track_color=(self.axesShade, self.axesShade, self.axesShade),
        )

        #
        left = 0
        bottom = 0
        width = 0.5
        height = 0.05
        pltFloorAxis = plt.axes([left, bottom, width, height])
        self.buttonSelectRunFile = Button(
            ax=pltFloorAxis,
            label="Run File\n(SELECT)",
        )
        self.buttonSelectRunFile.on_clicked(self.userSelectRunFile)

        #
        left = 0.5
        bottom = 0
        width = 0.5
        height = 0.05
        pltFloorAxis = plt.axes([left, bottom, width, height])
        self.buttonSelectTargetFile = Button(
            ax=pltFloorAxis,
            label="Target File\n(SELECT)",
        )
        self.buttonSelectTargetFile.on_clicked(self.userSelectTargetFile)

    def userSelectRunFile(self, event) -> None:
        """ """
        # csv of voltages after run
        initDir = None if self.fpathRun == None else os.path.dirname(self.fpathRun)
        fpath = askopenfilename(
            title="SELECT CSV RUN FILE",
            parent=self.root,
            initialfile=self.fpathRun,
            initialdir=initDir,
        )
        if fpath == "":
            return
        if not CSVProcessing.isValidRunFile(fpath):
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
            None if self.fpathTargets == None else os.path.dirname(self.fpathTargets)
        )
        fpath = askopenfilename(
            title="SELECT CSV TARGET FILE",
            parent=self.root,
            initialfile=self.fpathTargets,
            initialdir=initDir,
        )
        if fpath == "":
            return
        if not CSVProcessing.isValidTargetFile(fpath):
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
        self.buttonSelectRunFile.label.set_text(f"Run File\n({labelPath})")
        self.fpathRun = fpath
        self.plot()

    def setTargetFile(self, fpath: str) -> None:
        """ """
        labelPath = os.path.basename(fpath)
        self.buttonSelectTargetFile.label.set_text(f"Target File\n({labelPath})")
        self.fpathTargets = fpath
        self.plot()

    def plot(self) -> None:
        """ """
        if self.fpathRun != None:
            pass
        if self.fpathTargets != None:
            pass
        # if self.fpathRun != None and self.fpathTargets != None:

    def launch(self) -> None:
        """ """
        plt.show()
