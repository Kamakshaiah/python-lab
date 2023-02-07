def passFun():
    ''' just pass the function '''
    pass

def myMean(vec):

    ''' computes arithmentic mean '''

    return(sum(vec)/len(vec))

def argExample(*args):
    ''' example for arguments '''

    for arg in args:
        print(arg)

def kwargsExample(**kwargs):
    ''' example for keyword arguments '''

    for kw in kwargs:
        print(kw, ':', kwargs[kw])

def argsAndKwargsExample(*args, **kwargs):
    ''' example for both arguments and keyword arguments '''
    for arg in args:
        print(arg)

    for kw in kwargs:
        print(kw, ':', kwargs[kw])
        
def meanMaxMin(vec, *args):
    ''' This function creates Maximum and Minimum along with Mean as by user arguments.

        Arguments:
        vec: Input vector
        *args: positional arguments. eg. 'min' and 'max'

        Output:
        Returns default value: mean and either minumum or maximum by argument. 
        
    '''

    out1 = myMean(vec)
    if 'max' in args:
        out2 = max(vec)
        return({'mean': out1, 'max':out2})
    if 'min' in args:
        out2 = min(vec)
        return({'mean': out1, 'min':out2})

def product(vec):
    ''' gives product of elements in given vector (vec) '''
    res = 1
    for i in vec:
        res *= i
    return(res)
    
def rankData(x):
    ''' Returns ranks for input variable 'x' '''
    return([sorted(x).index(i) for i in x])

def geoMean(vec):
    ''' geometric mean '''
    n = len(vec)
    return(product(vec)**(1/n))

def harMean(vec):
    ''' harmonic mean '''
    s = 0
    n = len(vec)
    for i in vec:
        s += 1/i
    return(n/s)

def meanByType(vec, **kwargs):
    ''' example for means '''
    for kw in kwargs:
        if kwargs[kw] == 'am':
            print(kw, ':', myMean(vec))
        elif kwargs[kw] == 'gm':
            print(kw, ':', geoMean(vec))
        elif kwargs[kw] == 'hm':
            print(kw, ':', harMean(vec))
    else:
        return(list(vec))

def zerosMatrix(m, n):
    ''' creates zeros matrix '''

    mat = [[0]*n for i in range(m)]
    return(mat)

def identityMatrix(n):
    ''' creates identiry matrix '''
    mat = [[int(x==y) for x in range(n)]for y in range(n)]
    return(mat) 
	
def onesMatrix(m, n):
    ''' creates ones matrix '''
    mat = [[1] * n for i in range(m)]
    return(mat) 

def randMatrix(n, a, b):
    ''' Creates a X b order matrix with random data '''
    import random as rnd
    mat = [[rnd.randint(1, n) for i in range(b)] for j in range(a)]
    return(mat) 
        
def matrixAddition(m1, m2):
    ''' Adds input matrices m1 and m2 '''

    m = len(m1)
    n = len(m2[0])
    result = zerosMatrix(m, n)
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] + m2[i][j]
    return(result) 

def matrixSubtraction(m1, m2):
    ''' Subtracts one matrix 'm2' from another matrix 'm1' for input matrices m1 and m2 '''

    m = len(m1)
    n = len(m2[0])
    result = zerosMatrix(m, n)
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] - m2[i][j]
    return(result)

def pairwiseProduct(m1, m2):
    ''' Performs pairwise multiplications of elements from input matrices m1 and m2 '''
    
    result = zerosMatrix(len(m1), len(m2))
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            result[i][j] = m1[i][j] * m2[i][j]
    return(result) 

def matrixMultiplication(m1, m2):
    ''' Performs matrix multiplication of elements from input matrices m1 and m2 '''

    m = len(m1)
    n = len(m2[0])
    
    result = zerosMatrix(m, n)

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return(result)

def matMulVec(m1, m2):
    ''' Performs matrix multiplication of elements from input vectors m1 and m2 '''
    out = sum([i*j for i, j in zip(rs, cs)])
    return(out) 

def matrixDivision(m1, m2):
    ''' Divides input matrix m1 with m2 and provides resultant matrix '''

    m = len(m1)
    n = len(m2[0])
    result = zerosMatrix(m, n)

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] / m2[i][j]

    return(result) 

def matrixTranspose(m):
    ''' Transpose matrix m '''

    a = len(m)
    try:
        b = len(m[0])
    except:
        b = len([m[0]])
        
    result = zerosMatrix(b, a)
    
    for j in range(a): 
        for i in range(b): 
            result[i][j] = m[j][i]

    return(result) 

def Diagonals(m):

    ''' Calculates original and reverse diagonals for given input matrix 'm' '''

    diag = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == j:
                diag.append(m[i][j])
    revdiag = []
    a = list(reversed(list(range(len(m)))))
    b = list(range(len(m)))
    for i, j in zip(a, b):
        revdiag.append(m[j][i])

    return({'diagonal':diag, 'rev-diagonal': revdiag})

def Product(m):
    ''' Creates product of elements given in the input vector 'm' '''
    from functools import reduce
    return(reduce(lambda x, y: x * y, m))

def sumProduct(x, y):
    ''' Caluculates sum product for input vectors 'x' and 'y' '''
    return(sum(map(lambda x, y: x * y, x, y)))

def matDivide(data, dv):

    ''' helper function for performing chisuare analysis:
        Divides a matrix with required value '''

    out = sum(data, [])

    exmat = []
    for i in out:
        exmat.append(i/dv)

    rows = len(data)
    cols = len(data[0])

    ll = []
    ul = []

    for i in range(rows):
        ll.append(i*cols)

    for i in ll:
        ul.append(i+cols)
            

    res = []
    for i, j in zip(ll, ul):
        res.append(exmat[i:j])

    return(res) 

def matPower(data, po):

    ''' helper function for performing chisuare analysis:
        Calculates power of matrix with required value '''

    out = sum(data, [])

    exmat = []
    for i in out:
        exmat.append(i**po)

    rows = len(data)
    cols = len(data[0])

    ll = []
    ul = []

    for i in range(rows):
        ll.append(i*cols)

    for i in ll:
        ul.append(i+cols)
            

    res = []
    for i, j in zip(ll, ul):
        res.append(exmat[i:j])

    return(res)

def rowSums(m):
    ''' Calculates rows sums for given matrix 'm' '''
    rowSums = []
    for i in range(len(m)):
        rowSums.append(sum(m[i]))
    return(rowSums)

def colSums(m):
    ''' Calculates column sums for given matrix 'm' '''
    colsums = []
    for col in range(len(m[0])):
        t = 0
        for row in m:
            t += row[col]
        colsums.append(t)
    #return([sum(col) for col in zip(*m)])
    return(colsums)
