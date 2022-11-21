
def main():

    from PlotIntegrations import plot
    from tkinter.filedialog import askopenfilename
    
    plot(
        iPath=askopenfilename(title='SELECT iPath'),
        aPath=askopenfilename(title='SELECT aPath'),
        iTimeStampIndex=int(input('ENTER iTimeStampIndex (INTEGER) (DEFAULT = 0) : ')),
        iVoltageIndex=int(input('ENTER iVoltageIndex (INTEGER) (DEFAULT = 1) : ')),
        iStartRowIndex=int(input('ENTER iStartRowIndex (INTEGER) (DEFAULT = 0) : ')),
        aStartRowIndex=int(input('ENTER aStartRowIndex (INTEGER) (DEFAULT = 0) : '))
    )

if (__name__ == '__main__'):
    main()
