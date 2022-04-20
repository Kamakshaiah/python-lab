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

def twoSampleTTest(x, y, *args):
    ''' Computes T Statistics for two different samples say X, Y
        Inputs: Vectors with equal sample sizes
        Output: T Value and P Value
        '''
    import numpy as np
    import scipy.stats as stats

    mean1 = np.mean(x)
    mean2 = np.mean(y)
       
    if len(x) == len(y):
        if 'equalsamples' in args:
            sp = ((np.var(x)+np.var(y))/2)**0.5
            t_stat = ((mean1 - mean2)/(sp*(2/len(x))**0.5))
            df = (2*len(x) - 2)
            p = stats.t.sf(abs(t_stat), df=df)
            return({'T Value': t_stat, 'P Value': p*2})
        elif 'equalvariances' in args:
            sp = ((((len(x) - 1)*np.var(x)) + (len(y)*np.var(y)))/(len(x)+len(y)+2))
            t_stat = ((mean1 - mean2)/(sp*((1/len(x))+(1/len(y)))**0.5))
            df = (len(x) + len(y) + 2)
            p = stats.t.sf(abs(t_stat), df=df)
            return({'T Value': t_stat, 'P Value': p*2})
        elif 'unequalvariances' in args:
            sp = ((np.var(x)/len(x))+(np.var(y)/len(y)))
            t_stat = ((mean1 - mean2)/sp)
            df = ((np.var(x)/len(x)) + (np.var(y)/len(y)))**2/((((np.var(x)/len(x))**2)/(len(x) - 1))+(((np.var(y)/len(y))**2)/(len(y) - 1)))
            p = stats.t.sf(abs(t_stat), df=df)
            return({'T Value': t_stat, 'P Value': p*2})
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

    from scipy.stats import chi2

    s = skewness(x)
    k = kurtosis(x)
    jbs = len(x)*((s**2/6)*(k**2/24))

    return (1-chi2.pdf(jbs, 2))

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

    ''' This function helps assessing normality of given data variable using skewness. Gives p value for test statistic '''

    import scipy.stats as stats

    s = skewness(x)
    z = s/(6/len(x)**0.5)
    p = stats.norm.cdf(z)
    return p

def kurtNormTest(x):

    ''' This function helps assessing normality of given data variable using kurtosis. Gives p value for test statistic '''

    import scipy.stats as stats

    k = kurtosis(x)
    z = k/(24/len(x)**0.5)
    p = stats.norm.cdf(z)
    return p

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
