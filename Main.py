


def main():
    
    import matplotlib.pyplot as plt
    import pandas as pd
    import os

    filePath = 'sampleIntegrations.txt'
    if (not os.path.exists(filePath)): 
        import GenerateSampleIntegrations as GSI
        GSI.main()
    
    with open(filePath, 'r') as openFile:
        dataFrame = pd.read_csv(openFile, engine="pyarrow", header=None, delimiter=',', )

    timeStamps = dataFrame.iloc[:,0]    
    voltages = dataFrame.iloc[:,1]
    plt.plot(timeStamps,voltages)

    plt.title('Voltage Integrations')
    plt.xlabel(f'Time-Stamp SECONDS [ {timeStamps.min()} , {timeStamps.max()} ]')
    plt.ylabel(f'Voltage [ {voltages.min()} , {voltages.max()} ]')
    plt.show()



if (__name__ == '__main__'):
    main()