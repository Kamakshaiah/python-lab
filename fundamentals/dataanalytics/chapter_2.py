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

    for r in mat:
        print(r)

def identityMatrix(n):
    ''' creates identiry matrix '''
    m = [[int(x==y) for x in range(n)]for y in range(n)]
    for i in m:
        print(i)
	
def onesMatrix(n):
    ''' creates ones matrix '''
    rows = [[1] * n for i in range(n)]
    for r in rows:
        print(r)
