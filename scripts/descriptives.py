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



def tTest(a, *args):

    import numpy as np
    import scipy.stats as stats

    for x in args:

        x_bar = np.mean(x)
        std = np.std(x)
        se = std/(len(x)**0.5)
        t_stat = (x_bar - a)/se
        df = len(x) - 1
        p = 1 - stats.t.cdf(t_stat,df=df)

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

