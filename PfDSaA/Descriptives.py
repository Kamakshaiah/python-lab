def Mean(x):
    ''' Calculates arithmetic mean '''
    return sum(x)/float(len(x))

def meanDict(x):
    ''' Calculates arithmetic mean
        Output:
            is a dictionary with three properties i.e.
            'num' for numerator
            'denom' for denominator
            'Average' for arithmetic mean '''
    num = sum(x)
    denom = len(x)
    aver = num/denom
    obj = {"numer": num, "denom": denom, "Average": aver}
    return(obj)

def geoMean(x):
    ''' calculates gemetric mean using loops '''
    p = 1
    for i in x:
        p *= i
        
    return(p**(1/len(x)))

def harMean(x):
    ''' Calculates harmonic mean.
        Input: Vector of numeric values
        Output:
            numer: length of input vector (x) 
            denom: sum of the reciprocals of the elements of the input vector (x) '''
    denom = []

    for i in x:
        denom.append(1/float(i))
    denom = sum(denom)
    numer = len(x)
    return(numer/denom)

def Median(x):
    ''' calculates median '''
    n = len(x) 
    x.sort() 
  
    if n % 2 == 0: 
        median1 = x[n//2] 
        median2 = x[n//2 - 1] 
        return((median1 + median2)/2)
    else: 
        median = x[n//2]
        return("Median is: " + str(median)) 

def Mode(x):
    ''' calculates mode '''
    from collections import Counter 
  
    n = len(x) 
  
    data = Counter(x) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
    if len(mode) == n: 
        get_mode = "No mode found"
        return(get_mode)
    else: 
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
        return(get_mode) 
      
def Var(x):
    ''' Computes variance for input vector (x) '''
    ss = sum([(i-Mean(x))**2 for i in x])
    return(float(ss)/(len(x) - 1))

def Std(x):
    ''' Computes standard deviation for input vector (x) '''
    return Var(x)**0.5

def Skewness(x):
    ''' Calculates sample skewness for input vector (x) '''
    numer = sum([(i-Mean(x)**3) for i in x])
    denom = sum([(i-Mean(x)**2)**float(3)/2 for i in x])
    return(numer/denom)

def Kurtosis(x):
    ''' Calculates the kurtosis for input vector (x) '''
    numer = sum([(i-Mean(x))**4 for i in x])
    numer = numer / len(x)
    denom = sum([((i-Mean(x))**2) for i in x])
    denom = (denom/len(x))**2
    return (numer/denom)

def CoVar(x, y):

    ''' Calculates covarince for input variables x and y '''

    covar = sum([(i - Mean(x))*(j - Mean(y)) for i, j in zip(x, y)])/(len(x)-1)
    return(covar) 

