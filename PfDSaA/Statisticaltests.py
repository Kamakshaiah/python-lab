def tTest(a, *args):
    ''' Computes T Test:
        Inputs:
            a: assumed mean
            *args: data vector
        Output:
            T Value: Calculated T Value
            P Value: Probability Value for Cal. T Vallue '''
    import numpy as np
    import scipy.stats as stats

    for x in args:

        x_bar = np.mean(x)
        std = np.std(x)
        se = std/((len(x)-1)**0.5)
        t_stat = (x_bar - a)/se
        df = len(x) - 1
        p = stats.t.sf(t_stat, df=df)
    
        return({'T Value': t_stat, 'P Value': p*2})

def oneSampleAnova(factor, vector):
    ''' Computes F Statistic and P Value for given data.
        Inputs:
            Data set with one factor and one vector (numeric variable)
        Output:
            SSBetween
            SSWithin
            F Statistic
            P Value '''
    import pandas as pd
    import Simulations as sml
    import scipy.stats as stats

    data = pd.DataFrame({'factor':factor, 'vector':vector})
    
    k = len(pd.unique(data.factor))
    N = len(data.values)
    n = data.groupby('factor').size()[0]

    DFbet = k - 1
    DFwith = N - k
    DFtot = N - 1

    SSbet = (sum(data.groupby('factor').sum()['vector']**2)/n) \
    - (data['vector'].sum()**2)/N
    sum_y_sq = sum([value**2 for value in data['vector'].values])
    SSwith = sum_y_sq - sum(data.groupby('factor').sum()['vector']**2)/n
    SStot = sum_y_sq - (data['vector'].sum()**2)/N

    MSbet = SSbet/DFbet
    MSwith = SSwith/DFwith
    F = MSbet/MSwith
    p = stats.f.sf(F, DFbet, DFwith)

    return({'F Statistic': F, 'P VAlue': p})

def chiSqStat(obd, exd):
    ''' Calculates chi-square statistic for numeric data inputs
        Input:
            obd: observed data
            exd: expected data
        Output:
            Chi-square statistic
            '''
    dif = sum([((obd[i] - exd[i])**2/exd[i]) for i in range(len(obd))])
    return dif

def twoSampleTTest(x, y, *args):
    ''' Computes T Statistics for two different samples say X, Y
        Inputs: Vectors with equal sample sizes
        Output: T Value 
        '''
    from Descriptives import Mean, Var
    
    mean1 = Mean(x)
    mean2 = Mean(y)
       
    if len(x) == len(y):
        if 'equalsamples' in args:
            sp = ((Var(x    )+Var(y))/2)**0.5
            t_stat = ((mean1 - mean2)/(sp*(2/len(x))**0.5))
            return(t_stat)
        elif 'equalvariances' in args:
            sp = ((((len(x) - 1)*Var(x)) + (len(y)*Var(y)))/(len(x)+len(y)+2))
            t_stat = ((mean1 - mean2)/(sp*((1/len(x))+(1/len(y)))**0.5))
            return(t_stat)
        elif 'unequalvariances' in args:
            sp = ((Var(x)/len(x))+(Var(y)/len(y)))
            t_stat = ((mean1 - mean2)/sp)
            return(t_stat)
    else:
        print('Sample sizes are not equal')


def plotNormal(x):
    ''' this method plots normal curve for given data'''

    # importing packs

    import numpy as np
    from scipy.stats import norm
    import matplotlib.pyplot as plt

    # data transformation
    y = norm.pdf(x, 0, 1)
    plt.plot(x, y)
    plt.show()

def jbTest(x):

    ''' Calculates JB Test Statistic for input vector (x) '''

    from Descriptives import Skewness, Kurtosis
    s = Skewness(x)
    k = Kurtosis(x)
    jbs = (len(x)/6)*((s**2)+((1/4)*(k-3)**2))

    return(jbs)

def normCheck(x):

    import numpy as np
    import scipy.stats as stats
    import matplotlib.pyplot as plt

    # x = stats.norm.rvs(0, 1, 100)
    x.sort()
    y = np.linspace(-3, 3, len(x))
    y1 = np.linspace(min(x), max(x), len(x))

    # slope, intercept = np.polyfit(x, y, 1)

    plt.scatter(y, x)
    plt.plot(y, y1, color="red")
    plt.show()

def skewNormTest(x):

    ''' Calculates z statistic for given data (x) '''

    import scipy.stats as stats
    from Descriptives import Skewness
    
    s = Skewness(x)
    z = s/(6/len(x))**0.5
    p = stats.norm.sf(z)
    return(z) 

def kurtNormTest(x):

    ''' Calculates z statistic for given data (x) '''
    from Descriptives import Kurtosis
    k = Kurtosis(x)
    z = k/(24/len(x))**0.5
    return(z)

def twobytwoplot():

    import numpy as np
    import matplotlib.pyplot as plt

    for i in range(1, 5):
        plt.subplot(2, 2, i)
        x = np.random.uniform(1, 2, 100)
        y = np.random.uniform(1, 2, 100)
        plt.plot(x, y, 'o')
    plt.show()


def probPlot():

    import numpy as np
    import scipy.stats as stats
    import matplotlib.pyplot as plt

    x = np.random.normal(0, 1, 100)
    res = stats.probplot(x, plot=plt)
    plt.show()

def myProbPlot():

    import numpy as np
    import scipy.stats as stats
    import matplotlib.pyplot as plt

    y = np.random.normal(0, 1, 100)
    y.sort()
    y1 = stats.norm.cdf(y, np.mean(y), np.std(y))
    x = np.linspace(-3, 3, 100)
    x1 = np.linspace(min(y1), max(y1), len(y))

    plt.scatter(x, y1, color = 'blue')
    plt.plot(x, x1, color = "red")
    plt.show()
