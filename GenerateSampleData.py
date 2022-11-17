




def main():



    import sys
    import random
    


    # defaults

    # integrations
    iPath = 'sampleIntegrations.csv'
    # ablations
    aPath = 'sampleAblations.csv'

    startTime = 0

    integrationCount = 10_000
    timeStep = 0.2
    
    voltageMin = 0
    voltageMax = 3.5
    voltageStepMax = 0.1
    


    # args

    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        
        if (arg == '-iPath'):
            iPath = sys.argv[i + 1]
        
        if (arg == '-aPath'):
            aPath = sys.argv[i + 1]
            
        if (arg == '-startTime'):
            startTime = float(sys.argv[i + 1])
        
        if (arg == '-integrationCount'):
            integrationCount = int(sys.argv[i + 1])

        if (arg == '-timeStep'):
            timeStep = int(sys.argv[i + 1])
        
        if (arg == '-voltageMin'):
            voltageMin = float(sys.argv[i + 1])
        
        if (arg == '-voltageMax'):
            voltageMax = float(sys.argv[i + 1])

        if (arg == '-voltageStepMax'):
            voltageStepMax = float(sys.argv[i + 1])


    
    # generation loop

    currentTime = startTime
    currentVoltage = random.uniform(voltageMin,voltageMax)
    with open(iPath,'w') as iFile:

        for _ in range(integrationCount):

            # stepping the voltage in range
            voltageStep = random.uniform(-voltageStepMax,voltageStepMax)
            if (currentVoltage + voltageStep > voltageMax):
                currentVoltage -= voltageStep
            elif (currentVoltage + voltageStep < voltageMin):
                currentVoltage += voltageStep
            else:
                currentVoltage += voltageStep

            # clamping voltage
            currentVoltage = max(voltageMin, currentVoltage)
            currentVoltage = min(voltageMax, currentVoltage)
            
            # writing to file
            line = str(currentTime) + ',' + str(currentVoltage) + '\n'
            iFile.write(line)

            # incrementing time
            currentTime += timeStep
        
        iFile.close()





# don't run on import
if (__name__ == '__main__'):
    main()
