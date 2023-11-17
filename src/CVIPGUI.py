import os
import sys
import platform
import matplotlib
import pandas as pd
from tkinter import Tk
from matplotlib import pyplot
from matplotlib.widgets import Slider
from tkinter.filedialog import askopenfilename


class VIPGUI:
    def __init__(self, root: Tk) -> None:
        self.root = root

        #
        self.figureShade = 0.75
        self.axesShade = 0.85

        #
        self.floor = 0
        #
        self.expectedAblationCount = 0

        #
        figure, axes = pyplot.subplots()

        # styling the plot
        figure.set_facecolor((self.figureShade, self.figureShade, self.figureShade))
        axes.set_facecolor((self.axesShade, self.axesShade, self.axesShade))

        # setup for plotting the primary integration data
        pyplot.plot([], [], linewidth=1, label="Voltage")
        pyplot.subplots_adjust(bottom=0.2)
        pyplot.title("Ablations On Voltage-Integrations")
        pyplot.xlabel(f"Time-Stamp SECONDS [ {0} , {0} ]")
        pyplot.ylabel(f"Voltage V [ {0} , {0} ]")

        # initializing and drawing the floor line
        self.floorCoordsX = [0, 0]
        self.floorCoordsY = [0, 0]
        (self.floorLine,) = pyplot.plot(
            self.floorCoordsX,
            self.floorCoordsY,
            color="purple",
            linewidth=1,
            linestyle="dashed",
            label=f"Floor : {self.floor}",
        )

        # initializing the plot items and plot legend
        (self.pltList_expectedAblations,) = pyplot.plot(
            [],
            [],
            "o",
            color="black",
            markersize=0,
            label=f"Expected Ablations : {self.expectedAblationCount}",
        )
        (self.pltList_detectedAblations,) = pyplot.plot(
            [], [], "x", color="green", markersize=5, label="Detected Ablations : "
        )
        (self.pltList_detectedAnomalies,) = pyplot.plot(
            [], [], "x", color="purple", markersize=5, label="Detected Anomalies : "
        )
        (self.pltList_detectedMissingAblations_flat,) = pyplot.plot(
            [], [], "x", color="red", markersize=5, label="Detected Missing : "
        )
        (self.pltList_detectedMissingAblations_intersect,) = pyplot.plot(
            [], [], "+", color="red", markersize=5, label="Detected Miss Intersect"
        )
        (self.pltList_unidentified,) = pyplot.plot(
            [], [], "o", color="black", markersize=0, label=f"Unidentified : "
        )

        # plot text attributes
        alignments = ("top", "bottom")
        shade1 = 0.00
        shade2 = 0.20
        colors = ((shade1, shade1, shade1), (shade2, shade2, shade2))
        styles = ("normal", "italic")
        sizes = (7, 8)

    def plot(self) -> None:
        pass

    def launch(self) -> None:
        pyplot.show()
