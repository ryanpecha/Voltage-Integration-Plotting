
def main():
    '''
        
    '''
    
    # clearing console
    from os import system; system('cls||clear')
    # GUI instance
    from components.GUI import GUI
    GUI()



# don't run on import because of shared QT backend instance
if (__name__ == '__main__'):
    main()
