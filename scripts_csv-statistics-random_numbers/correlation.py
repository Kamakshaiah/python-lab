# correlation

def correl(x, y):

    xdev = [(i - myMean(x)) for i in x]
    ydev = [(i - myMean(y)) for i in y]

    sdev = []

    for i in range(len(xdev)):
        sdev.append(xdev[i]*ydev[i])

    numer = sum(sdev)

    dnom1 = [(i-myMean(x))**2 for i in x]
    dnom2 = [(i-myMean(y))**2 for i in y]

    dnom1 = sum(dnom1)**0.5
    dnom2 = sum(dnom2)**0.5

    denom = dnom1 * dnom2

    stat = numer/denom

    return stat
    
# def cortest(): 
