


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
        iDF = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    
    print('PLOTTING:', aPath)
    with open(aPath, 'r') as openFile:
        aDF = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    


    # dataframe to column/list
    i_timeStamps = iDF.iloc[:,i_timeStampIndex]
    i_voltages = iDF.iloc[:,i_voltageIndex]
    a_vertices = aDF.iloc[:,a_vertexIndex]

    # calculating the interval between integrations
    integrationTimeStep = i_timeStamps[1] - i_timeStamps[0]
    
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
    plt.ylabel(f'Voltage [ {i_voltages.min()} , {i_voltages.max()} ]')
    
    

    # initializing and drawing the floor line 
    initialFloor = 0.20
    floorX = [i_timeStamps.min(),i_timeStamps.max()]
    floorY = [initialFloor,initialFloor]
    floorLine, = plt.plot(floorX, floorY, color = 'purple', linewidth=1, linestyle='dashed', label='Floor')

    

    # initializing and drawing the ablation intersections
    ablations, = plt.plot([], [], 'x', color='green', markersize=5, label='Ablations')
    anomalies, = plt.plot([], [], 'x', color='purple', markersize=5, label='Anomalies')
    errorsFlat, = plt.plot([], [], 'x', color='red', markersize=5, label='Missing')
    errors, = plt.plot([], [], '+', color='red', markersize=5, label='Miss Intersect')

    # ablation set method
    def setAblations(floor):

        saddles = []

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
        
        # iterating over integrations
        for i in range(1,i_timeStamps.size - 1):
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
                # getting index range of this saddle
                saddles.append( (saddleIndex - saddleSize , saddleIndex) )
                # resetting saddle size
                saddleSize = 0
            
            # our saddle has grown
            else:
                saddleSize += 1
        
        # updating plot
        
        ablations.set_xdata(ablationsX)
        ablations.set_ydata(ablationsY)

        anomalies.set_xdata(anomaliesX)
        anomalies.set_ydata(anomaliesY)            

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

            allowableTimeStep = ablationTimeStepMode * 1.25
            averageAblationY = 0
            for y in ablationsY:
                averageAblationY += y
            averageAblationY /= len(ablationsY)

            # calculating missing ablations
            for i in range(0, len(ablationsX) - 1):
                curTime = ablationsX[i]
                nextTime = ablationsX[i + 1]
                distance = nextTime - curTime
                
                # idnetifying errors following from current ablation
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

        # updating errors / missing ablations on plot
        errors.set_xdata(errorsX)
        errors.set_ydata(errorsY)
        errorsFlat.set_xdata(errorsX)
        errorsFlat.set_ydata(errorsFlatY)

        # unkown trailing / preceding missing ablations
        extraneousMissingCount = expectedAblationCount - len(errorsX) - len(ablationsX)
        print("ABLATIONS > DETECTED:", len(ablationsX), "| EXPECTED:", expectedAblationCount, "| MISSING LOCATED:", len(errorsX), "| MISSING EXTRANEOUS:", extraneousMissingCount)
        if (extraneousMissingCount > 0):
            print(f"WARNING > {extraneousMissingCount} UNIDENTIFIABLE ABLATIONS")
        if (extraneousMissingCount < 0):
            print(f"WARNING > {abs(extraneousMissingCount)} MORE DETECTIONS THAN EXPECTED")
        


    # initial ablation set
    setAblations(initialFloor)



    plt.legend(facecolor=(figShade,figShade,figShade))



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
    def updateFloor(val):
        # drawing the floor and ablations
        floorLine.set_ydata([val,val])
        setAblations(val)
    floorSlider.on_changed(updateFloor)

    

    # draw
    plt.show()





# don't run on import
if (__name__ == '__main__'):
    main()
