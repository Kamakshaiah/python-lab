# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
##### dot plot ##########
##
##import matplotlib.pyplot as plt
##
### data simulation
##
##data = [('apples', [0.1, 0.25]),
##	    ('oranges', [0.6, 0.35]),
##	    ('pears', [0.1, 0.18]),
##	    ('bananas', [0.7, 0.98]),
##	    ('peaches', [0.6, 0.48])]
##
##names = [item[0] for item in data]
##predicted = [item[1][0] for item in data]
##observed = [item[1][1] for item in data]
##
### figure
##
##fig, ax = plt.subplots()
##
##ax.plot(observed, color = 'lightblue', marker = 'o', linestyle = 'none', markersize = 12, label='Observed')
##ax.plot(predicted, color = 'red', marker = 's', linestyle = 'none', markersize = 12, label='Predicted')
##
##ax.margins(0.1) # this command just push data inside try using different values
##
##ax.legend(loc='best', numpoints = 1)
##ax.grid(axis='y')
##ax.set(xticks=range(len(names)), xticklabels=names, ylabel = 'Y Data')
##plt.show()
##
##
##### bar plot for ordinal data (responses) ##########
##
##x = [1] * 3 + [2] * 3 + [3] * 3 + [4] * 1
##print(x)
##
##import random
##random.shuffle(x)
##

def catDat(x):
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

##catDat(x)[0]
##catDat(x)[1]
##sum(catDat(x)[1])
##
##plt.bar(range(1, 5), catDat(x)[1], align = 'center')
##plt.xticks(range(1, 5), catDat(x)[0])
### bar plot
##
##plt.bar(range(2), [round(random.random()*100) for i in range(2)])
##
##
##### bar plot for ordinal data (gender) ##########
##
##import random
##
##gender = ['male', 'female']
##
##y_pos = range(len(gender))
##dat = [round(random.random()*100) for i in range(2)]
##
###fig, ax = plt.subplots()
###
####plt.xticks(y_pos, gender)
###ax.bar(y_pos, dat, align = 'center')
###ax.set(xticks=range(len(gender)), xticklabels=gender)
###plt.show()
##import pylab as plt
##
##plt.bar(y_pos, dat, align = 'center')
##plt.xticks(y_pos, gender)
##
##
########## Pie Chart ############
##
##labels = [item[0] for item in data]
##observed = [item[1][1]*100 for item in data]
##colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', "red"]
##explode = (0.1, 0, 0, 0, 0)
##
##plt.pie(observed, explode=explode, labels=labels, colors=colors,
##        autopct='%1.1f%%', shadow=True, startangle=140)
##
##
### ploting diagrams from CSV file
##
##import pandas as pd
##
##dat = pd.read_csv('/media/hi/C2ACA28AACA278951/Windows/My Writings/Books/Python_30days/data/samp.csv')
##dat[1:6]
##
##df = pd.value_counts(dat['gender']).to_frame().reset_index()
##
##plt.bar(range(1,3), df['gender'], align = 'center', color = 'lightcoral')
##plt.xticks(range(1,3), df['index'])
##
### NORMAL CURVE
##
##from matplotlib.mlab import normpdf
##import matplolib.pyplot
##import pylab as p
##import numpy as np
##
##
##from scipy import stats
###tvals = stats.t.cdf(np.arange(0, 0.99, 0.0125), 79)
##
##x = np.arange(-4, 4, 0.1)
##len(x)
##
##tvals1 = stats.t.pdf(x, 1)
##tvals2 = stats.t.pdf(x, 2)
##tvals30 = stats.t.pdf(x, 30)
##
##len(tvals1)
##len(tvals2)
##len(tvals30)
##
###cols = ('blue', 'red', 'yello')
##
##p.plot(x, tvals1, x, tvals2, x, tvals30)
##
##p.plot(x, tvals1)
##p.plot(x, tvals2)
##p.plot(x, tvals30)
##
##
### shade area
##
##x = np.arange(-4, 4, 0.01)
##y = normpdf(x, 0, 1)
##z = normpdf(x[1:200], 0, 1)
##
##p.plot(x, y, color = "blue", lw=2)
##p.fill_between(x[1:200], z, color = "red")
##p.show()
##
### boltzman curve
##
##def boltzman(x, xmid, tau):
##    return 1. / (1. + np.exp(-(x-xmid)/tau))
##
##x = np.arange(-6, 6, .01)
##S = boltzman(x, 0, 1)
##Z = 1-boltzman(x, 0.5, 1)
##p.plot(x, S, x, Z, color='red', lw=2)
##p.show()
##
### text in plot
##import matplotlib.pyplot as plt
##
##fig = plt.figure()
##fig, ax = plt.subplots(111)
##
##p.plot(x, tvals1, x, tvals2, x, tvals30)
##plt.text(0, 0.20, "DoF=1", color = "red")
##plt.annotate('DoF2', xy=(1, 0.20), xytext=(3, 0.30), arrowprops=dict(facecolor='black', shrink=0.025, width = 1, headwidth=3), color = "red")
##plt.annotate('DoF30', xy=(1, 0.30), xytext=(3, 0.37), arrowprops=dict(facecolor='black', shrink=0.025, width = 1, headwidth=3), color = "red")
##plt.text(0, 0.20, "DoF=1", color = "red")
##plt.show()

#
#fig = plt.figure()
#fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
#
#ax = fig.add_subplot(111)
#fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
#
#ax.set_xlabel('xlabel')
#ax.set_ylabel('ylabel')
#
#ax.text(3, 8, 'boxed italics text in data coords', style='italic',
#        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
#
#ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)
#
#ax.text(3, 2, u'unicode: Institut f\374r Festk\366rperphysik')
#
#ax.text(0.95, 0.01, 'colored text in axes coords',
#        verticalalignment='bottom', horizontalalignment='right',
#        transform=ax.transAxes,
#        color='green', fontsize=15)
#
#
#ax.plot([2], [1], 'o')
#ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
#            arrowprops=dict(facecolor='black', shrink=0.05))
#
#ax.axis([0, 10, 0, 10])
#
#plt.show()

def simNumVec(n):
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
    import random

    x = []
    for i in range(n):
        x.append(round(random.random()*100))
    return(x)

def simHetDat(n, r):
    ''' this cretes response wisedata for n times for gender, occupation, marital status '''
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
    #return (dict(KPCC = stat, numerator = numer, den1 = dnom1, den2 = dnom2))

##def regCoefs(x, y):
##
##    s1 = sum(x)
##    s2 = sum(y)
##    s3 = 
    
