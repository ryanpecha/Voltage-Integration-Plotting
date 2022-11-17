


def main():
    
    from matplotlib.widgets import Slider, Button
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    import sys
    


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



    if (not os.path.exists(iPath)):
        print("NO SUCH INTEGRATIONS FILE EXISTS:", iPath)
        return
    
    if (not os.path.exists(aPath)):
        print("NO SUCH ABLATIONS FILE EXISTS:", aPath)
        return



    print('PLOTTING:', iPath)
    with open(iPath, 'r') as openFile:
        iDF = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    
    
    print('PLOTTING:', aPath)
    with open(aPath, 'r') as openFile:
        aDF = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    


    i_timeStamps = iDF.iloc[:,i_timeStampIndex]
    i_voltages = iDF.iloc[:,i_voltageIndex]
    a_vertices = aDF.iloc[:,a_vertexIndex]


    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.175)
    
    plt.plot(i_timeStamps,i_voltages)
    plt.title('Voltage Integrations')
    plt.xlabel(f'Time-Stamp SECONDS [ {i_timeStamps.min()} , {i_timeStamps.max()} ]')
    plt.ylabel(f'Voltage [ {i_voltages.min()} , {i_voltages.max()} ]')



    left = 0.125
    bottom = 0.025
    width = 0.75
    height = 0.05
    floorAxis = plt.axes([left, bottom, width, height])

    initialFloor = 1
    minFloor = i_voltages.min()
    maxFloor = i_timeStamps.max()
    floorIncrement = 0.01
    floorSlider = Slider(ax=floorAxis, label='Floor', valmin=minFloor, valmax=maxFloor, valinit=initialFloor, valstep=floorIncrement)

    def updateFloor(val):
        print('NEW FLOOR :', val)

    floorSlider.on_changed(updateFloor)



    plt.show(block=True)





if (__name__ == '__main__'):
    main()
