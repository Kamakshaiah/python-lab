def Mean(x):
    ''' Calculates arithmetic mean '''
    return sum(x)/float(len(x))

def simRandVector(n):

    ''' this function is useful for simulating a random numeric vector using 'n' values '''

    import random as rd
    x = list(rd.randint(0, 5)*n for i in range(n))

    return(x)

def rankify(A):
 
    # Rank Vector
    R = [0 for x in range(len(A))]
 
    # Sweep through all elements
    # in A for each element count
    # the number of less than and 
    # equal elements separately
    # in r and s.
    for i in range(len(A)):
        (r, s) = (1, 1)
        for j in range(len(A)):
            if j != i and A[j] < A[i]:
                r += 1
            if j != i and A[j] == A[i]:
                s += 1      
        
        # Use formula to obtain rank
        R[i] = r + (s - 1) / 2
 
    # Return Rank Vector
    return R

def spearmanCor(x, y):

    r1 = rankify(x)
    r2 = rankify(y)
    
    d = list(map(lambda i, j:  i-j, r1, r2))

    sd = sum([i**2 for i in d])
    n = len(x)
    return(1-(sd)/(n*(n**2-1)))

    
def spearmanCorTest(x, y):

    ''' t test for spearman rho rank correlation '''
    r = spearmanCor(x, y)
    n = len(x)
    t = r*((n-2)/(1-r**2)**0.5)

    return({'tstat': t, 'df':n-1})


def condis(x, y):

    ''' this function return concordant and discordant pairs as in dictionary '''

    ind1 = []; con = 0; dis = 0

    for i, j in zip(x, y):
        if i == j:
            ind1.append(1)
            con += 1
        else:
            ind1.append(0)
            dis += 1
    return({'con':con, 'dis':dis})

def kendalsTau(x, y):

    ''' this returns kendal's tau statistic for 'x', 'y' '''

    r1 = condis(x, y)['con']
    r2 = condis(x, y)['dis']

    n = len(x)
    return((r1-r2)/(n*(n-1)/2))


def correl(x, y):

    xdev = [(i - Mean(x)) for i in x]
    ydev = [(i - Mean(y)) for i in y]

    sdev = []

    for i in range(len(xdev)):
        sdev.append(xdev[i]*ydev[i])

    numer = sum(sdev)

    dnom1 = [(i-Mean(x))**2 for i in x]
    dnom2 = [(i-Mean(y))**2 for i in y]

    dnom1 = sum(dnom1)**0.5
    dnom2 = sum(dnom2)**0.5

    denom = dnom1 * dnom2

    stat = numer/denom

    return stat
    
# def cortest(): 
    
    

