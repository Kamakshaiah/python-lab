# I. functions for data manipulation (editing and coding)     
# Resources
# central tendency: https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/

def simNumData(n, m, *args):
    ''' creates a vector of 1 to m values for max. n '''
    import random as rnd
    import string
    x = []
    if "num" in args:
        for i in range(m):
            x.append(rnd.randint(1, n))
    elif "cat" in args:
        x = list(string.ascii_letters[1:n])
    return(x)

def simCatData(n, cats):
    ''' creates a vector of user responses '''
    import random as rnd
    x = []
    for i in range(n):
        x.append(rnd.choice(cats))
    return(x)

def toCat(*args):
    ''' Converts numerical data into categorical data '''
    tocat = []
    for i in y:
        if i > 0 and i <= 30:
            tocat.append("0 to 30")
        elif i > 30 and i <= 60:
            tocat.append("30 to 60")
        elif i > 60 and i <= 90:
            tocat.append("60 to 90")
        elif i > 90 and i <= 100:
            tocat.append("90 to 100")
    return(tocat)

# utilities

def findObject(pkg_name, str_name):
    ''' finds the search string in the package/module '''
    import pkg_name
    for i in dir(pkg_name):
        if i == str_name:
            print(i)
        else:
            print("you have not that string in search path")


#II.  functions for measures of central tendency

def mean(x, *args):
    from functools import reduce 
    if "am" in args:
        return(sum(x)/len(x))
    elif "gm" in args:
        out = reduce((lambda x, y: x*y), x)
        return out**(1/len(x))
    elif "hm" in args:
        numer = len(x)
        denom = [1/i for i in x]
        return(numer/sum(denom))
    
def square(x, *args):
    ''' this function make square of each element using loops and conditions '''
    templi = []
    
    if "lambda" in args:
          return(list(map(lambda i: i**2, x)))
    else:
        for i in x:
            templi.append(i**2)
        return(templi)
    
def inputOutputEx(n):
    ''' a simple function to compute arithmetic value for 'n' user input values '''
    from functools import reduce
    x = []; i = 0
    for i in range(n):
        x.append(input("write a value:"))
    
    numer = sum(map(int, x))
    denom = len(x)
    return(numer/denom)

def median(x):
    ''' returns median of input data variable '''
    n = len(x)
    if n % 2 == 0:
        med1 = x[n // 2]
        med2 = x[n//2 - 1]
        median = (med1 + med2)/2
    else:
        median = x[n // 2]
    return(median)

def mode(x):
    ''' returns modal value of given distribution '''
    n = len(x)
    from collections import Counter
    data = Counter(x)
    datadict = dict(data)
    mode = [k for k, v in datadict.items() if v == max(list(datadict.values()))]
    if len(mode) == n:
        print("No mode found")
    else:
        return(mode) 
    
      
# III. measures of dispersion



# IV. measures of shape

# V. Bivariate

#1. t test
#2. cor test
#3. normality tests

# probability distributions using 'random' module

def paratovar(n, a, plot="false"):
    ''' creates parato distribution with:
        n - size of distribution 
        a - number of data points
        if 'plot = true' create parato-plot. '''
    import random
    import matplotlib.pyplot as plt
    x = []
    for i in range(n):
        x.append(random.paretovariate(a))
    if plot == "true":
        plt.plot(x)
        plt.show()
    else:
        return(x)

