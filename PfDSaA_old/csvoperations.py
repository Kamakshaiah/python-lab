# chapter 2

def readCSV(p):

    ''' return data vectors from CSV file '''
    import csv
    gen = []
    path = p
    
    reader = csv.reader(open(path, 'rU'))
    for r in reader:
        gen.append(r[0])
        print(gen[-1])
           

def writeCSV(p, data):

    ''' this program writes data to CSV file at given path disk \n
        the data set should be a list saved using name 'data' '''
    
    import csv

    data = [['first', 'second', 'third'],
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    path = p
    
    file = open(path, 'w')
    with file:
        wr = csv.writer(file)
        wr.writerows(data)

##    if data==dummy:
##        data = [['first', 'second', 'third'],
##                [1, 2, 3],
##                [4, 5, 6],
##                [7, 8, 9]]
##
##        path = 'p'
##        file = open(path, 'w')
##        with file:
##            wr = csv.writer(file)
##            wr.writerows(data)
##    else:
##        path = 'p'
##        file = open(path, 'w')
##        with file:
##            wr = csv.writer(file)
##            wr.writerows(data)
##        

