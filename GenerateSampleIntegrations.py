
def main():

    import random
    
    integrationCount = 1_000_000
    fileName = 'sampleIntegrations.txt'
    startTime = 0

    timeStepRange = (0,0.25)
    voltageRange = (0,3.5)

    currentTime = startTime
    with open('./'+fileName,'w') as openFile:

        for i in range(integrationCount):
            currentTime += random.uniform(timeStepRange[0],timeStepRange[1])
            voltage = random.uniform(voltageRange[0],voltageRange[1])
            line = str(currentTime) + ',' + str(voltage) + '\n'
            #if (i != integrationCount - 1): line += '\n'
            openFile.write(line)
        
        openFile.close()


if (__name__ == '__main__'):
    main()
