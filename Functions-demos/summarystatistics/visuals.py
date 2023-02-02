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

def twobytwoplot():
    ''' creates a visual for 2 by 2 graph grid
        requires no inputs
    '''
    import numpy as np
    import matplotlib.pyplot as plt

    for i in range(1, 5):
        plt.subplot(2, 2, i)
        x = np.random.uniform(1, 2, 100)
        y = np.random.uniform(1, 2, 100)
        plt.plot(x, y, 'o')
    plt.show()

def PDFPlot():

    ''' creates a visual for PDF for normally distributed data
        requires no inputs
    '''

    import numpy as np
    import scipy.stats as stats
    import matplotlib.pyplot as plt

    x = np.random.normal(0, 1, 100)
    res = stats.probplot(x, plot=plt)
    plt.show()

def CDFPlot():

    ''' creates a visual for CDF for normally distributed data
        requires no inputs
    '''

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
