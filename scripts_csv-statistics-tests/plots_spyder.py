# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
### dot plot ##########

import matplotlib.pyplot as plt

# data simulation

data = [('apples', [0.1, 0.25]),
	    ('oranges', [0.6, 0.35]),
	    ('pears', [0.1, 0.18]),
	    ('bananas', [0.7, 0.98]),
	    ('peaches', [0.6, 0.48])]

names = [item[0] for item in data]
predicted = [item[1][0] for item in data]
observed = [item[1][1] for item in data]  

# figure 

fig, ax = plt.subplots()

ax.plot(observed, color = 'lightblue', marker = 'o', linestyle = 'none', markersize = 12, label='Observed')
ax.plot(predicted, color = 'red', marker = 's', linestyle = 'none', markersize = 12, label='Predicted')

ax.margins(0.1) # this command just push data inside try using different values

ax.legend(loc='best', numpoints = 1)
ax.grid(axis='y')
ax.set(xticks=range(len(names)), xticklabels=names, ylabel = 'Y Data')
plt.show()


### bar plot for ordinal data (responses) ##########

x = [1] * 3 + [2] * 3 + [3] * 3 + [4] * 1
print x

import random
random.shuffle(x)


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

catDat(x)[0]
catDat(x)[1]
sum(catDat(x)[1])

plt.bar(range(1, 5), catDat(x)[1], align = 'center')
plt.xticks(range(1, 5), catDat(x)[0])
# bar plot

plt.bar(range(2), [round(random.random()*100) for i in range(2)])


### bar plot for ordinal data (gender) ##########

import random

gender = ['male', 'female']

y_pos = range(len(gender))
dat = [round(random.random()*100) for i in range(2)]

#fig, ax = plt.subplots()
#
##plt.xticks(y_pos, gender)
#ax.bar(y_pos, dat, align = 'center')
#ax.set(xticks=range(len(gender)), xticklabels=gender)
#plt.show()
import pylab as plt

plt.bar(y_pos, dat, align = 'center')
plt.xticks(y_pos, gender)


######## Pie Chart ############

labels = [item[0] for item in data]
observed = [item[1][1]*100 for item in data]  
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', "red"]
explode = (0.1, 0, 0, 0, 0)

plt.pie(observed, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
        

# ploting diagrams from CSV file 

import pandas as pd

dat = pd.read_csv('/media/hi/C2ACA28AACA278951/Windows/My Writings/Books/Python_30days/data/samp.csv')
dat[1:6]

df = pd.value_counts(dat['gender']).to_frame().reset_index()

plt.bar(range(1,3), df['gender'], align = 'center', color = 'lightcoral')
plt.xticks(range(1,3), df['index'])

# NORMAL CURVE

from matplotlib.mlab import normpdf
import matplolib.pyplot 
import pylab as p
import numpy as np


from scipy import stats
#tvals = stats.t.cdf(np.arange(0, 0.99, 0.0125), 79)

x = np.arange(-4, 4, 0.1)
len(x)

tvals1 = stats.t.pdf(x, 1)
tvals2 = stats.t.pdf(x, 2)
tvals30 = stats.t.pdf(x, 30)

len(tvals1)
len(tvals2)
len(tvals30)

#cols = ('blue', 'red', 'yello')

p.plot(x, tvals1, x, tvals2, x, tvals30)

p.plot(x, tvals1)
p.plot(x, tvals2)
p.plot(x, tvals30)


# shade area

x = np.arange(-4, 4, 0.01)
y = normpdf(x, 0, 1)
z = normpdf(x[1:200], 0, 1)

p.plot(x, y, color = "blue", lw=2)
p.fill_between(x[1:200], z, color = "red")
p.show()

# boltzman curve

def boltzman(x, xmid, tau):
    return 1. / (1. + np.exp(-(x-xmid)/tau))

x = np.arange(-6, 6, .01)
S = boltzman(x, 0, 1)
Z = 1-boltzman(x, 0.5, 1)
p.plot(x, S, x, Z, color='red', lw=2)
p.show()

# text in plot
import matplotlib.pyplot as plt

fig = plt.figure()
fig, ax = plt.subplots(111)

p.plot(x, tvals1, x, tvals2, x, tvals30)
plt.text(0, 0.20, "DoF=1", color = "red")
plt.annotate('DoF2', xy=(1, 0.20), xytext=(3, 0.30), arrowprops=dict(facecolor='black', shrink=0.025, width = 1, headwidth=3), color = "red")
plt.annotate('DoF30', xy=(1, 0.30), xytext=(3, 0.37), arrowprops=dict(facecolor='black', shrink=0.025, width = 1, headwidth=3), color = "red")
plt.text(0, 0.20, "DoF=1", color = "red")
plt.show()

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
