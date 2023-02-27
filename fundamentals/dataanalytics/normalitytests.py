# normality tests

def myMean(x):
    return sum(x)/float(len(x))

def myVar(x):
    ss = sum([(i-myMean(x))**2 for i in x])
    return float(ss)/(len(x) - 1)

def myStd(x):
    return myVar(x)**0.5

def skewness(x):
    numer = sum([(i-myMean(x)**3) for i in x])
    denom = sum([(i-myMean(x)**2)**float(3)/2 for i in x])
    return numer/denom

def kurtosis(x):
    numer = sum([(i-myMean(x))**4 for i in x])
    numer = numer / len(x)
    denom = sum([((i-myMean(x))**2) for i in x])
    denom = (denom/len(x))**2
    return (numer/denom)-3

def DATest(x):

    ''' return D Augustino's Normality test '''

    import math

    g1 = skewness(x)
    g2 = kurtosis(x)

    n = len(x)
    
    m1_g1 = 0
    m2_g1 = (6*(n-2)/((n+1)*(n+3)))
    m3_g1 = (6*(n-3)/((n+1)*(n+2)*(n+4)))
    m4_g1 = (6*(n-4)/((n+1)*(n+2)*(n+3)*(n+5)))

    g1_g1 = 0
    g2_g1 = (m4_g1/(m2_g1**2)) - 3

    m1_g2 = (6/(n+1))
    m2_g2 = (24*n*(n-2)*(n-3))/(((n+1)**2)*(n+3)*(n+5))

    g1_g2 = (6*(n**2)-5*n+2)/((n+7)*(n+9))*((6*(n+3)*(n+5))/(n*(n-2)*(n-3)))**0.5
    g2_g2 = ((36*((15*(n**6))-(36*(n**5))-(628*(n**4))-982*(n**3) \
                  - 5777*(n**2) - 640*(n) + 900)/(n*(n-3)*(n-2)*(n+7)*(n+9)*(n+11)*(n+13))))

    Wsq = (2*(g2_g1+4))**0.5 - 1
    W = Wsq **0.5
    delta = 1/math.log(W, 2)
    alphasq = 2/(Wsq-1)
    alpha = alphasq**0.5
    # the below statement is added by me correction required
    alpha = abs(alpha) 

    z1_g1 = math.asinh(g1/(alpha*(m2_g1)**0.5))

    return(z1_g1)

def ADTest(x):

    ''' this function return anderson darling test '''

    
