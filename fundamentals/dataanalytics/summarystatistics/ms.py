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
