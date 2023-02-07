# simulations

def simNumVec(n):

    ''' Creates a vector of random numbers as by user input 'n' '''
    
    import random

    x = []
    for i in range(n):
        x.append(round(random.random()*100))
    return(x)

def simNumVecDecimals(n):
    ''' Creates data vector with a start value 1 to upper limit l for length n '''
    import random as rnd
    data = [round(rnd.random(), 2) for i in range(n)]
    return(data)

def simNumVecBetween(n, a, b):
    ''' Creates n number of data points with starting value 'a' and ending value 'b' '''
    import random as rnd
    data = [rnd.randint(a, b) for i in range(n)]
    return(data) 

def simBiVarData(n):
    ''' Creates a dictionary with two variables namely 'x' and 'y' for input 'n' '''
    
    import random

    x = []
    for i in range(n):
	      x.append(round(random.random()*100))
    y = []
    for i in range(n):
	      y.append(round(random.random()*100))

    return({'x': x, 'y': y})

def simDictData(names):

    ''' Creates a dictionary of keys from input names and valus from input lenght n '''

    data = dict(zip(names, simNumVec(len(names))))

    return(data) 

def simDictDataFromArrays(n, names, decimals = False):

    ''' Creates a multivariate data set with length 'n' for given list of names '''

    if decimals == False:
        data = dict.fromkeys(names, simNumVec(n))
        return(data) 
    if decimals == True:
        data = dict.fromkeys(names, simNumVecDecimals(n))
        return(data) 

def simCatDataDict(n, name, res):
    ''' Creates a vector of size n for categories mentioned in args '''
    import random as rnd
    name = name
    data = rnd.choices(res, k = n)
    return({name: data})

def simCatData(n, res):
    ''' Creates categorical data based on arguments for value 'n' '''
    import random as rnd 

    res = res * n
    res = res
    rnd.shuffle(res, rnd.random)
    return(res[0:n]) 

def simHetDat(n, r):
    ''' A function to create heterogeneous data variables such as 'gender', 'occupation', 'marital status'.
        The responses are as follows:
        all: creates a data frame with following responses
	gender: 'male', 'female'
	occupation: 'employed', 'unemployed'
	marital status: 'married', 'unmarried'
        '''
    import random
    import pandas as pd

    m = n//2

    g1 = ['male', 'female']
    g1 = g1 * m
    random.shuffle(g1, random.random)

    g2 = ['employed', 'unemployed']
    g2 = g2 * m
    random.shuffle(g2, random.random)

    g3 = ['married', 'unmarried']
    g3 = g3 * m
    random.shuffle(g3, random.random)

    x = []

    for i in range(n):
        x.append(round(random.random()*100))

    if (r == 'all'):
        dat = pd.DataFrame({'gen':g1, 'occ':g2, 'ms':g3, 'numeric':x})
        return(dat)

    elif (r == "gender"):
        dat = pd.DataFrame({'gen':g1, 'numeric':x})
        return(dat)

    elif (r == "occupation"):
        dat = pd.DataFrame({'occ':g2, 'numeric':x})
        return(dat)

    elif (r == "marital status"):
        dat = pd.DataFrame({'ms':g3, 'numeric':x})
        return(dat)

    else:
        print('response is missing')
        raise SystemExit

def simDataSetFromDict(d):

    ''' Crates a fully qualified data set for input data dictionary d '''
    import pandas as pd
    
    data = pd.DataFrame(d)
    return(data)
