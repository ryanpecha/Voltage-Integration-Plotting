


def main():
    
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    import sys
    
    integrationsPath = 'sampleIntegrations.csv'
    scanCsvPath = 'sampleScanCSV.csv'

    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if (arg == '-iPath'):
            if (i + 1 == len(sys.argv)):
                print("'-iPath' WAS NOT GIVEN AN ARGUMENT")
                return
            integrationsPath = sys.argv[i + 1]
        if (arg == '-sPath'):
            if (i + 1 == len(sys.argv)):
                print("'-sPath' WAS NOT GIVEN AN ARGUMENT")
                return
            scanCsvPath = sys.argv[i + 1]



    if (not os.path.exists(integrationsPath)):
        print("NO SUCH FILE EXISTS:", integrationsPath)
        return
    
    if (not os.path.exists(scanCsvPath)):
        print("NO SUCH FILE EXISTS:", scanCsvPath)
        return



    print('PLOTTING:', integrationsPath)
    with open(integrationsPath, 'r') as openFile:
        integrationsDataFrame = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')
    
    print('PLOTTING:', scanCsvPath)
    with open(scanCsvPath, 'r') as openFile:
        integrationsDataFrame = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')



    # simData uses t=0, v=1
    timeStamps = integrationsDataFrame.iloc[:,11]    
    voltages = integrationsDataFrame.iloc[:,0]
    
    plt.plot(timeStamps,voltages)
    plt.title('Voltage Integrations')
    plt.xlabel(f'Time-Stamp SECONDS [ {timeStamps.min()} , {timeStamps.max()} ]')
    plt.ylabel(f'Voltage [ {voltages.min()} , {voltages.max()} ]')
    plt.show()



if (__name__ == '__main__'):
    main()
