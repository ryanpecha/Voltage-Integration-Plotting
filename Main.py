


def main():
    
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    import sys
    
    filePath = 'sampleIntegrations.txt'

    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if (arg == '-filePath'):
            if (i + 1 == len(sys.argv)):
                print("'-filePath' WAS NOT GIVEN AN ARGUMENT")
                return
            filePath = sys.argv[i + 1]

    if (not os.path.exists(filePath)):
        print("NO SUCH FILE EXISTS:", filePath)
        return
    
    print('PLOTTING:', filePath)

    with open(filePath, 'r') as openFile:
        dataFrame = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',')

    timeStamps = dataFrame.iloc[:,0]    
    voltages = dataFrame.iloc[:,1]
    plt.plot(timeStamps,voltages)

    plt.title('Voltage Integrations')
    plt.xlabel(f'Time-Stamp SECONDS [ {timeStamps.min()} , {timeStamps.max()} ]')
    plt.ylabel(f'Voltage [ {voltages.min()} , {voltages.max()} ]')
    plt.show()



if (__name__ == '__main__'):
    main()
