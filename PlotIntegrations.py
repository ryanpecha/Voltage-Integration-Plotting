


def main():
    
    # imports
    from matplotlib.widgets import Slider
    import matplotlib.pyplot as plt
    import pandas as pd
    import sys
    import os

    # setting PyQT5 backend
    try :
        import matplotlib
        matplotlib.use('qtagg')
    except :
        print("COULD NOT SET QT BACKEND")



    # defaults

    # integrations
    iPath = 'sampleIntegrations.csv'
    # ablations
    aPath = 'sampleAblations.csv'
    
    # 11
    i_timeStampIndex = 0
    # 0
    i_voltageIndex = 1
    # 5
    a_vertexIndex = 0

    # integrations file start row index
    iStartRowIndex = 0
    # ablations file start row index
    aStartRowIndex = 0



    # args

    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        
        if (arg == '-iPath'):
            iPath = sys.argv[i + 1]
        
        if (arg == '-aPath'):
            aPath = sys.argv[i + 1]
        
        if (arg == '-timeStampIndex'):
            i_timeStampIndex = int(sys.argv[i + 1])
        
        if (arg == '-voltageIndex'):
            i_voltageIndex = int(sys.argv[i + 1])
        
        if (arg == '-vertexIndex'):
            a_vertexIndex = int(sys.argv[i + 1])

        if (arg == '-iStartRowIndex'):
            iStartRowIndex = int(sys.argv[i + 1])

        if (arg == '-aStartRowIndex'):
            aStartRowIndex = int(sys.argv[i + 1])



    # path verification

    if (not os.path.exists(iPath)):
        print("NO SUCH INTEGRATIONS FILE EXISTS:", iPath)
        return
    
    if (not os.path.exists(aPath)):
        print("NO SUCH ABLATIONS FILE EXISTS:", aPath)
        return



    # csv to dataframe

    print('PLOTTING:', iPath)
    with open(iPath, 'r') as openFile:
        [ openFile.readline() for _ in range(iStartRowIndex) ]
        iDF = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    
    print('PLOTTING:', aPath)
    with open(aPath, 'r') as openFile:
        [ openFile.readline() for _ in range(aStartRowIndex) ]
        aDF = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    


    # dataframe to column/list
    i_timeStamps = iDF.iloc[:,i_timeStampIndex]
    i_voltages = iDF.iloc[:,i_voltageIndex]
    a_vertices = aDF.iloc[:,a_vertexIndex]

    # calculating the interval between integrations
    #integrationTimeStep = i_timeStamps[1] - i_timeStamps[0]
    
    # getting the expected number of ablation detections
    expectedAblationCount = a_vertices.size



    # plotting the primary integration data    

    fig, ax = plt.subplots()
    figShade = 0.75
    axShade = 0.85
    fig.set_facecolor((figShade,figShade,figShade))
    ax.set_facecolor((axShade,axShade,axShade))

    plt.plot(i_timeStamps,i_voltages, linewidth=1, label='Voltage')
    plt.subplots_adjust(bottom=0.2)
    plt.title('Ablations On Voltage-Integrations')
    plt.xlabel(f'Time-Stamp SECONDS [ {i_timeStamps.min()} , {i_timeStamps.max()} ]')
    plt.ylabel(f'Voltage V [ {i_voltages.min()} , {i_voltages.max()} ]')
    
    

    # initializing and drawing the floor line 
    initialFloor = 0.20
    floorX = [i_timeStamps.min(),i_timeStamps.max()]
    floorY = [initialFloor,initialFloor]
    floorLine, = plt.plot(floorX, floorY, color = 'purple', linewidth=1, linestyle='dashed', label=f'Floor : {initialFloor}')

    

    # initializing and drawing the ablation intersections
    plt.plot([],[],'o', color='black', markersize=0, label=f'Expected Ablations : {expectedAblationCount}')
    ablations, = plt.plot([], [], 'x', color='green', markersize=5, label='Detected Ablations : ')
    anomalies, = plt.plot([], [], 'x', color='purple', markersize=5, label='Detected Anomalies : ')
    errorsFlat, = plt.plot([], [], 'x', color='red', markersize=5, label='Detected Missing : ')
    errors, = plt.plot([], [], '+', color='red', markersize=5, label='Detected Miss Intersect')
    plt.plot([],[],'o', color='black', markersize=0, label=f'Unidentified : ')
    


    # plot text attributes
    alignments = ('top','bottom')
    shade1 = 0.00
    shade2 = 0.20
    colors = ((shade1,shade1,shade1),(shade2,shade2,shade2))
    styles = ('normal','italic')
    sizes = (7,8)

    # legend reference
    legend = plt.legend(facecolor=(figShade,figShade,figShade))

    # ablation set method with newest instance tracking
    class RefreshInstance: pass
    newestRefreshInstance = [None]
    def setAblations(floor, textList):
        
        # a newer refresh has been initiated
        myRefreshInstance = RefreshInstance()
        newestRefreshInstance[0] = myRefreshInstance

        # value initialization

        ablationsX = []
        ablationsY = []
        ablationTimeIndices = []

        anomaliesX = []
        anomaliesY = []
        
        errorsX = []
        errorsY = []
        errorsFlatY = []

        saddleSize = 0
        saddleIndex = 0
        
        # checking refreshInstance
        if (newestRefreshInstance[0] != myRefreshInstance): return

        # iterating over integrations
        for i in range(1,i_timeStamps.size - 1):

            # checking refreshInstance
            if (newestRefreshInstance[0] != myRefreshInstance): return

            # grabbing current voltage
            voltage = i_voltages[i]
            
            # ignoring above the floor
            if (voltage > floor):
                continue
            
            # voltage decreased, shifting the saddle right
            if (i_voltages[i - 1] > voltage):
                saddleIndex = i
            
            # increased beyond floor, adding the saddle
            if (i_voltages[i + 1] > floor):
                if (saddleSize == 0):
                    anomaliesX.append(i_timeStamps[saddleIndex])
                    anomaliesY.append(i_voltages[saddleIndex])
                else:
                    ablationsX.append(i_timeStamps[saddleIndex])
                    ablationsY.append(i_voltages[saddleIndex])
                    ablationTimeIndices.append(saddleIndex)
                # resetting saddle size
                saddleSize = 0
            
            # our saddle has grown
            else:
                saddleSize += 1

        # checking refreshInstance
        if (newestRefreshInstance[0] != myRefreshInstance): return

        # updating plot
        
        ablations.set_xdata(ablationsX)
        ablations.set_ydata(ablationsY)

        anomalies.set_xdata(anomaliesX)
        anomalies.set_ydata(anomaliesY)            

        # checking refreshInstance
        if (newestRefreshInstance[0] != myRefreshInstance): return

        # cannot locate missing ablations with only one detected ablation
        if (len(ablationsX) > 1):

            #ablationTimeStepAverage = (ablationsX[-1] - ablationsX[0]) / (len(ablationsX) - 1)
            # calculating mode and allowable step
            timeSteps = {}
            for i in range(len(ablationsX) - 1):
                curTime = ablationsX[i]
                nextTime = ablationsX[i + 1]
                timeStep = nextTime - curTime
                if timeStep in timeSteps:
                    timeSteps[timeStep] += 1
                else:
                     timeSteps[timeStep] = 1
            curAvgFreq = 0
            ablationTimeStepMode = 0
            for timeStep in timeSteps:
                if (timeSteps[timeStep] > curAvgFreq):
                    curAvgFreq = timeSteps[timeStep]
                    ablationTimeStepMode = timeStep                

            allowableTimeStep = ablationTimeStepMode * 1.5
            averageAblationY = 0
            for y in ablationsY:
                averageAblationY += y
            averageAblationY /= len(ablationsY)

            # calculating missing ablations
            for i in range(0, len(ablationsX) - 1):

                # checking refreshInstance
                if (newestRefreshInstance[0] != myRefreshInstance): return

                # grabbing current values from detected ablations
                curTime = ablationsX[i]
                nextTime = ablationsX[i + 1]
                distance = nextTime - curTime
                
                # identifying errors following from current ablation
                if (distance > allowableTimeStep):
                    missCount = int(distance / ablationTimeStepMode)
                    timeIndex = ablationTimeIndices[i]
                    
                    # building errors following current ablation
                    for m in range(1,missCount+1):
                        
                        # adding error x
                        errorTime = curTime + (ablationTimeStepMode * m)
                        errorsX.append(errorTime)
                        
                        # calculating actual error y value on plot
                        while (i_timeStamps[timeIndex + 1] < errorTime):
                            timeIndex += 1
                        x1 = i_timeStamps[timeIndex]
                        x2 = i_timeStamps[timeIndex + 1]
                        y1 = i_voltages[timeIndex]
                        y2 = i_voltages[timeIndex + 1]
                        slope = (y2-y1) / (x2-x1)
                        y = (slope * (errorTime - x1)) + y1
                        
                        # adding error y
                        errorsY.append(y)
                        errorsFlatY.append(averageAblationY)

        # checking refreshInstance
        if (newestRefreshInstance[0] != myRefreshInstance): return

        # updating errors / missing ablations on plot
        errors.set_xdata(errorsX)
        errors.set_ydata(errorsY)
        errorsFlat.set_xdata(errorsX)
        errorsFlat.set_ydata(errorsFlatY)

        # checking refreshInstance
        if (newestRefreshInstance[0] != myRefreshInstance): return

        # generating coordinate index text
        
        [indexText.remove() for indexText in textList]
        textList.clear()
        allX = sorted(ablationsX + errorsX)

        # checking refreshInstance
        if (newestRefreshInstance[0] != myRefreshInstance): return

        # ablations
        for i in range(len(ablationsX)):
            x = ablationsX[i]
            y = ablationsY[i]
            globalIndex = allX.index(x)
            textList.append(
                plt.text(
                    x = x,
                    y = y,
                    s = str(globalIndex),
                    fontsize = sizes[ (globalIndex % 4) > 1 ],
                    color = colors[ (globalIndex % 4) > 1 ],
                    verticalalignment = alignments[globalIndex % 2],
                    fontfamily = 'monospace',
                    fontstyle = styles[ (globalIndex % 4) > 1 ],
                    alpha=0.75
                )
            )
        
        # errors / missing
        for i in range(len(errorsX)):
            x = errorsX[i]
            y = errorsFlatY[i]
            globalIndex = allX.index(x)
            textList.append(
                plt.text(
                    x = x,
                    y = y,
                    s = str(globalIndex),
                    fontsize = sizes[ (globalIndex % 4) > 1 ],
                    color = colors[ (globalIndex % 4) > 1 ],
                    verticalalignment = alignments[globalIndex % 2],
                    fontfamily = 'monospace',
                    fontstyle = styles[ (globalIndex % 4) > 1 ],
                    alpha=0.75
                )
            )

        # unkown trailing / preceding missing ablations
        extraneousMissingCount = expectedAblationCount - len(errorsX) - len(ablationsX)
        print("ABLATIONS > DETECTED:", len(ablationsX), "| EXPECTED:", expectedAblationCount, "| MISSING LOCATED:", len(errorsX), "| UNIDENTIFIED EXTRANEOUS:", extraneousMissingCount)
        if (extraneousMissingCount > 0):
            print(f"WARNING > {extraneousMissingCount} UNIDENTIFIABLE ABLATIONS")
        if (extraneousMissingCount < 0):
            print(f"WARNING > {abs(extraneousMissingCount)} MORE DETECTIONS THAN EXPECTED ABLATIONS")
        
        # unidentified point labeling
        if (extraneousMissingCount > 0):
            x = allX[-1] + (ablationTimeStepMode * 8)
            y = averageAblationY
            textList.append(
                plt.text(
                    x = x,
                    y = y,
                    s = f'{extraneousMissingCount} UNIDENTIFIED',
                    fontsize = 8,
                    color = 'red',
                    verticalalignment = 'bottom',
                    fontfamily = 'monospace',
                    fontstyle = 'normal',
                    alpha=1
                )
            )
        
        # updating the value fields of the legend
        legend.get_texts()[-5].set_text(f'Detected Ablations : {len(ablationsX)}')
        legend.get_texts()[-4].set_text(f'Detected Anomalies : {len(anomaliesX)}')
        legend.get_texts()[-3].set_text(f'Detected Missing : {len(errorsX)}')
        legend.get_texts()[-1].set_text(f'Unidentified : {extraneousMissingCount}')
        legend.get_texts()[1].set_text(f'Floor : {round(floor,3)}')



    # initial ablation set
    setAblations(initialFloor, [])


    # axis for positioning the floor slider
    left = 0.125
    bottom = 0.025
    width = 0.775
    height = 0.1
    floorAxis = plt.axes([left, bottom, width, height])

    # floor slider
    floorIncrement = 0.001
    minFloor = i_voltages.min() - floorIncrement
    maxFloor = i_voltages.max() + floorIncrement
    floorSlider = Slider(ax=floorAxis, label='Floor', valmin=minFloor, valmax=maxFloor, valinit=initialFloor, valstep=floorIncrement, track_color=(axShade,axShade,axShade))
    
    # plot updating
    plotText = []
    def updateFloor(val):
        # drawing the floor and ablations
        floorLine.set_ydata([val,val])
        setAblations(floor=val, textList=plotText)
    floorSlider.on_changed(updateFloor)

    

    # draw
    plt.show()





# don't run on import
if (__name__ == '__main__'):
    main()
