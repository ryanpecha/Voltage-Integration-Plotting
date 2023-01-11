


def __selectFile__(fileUITitle,fileTypes,root):
    '''
        Allows the user to select a file via fileDialog UI.
        Bad files and escapes will return ""
    '''
    from tkinter.filedialog import askopenfilename
    # building combined set of all valid file formats
    allFileNames = ', '.join((fileType[0] for fileType in fileTypes))
    allFileTypes = ' '.join((fileType[1] for fileType in fileTypes))
    allFileType = (allFileNames,allFileTypes)
    fileTypes = (allFileType,) + fileTypes
    # polling user for file via fileDialog
    try:
        # file UI
        filePath = askopenfilename(title=fileUITitle,filetypes=fileTypes,root=root)
    except:
        # Simplifying bad selection to '' 
        return ''
    # Simplifying bad selection to '' 
    if filePath == None: return ''
    return filePath



def selectFile_runFile(root):
    '''
        Allows user to select the .run file containing all target ablations.
        This file specifies the shot locations for a given run.
        AKA ablations
        AKA targets
    '''
    fileUITitle = 'SELECT ".run" FILE WITH TARGET ABLATION COORDINATES'
    fileTypes = (('run files','*.run *.Run *.RUN'),('csv files','*.csv *.CSV'),('text files','*.txt'))
    return __selectFile__(fileUITitle,fileTypes)



def selectFile_scanFile(root):
    '''
        Allows user to select the .scancsv file containing all voltage integrations.
        This file specifies the voltage of the collector at a consistent time interval for a given run.
        AKA integrations
        AKA voltage
    '''
    fileUITitle = 'SELECT ".scancsv" FILE WITH VOLTAGE INTEGRATIONS'
    fileTypes = (('scancsv files','*.scancsv *.scanCSV *.Scancsv *.ScanCSV'),('csv files','*.csv *.CSV'),('text files','*.txt'))
    return __selectFile__(fileUITitle,fileTypes)
