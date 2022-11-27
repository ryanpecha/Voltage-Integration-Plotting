




def managePackages():

    # imports
    import subprocess
    import sys
    
    # checking versions
    print("CHECKING PYTHON PACKAGES")
    versionCheck = subprocess.run(['py', '-m', 'pip', 'list'], shell=True, capture_output=True)
    try :
        versionCheck.check_returncode()
        print("PASSED PIP PACKAGE LIST WITH RETURN CODE : ", versionCheck.returncode)
    except:
        print("FAILED PIP PACKAGE LSIT WITH RETURN CODE : ", versionCheck.returncode)
        print(versionCheck.stderr)
        return



    # cleaning current and target packages to format [ ("package","version") , ("package","version") , ... ] 
    currentPackageTable = [ package.split() for package in (str(versionCheck.stdout)).replace('\\r\\n',' \n').split('\n')[2:-1] ]    
    with open('requirements.txt', 'r') as Freqs:
        targetPackageTable = [ package.strip('\n').split('==') for package in Freqs.readlines() ]

    # package print debug
    #print('CURRENT : ')
    #[ print(package) for package in currentPackageTable ]
    #print('TARGET : ')
    #[ print(package) for package in targetPackageTable ]



    # checking for target packages
    for targetPackage in targetPackageTable:
        


        # checking for package of version
        if (targetPackage in currentPackageTable):
           # found matching version
           print(f'FOUND MATCHING PACKAGE "{targetPackage[0]}" OF TARGET VERSION {targetPackage[1]}')
           continue
        


        # checking for package of name and any version
        foundPackage = False
        for currentPackage in currentPackageTable:
            if (targetPackage[0] == currentPackage[0]):
                
                # found matching package of differing version
                foundPackage = True
                print(f'FOUND MATCHING PACKAGE "{targetPackage[0]}" OF DIFFERING VERSION | CURRENT : {currentPackage[1]} | TARGET : {targetPackage[1]}')

                # asking to install target version
                if (input(f'INSTALL "{targetPackage[0]}" VERSION {targetPackage[1]} (Y/N) ? : ').lower() != 'y'):
                    # user opted to not install matching version
                    print(f'PROCEEDING WITH "{targetPackage[0]}" VERSION {currentPackage[1]}')
                    break
                
                # uninstalling current version
                packageUnInstaller = subprocess.run(['py', '-m', 'pip', 'uninstall', targetPackage[0]], shell=True, stdout=sys.stdout)
                try :
                    packageUnInstaller.check_returncode()
                    print(f"PASSED {targetPackage[0]} TARGET VERSION {targetPackage[1]} UNINSTALL WITH RETURN CODE : ", packageUnInstaller.returncode)
                except:
                    print(f"FAILED {targetPackage[0]} TARGET VERSION {targetPackage[1]} UNINSTALL WITH RETURN CODE : ", packageUnInstaller.returncode)
                    print(packageUnInstaller.stderr)
                    return

                # installing target version
                packageInstaller = subprocess.run(['py', '-m', 'pip', 'install', targetPackage[0] + '==' + targetPackage[1]], shell=True, stdout=sys.stdout)
                try :
                    packageInstaller.check_returncode()
                    print(f"PASSED {targetPackage[0]} TARGET VERSION {targetPackage[1]} INSTALL WITH RETURN CODE : ", packageInstaller.returncode)
                except:
                    print(f"FAILED {targetPackage[0]} TARGET VERSION {targetPackage[1]} INSTALL WITH RETURN CODE : ", packageInstaller.returncode)
                    print(packageInstaller.stderr)
                    return
                
                # package has been installed with target version
                break
        


        # skip install if package exists
        if (foundPackage): continue
        

        
        # package does not exist
        print(f'COULD NOT LOCATE PACKAGE {targetPackage[0]}')

        # asking to install target version
        if (input(f'INSTALL "{targetPackage[0]}" VERSION {targetPackage[1]} (Y/N) ? : ').lower() != 'y'):
            # user opted to not install matching version
            print(f'ERROR, INSTALL DENIED FOR "{targetPackage[0]}" VERSION {targetPackage[1]}')
            break
        
        # installing missing package of target version
        packageInstaller = subprocess.run(['py', '-m', 'pip', 'install', targetPackage[0] + '==' + targetPackage[1]], shell=True, stdout=sys.stdout)
        try :
            packageInstaller.check_returncode()
            print(f"PASSED {targetPackage[0]} TARGET VERSION {targetPackage[1]} INSTALL WITH RETURN CODE : ", packageInstaller.returncode)
        except:
            print(f"FAILED {targetPackage[0]} TARGET VERSION {targetPackage[1]} INSTALL WITH RETURN CODE : ", packageInstaller.returncode)
            print(packageInstaller.stderr)
            return
        


    # all packages installed
    print('SUCCESS! ALL PACKAGES INSTALLED')





def main():

    # imports
    from PlotIntegrations import plot
    from tkinter.filedialog import askopenfilename
    from tkinter import Tk
    
    # bringing root to front
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    # asking user if they want auto package management
    if (input(f'AUTO MANAGE PACKAGES (Y/N) ? : ').lower() == 'y'):
        # user opted to auto manage packages
        managePackages()    
    
    # plotting data
    try:
        plot(
            iPath=askopenfilename(title='SELECT iPath',parent=root),
            aPath=askopenfilename(title='SELECT aPath',parent=root),
            iTimeStampIndex=int(input('ENTER iTimeStampIndex (INTEGER) (DEFAULT = 0) : ')),
            iVoltageIndex=int(input('ENTER iVoltageIndex (INTEGER) (DEFAULT = 1) : ')),
            iStartRowIndex=int(input('ENTER iStartRowIndex (INTEGER) (DEFAULT = 0) : ')),
            aStartRowIndex=int(input('ENTER aStartRowIndex (INTEGER) (DEFAULT = 0) : '))
        )
    except Exception as e:
        print('INVALID ARGUMENT')
        print(e)





# don't run on import
if (__name__ == '__main__'):
    main()
