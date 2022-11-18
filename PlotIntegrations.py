


def main():
    
    from matplotlib.widgets import Slider, Button
    import matplotlib.pyplot as plt
    import pandas as pd
    import sys
    import os



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
    
    
    
    # calculating the interval between integrations
    #timeStep = i_timeStamps[1] - i_timeStamps[0]

    # initializing and drawing the floor line 
    initialFloor = 0.20
    floorX = [i_timeStamps.min(),i_timeStamps.max()]
    floorY = [initialFloor,initialFloor]
    floorLine, = plt.plot(floorX, floorY, color = 'purple', linewidth=1, linestyle='dashed', label='Floor')

    

    # initializing and drawing the ablation intersections
    ablations, = plt.plot([], [], 'x', color='green', markersize=5, label='Ablations')
    anomalies, = plt.plot([], [], 'x', color='purple', markersize=10, label='Anomalies')
    def setAblations(floor):

        ablationsX = []
        ablationsY = []
        
        anomaliesX = []
        anomaliesY = []
        
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
                saddleSize = 0
            
            # our saddle has grown
            else:
                saddleSize += 1
        
        # updating plot
        
        ablations.set_xdata(ablationsX)
        ablations.set_ydata(ablationsY)

        anomalies.set_xdata(anomaliesX)
        anomalies.set_ydata(anomaliesY)
        


    # initial ablation set
    setAblations(initialFloor)



    errors, = plt.plot([], [], 'x', color='red', markersize=10, label='Missing')

    # need most common interval
    # need an average interval
    # need an allowable interval range

    # TODO add toggle button for include anomalies within ablations 
    # TODO error checking based on integration intervals
    # TODO slider reset buttons
    # TODO add Voltge units



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


