# https://www.analyticsvidhya.com/blog/2020/06/introduction-anova-statistics-data-science-covid-python/
# https://towardsdatascience.com/anova-test-with-python-cfbf4013328b
# https://www.javatpoint.com/anova-test-in-python [best]
# one-way

p1 = np.random.randint(20, 100, 10)
p2 = np.random.randint(20, 100, 10)
p3 = np.random.randint(20, 100, 10)
p4 = np.random.randint(20, 100, 10)
import scipy as sp
sp.stats.f_oneway(p1, p2, p3, p4) # F_onewayResult(statistic=0.8501996248015778, pvalue=0.47566392232042465)

# two-way anonva

import numpy as np
import pandas as pd
  
# Create a dataframe
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
                          'Watering': np.repeat(['daily', 'weekly'], 15),
                          'height': [14, 16, 15, 15, 16, 13, 12, 11, 14, 
                                     15, 16, 16, 17, 18, 14, 13, 14, 14, 
                                     14, 15, 16, 16, 17, 18, 14, 13, 14, 
                                     14, 14, 15]})

import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('height ~ C(Fertilizer) + C(Watering) + C(Fertilizer):C(Watering)', data=dataframe).fit()
result = sm.stats.anova_lm(model, type=2)
print(result)
