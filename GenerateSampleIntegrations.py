


def generateSampleIntegrations(fileName : str, integrationCount : int, startTime : float, timeStepRange : tuple, voltageRange : tuple) -> None:
    import random
    currentTime = startTime
    with open('./'+fileName,'w') as openFile:
        for _ in range(integrationCount):
            currentTime += random.uniform(timeStepRange[0],timeStepRange[1])
            voltage = random.uniform(voltageRange[0],voltageRange[1])
            line = str(currentTime) + ',' + str(voltage) + '\n'
            openFile.write(line)
        openFile.close()



def main():

    import sys
    
    filePath = 'sampleIntegrations.txt'
    
    integrationCount = 10_000
    
    startTime = 0
    
    timeStepMin = 0.2
    timeStepMax = 0.2
    
    voltageMin = 0
    voltageMax = 3.5
    
    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        
        if (arg == '-filePath'):
            filePath = sys.argv[i + 1]
        
        if (arg == '-integrationCount'):
            integrationCount = int(sys.argv[i + 1])
            
        if (arg == '-startTime'):
            startTime = float(sys.argv[i + 1])
        
        if (arg == '-timeStepMin'):
            timeStepMin = float(sys.argv[i + 1])
        
        if (arg == '-timeStepMax'):
            timeStepMax = float(sys.argv[i + 1])
        
        if (arg == '-voltageMin'):
            voltageMin = float(sys.argv[i + 1])
        
        if (arg == '-voltageMax'):
            voltageMax = float(sys.argv[i + 1])

    timeStepRange = (timeStepMin,timeStepMax)
    voltageRange = (voltageMin,voltageMax)    
    generateSampleIntegrations(filePath, integrationCount, startTime, timeStepRange, voltageRange)



if (__name__ == '__main__'):
    main()
