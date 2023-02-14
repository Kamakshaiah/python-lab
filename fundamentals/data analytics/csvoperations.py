# chapter 2

def readCSV(p):

    ''' return data vectors from CSV file. Return Numpy array object. The first array will be the header. '''
    import csv
    import numpy as np
    
    path = p
    out = []
    reader = csv.reader(open(path, 'r'))
    for r in reader:
        out.append(r)
        
    return np.array(out)
           
def makeDataFrame(data):
    ''' Creates data frame from numpy data array. First row in the numpy array is used for column names '''
    import pandas as pd
    import numpy as np
    
    df = pd.DataFrame(np.delete(data, 0, 0), columns = data[0, ])
    return df


def writeCSV(p, data):

    ''' This program writes data to CSV file at given path disk. The data set should be Numpy data array '''
    
    import csv
    path = p
    
    file = open(path, 'w')
    with file:
        wr = csv.writer(file)
        wr.writerows(data)

def writeDataFrame(path, df):
    ''' Writes Pandas data frame object to CSV file. @path: windows path variable. @df: pandas data frame.'''
    
    import os
    import datetime
    
    path = str(path) + '\\' 
    path = os.path.join(path, str(datetime.date.today()) +  '-' + str(datetime.datetime.now().strftime('%H-%M-%S')) + '.csv')
    
    df.to_csv(path)