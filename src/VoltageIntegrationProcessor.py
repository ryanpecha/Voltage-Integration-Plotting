def main():
    """VIP Program Launcher"""

    import os
    import sys
    import matplotlib
    import win32.win32gui
    from tkinter import Tk
    import win32.lib.win32con
    from components.CVIPGUI import VIPGUI
    from components.CRunData import RunData
    from components.CTargetData import TargetData

    # hide running terminal
    if "--hideTerminal" in sys.argv:
        sys.argv.remove("--hideTerminal")
        fgID: int = win32.win32gui.GetForegroundWindow()
        win32.win32gui.ShowWindow(fgID, win32.lib.win32con.SW_HIDE)

    # bringing root to front and get ref for file dialogs
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    # setting PyQT5 backend, default is tkinter
    try:
        matplotlib.use("qtagg")
    except:
        print("WARNING : COULD NOT SET QT BACKEND FOR MATPLOTLIB")

    # setup and launch matplotlib gui
    gui = VIPGUI(root)
    if len(sys.argv) > 1:
        fpath = sys.argv[1]
        if not os.path.exists(fpath):
            pass
        if os.path.isdir(fpath):
            pass
        elif RunData.isValidFile(fpath):
            gui.setRunFile(fpath)
        elif TargetData.isValidFile(fpath):
            gui.setTargetFile(fpath)
    gui.launch()


# don't run on import because of shared QT backend instance
if __name__ == "__main__":
    main()
