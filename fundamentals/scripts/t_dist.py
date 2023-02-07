# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:30:31 2018

@author: hi
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = np.arange(-4, 4, 0.1)

tvals1 = stats.t.pdf(x, 1)
tvals2 = stats.t.pdf(x, 30)


plt.plot(x, tvals1, x, tvals2)
plt.text(0, 0.15, 'DoF1', color = "red")
plt.annotate("DoF30", xy=(1, 0.25), xytext = (3, 0.35), arrowprops=dict(facecolor="black", shrink=0.025, width=1, headwidth=4), color="red")