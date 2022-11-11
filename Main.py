


def main():
    
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    import sys
    
    integrationsPath = 'sampleIntegrations.csv'
    dipPath = 'sampleScanCSV.csv'

    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if (arg == '-iPath'):
            if (i + 1 == len(sys.argv)):
                print("'-iPath' WAS NOT GIVEN AN ARGUMENT")
                return
            integrationsPath = sys.argv[i + 1]
        if (arg == '-dPath'):
            if (i + 1 == len(sys.argv)):
                print("'-dPath' WAS NOT GIVEN AN ARGUMENT")
                return
            dipPath = sys.argv[i + 1]



    if (not os.path.exists(integrationsPath)):
        print("NO SUCH FILE EXISTS:", integrationsPath)
        return
    
    if (not os.path.exists(dipPath)):
        print("NO SUCH FILE EXISTS:", dipPath)
        return



    print('PLOTTING:', integrationsPath)
    with open(integrationsPath, 'r') as openFile:
        integrationsDataFrame = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    
    print('PLOTTING:', dipPath)
    with open(dipPath, 'r') as openFile:
        dipsDataFrame = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')



    # simData uses t=0, v=1
    timeStamps = integrationsDataFrame.iloc[:,11]    
    voltages = integrationsDataFrame.iloc[:,0]
    dipVertices = dipsDataFrame.iloc[:,5]


    
    plt.plot(timeStamps,voltages)
    plt.title('Voltage Integrations')
    plt.xlabel(f'Time-Stamp SECONDS [ {timeStamps.min()} , {timeStamps.max()} ]')
    plt.ylabel(f'Voltage [ {voltages.min()} , {voltages.max()} ]')
    plt.show()



if (__name__ == '__main__'):
    main()
