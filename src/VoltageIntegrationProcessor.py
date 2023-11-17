import os
import sys
import platform
import matplotlib
import pandas as pd
import win32.win32gui
from tkinter import Tk
import win32.lib.win32con
from CVIPGUI import VIPGUI
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from tkinter.filedialog import askopenfilename


def main():
    """ """

    # hide running terminal
    if "--hideTerminal" in sys.argv:
        # only supported for windows
        if platform.system() == "windows":
            fgID: int = win32.win32gui.GetForegroundWindow()
            win32.win32gui.ShowWindow(fgID, win32.lib.win32con.SW_HIDE)

    # hide running terminal
    if "--clearTerminal" in sys.argv:
        os.system("cls||clear")

    # bringing root to front
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    # setting PyQT5 backend
    try:
        matplotlib.use("qtagg")
    except:
        print("WARNING : COULD NOT SET QT BACKEND FOR MATPLOTLIB")

    # launching gui
    gui = VIPGUI(root)
    gui.launch()


# don't run on import because of shared QT backend instance
if __name__ == "__main__":
    main()
