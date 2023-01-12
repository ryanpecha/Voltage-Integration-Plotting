
from components.Theme import *
class GUI():
    '''
        Single GU
    '''
    

    def __init__(self,theme:Theme=THEME_dark) -> None:
        '''

        '''
        
        #
        from components import FileSelect as FS
        #
        self.path_voltage = None
        self.path_targets = None
        #self.root = 

        self.__setTkRootAtFront__()
        self.__trySetQTBackend__()
        self.__setTheme__(theme)

        
    


    def __setTheme__(self,theme:Theme):
        pass



    def __setTkRootAtFront__(self):
        '''
            bringing root to front
        '''
        from tkinter import Tk
        self.root = Tk()
        self.root.attributes("-topmost", True)
        self.root.withdraw()



    def __trySetQTBackend__(self):
        '''
            Setting PyQT5 backend.
            Defaults to tkinter on error.
        '''
        try :
            import matplotlib
            matplotlib.use('qtagg')
        except :
            print("WARNING, COULD NOT SET QT BACKEND")
