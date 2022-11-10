




def main():
    
    import sys
    import matplotlib
    import numpy
    import pandas as pd



    filePath = ''


    dataFrame = pd.read_csv(sys.stdin, engine="pyarrow", header=None)
    columnCount = dataFrame.shape[1]


    










if (__name__ == '__main__'):
    main()