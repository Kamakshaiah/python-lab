def myVar(x):
    ''' calculates variance '''
    
    ss = sum([(i-myMean(x))**2 for i in x])
    return float(ss)/(len(x) - 1)

def myStd(x):
    ''' calculates standard deviation '''
    return myVar(x)**0.5
