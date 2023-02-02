# simulations

def catDat(x):

    ''' Creates categorical data.
        Input: 'x' should be a random vector of numbers.
        Output: A list of categories along with frequencies.  '''
    
    a = b = c = d = 0
    a; b; c; d

    for i in x:
        if i == 1:
            a = a + 1
        elif i == 2:
            b = b + 1
        elif i == 3:
            c = c + 1
        elif i == 4:
            d = d + 1

    data = [('one', a),
            ('two', b),
            ('three', c),
            ('four', d)]
    y = []
    z = []

    for i in data:
        y.append(i[0])
        z.append(i[1])
    return y, z

def simNumVec(n):
    ''' creates a vector of random numbers as by user input 'n' '''
    
    import random

    x = []
    for i in range(n):
	      x.append(round(random.random()*100))
    y = []
    for i in range(n):
	      y.append(round(random.random()*100))

    args = ["x", "y"]

    print(("{:^6.5}"*2).format(*args))
    for i, j in zip(x, y):
        print('{0:5}{1:5}'.format(i,j))


def simVec(n):
    ''' creates a vector of random numbers as by user input 'n' '''
    
    import random

    x = []
    for i in range(n):
        x.append(round(random.random()*100))
    return(x)

def simHetDat(n, r):
    ''' A function to create heterogeneous data variables such as 'gender', 'occupation', 'marital status'.
        The responses are as follows: 
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
        dat = pd.DataFrame({'gen':g1, 'occ':g2, 'ms':g3, 'freq.':x})
        return(dat)

    elif (r == "gender"):
        dat = pd.DataFrame({'gen':g1, 'freq.':x})
        return(dat)

    elif (r == "occupation"):
        dat = pd.DataFrame({'occ':g2, 'freq.':x})
        return(dat)

    elif (r == "marital status"):
        dat = pd.DataFrame({'ms':g3, 'freq.':x})
        return(dat)

    else:
        print('response is missing')
        raise SystemExit
