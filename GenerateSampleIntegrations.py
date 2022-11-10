


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
    fileName = 'sampleIntegrations.txt'
    integrationCount = 10_000
    startTime = 0
    timeStepRange = (0.2,0.2)
    voltageRange = (0,3.5)    
    generateSampleIntegrations(fileName, integrationCount, startTime, timeStepRange, voltageRange)



if (__name__ == '__main__'):
    main()
