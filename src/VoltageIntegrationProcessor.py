import os
import sys
import platform
import pandas as pd
import win32.win32gui
import win32.lib.win32con
from CVIPGUI import VIPGUI
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def main():
    
    # hiding terminal if flag present
    if ("--hideTerminal" in sys.argv):
        # only supported for windows
        if (platform.system() == "windows"):
            fgID:int = win32.win32gui.GetForegroundWindow()
            win32.win32gui.ShowWindow(fgID , win32.lib.win32con.SW_HIDE)
    
    # launching gui
    gui = VIPGUI()
    gui.launch()


if __name__ == "__main__":
    main()
