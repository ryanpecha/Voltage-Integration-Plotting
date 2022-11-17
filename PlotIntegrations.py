


def main():
    
    from matplotlib.widgets import Slider, Button
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
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
        
        if (arg == '-verticesIndex'):
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
    title = 'Ablations On Voltage-Integrations'
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    plt.plot(i_timeStamps,i_voltages)
    plt.title(title)
    plt.xlabel(f'Time-Stamp SECONDS [ {i_timeStamps.min()} , {i_timeStamps.max()} ]')
    plt.ylabel(f'Voltage [ {i_voltages.min()} , {i_voltages.max()} ]')

    
    
    # calculating the interval between integrations
    #timeStep = i_timeStamps[1] - i_timeStamps[0]

    # initializing and drawing the floor line 
    initialFloor = 0.10
    floorX = [i_timeStamps.min(),i_timeStamps.max()]
    floorY = [initialFloor,initialFloor]
    floorLine, = plt.plot(floorX, floorY)

    # initializing and drawing the ablation intersections
    



    # axis for positioning the floor slider
    left = 0.125
    bottom = 0.025
    width = 0.775
    height = 0.1
    floorAxis = plt.axes([left, bottom, width, height])

    # floor slider
    minFloor = i_voltages.min()
    maxFloor = i_voltages.max()
    floorIncrement = 0.001
    floorSlider = Slider(ax=floorAxis, label='Floor', valmin=minFloor, valmax=maxFloor, valinit=initialFloor, valstep=floorIncrement)
    def updateFloor(val):
        floorLine.set_ydata([val,val])
    floorSlider.on_changed(updateFloor)



    # draw
    plt.show()





# don't run on import
if (__name__ == '__main__'):
    main()
