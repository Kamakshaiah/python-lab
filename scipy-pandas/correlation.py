import numpy as np

# data simulations

sales_north = np.random.random_sample(120).reshape(30, 4)
sales_south = np.random.random_sample(120).reshape(30, 4)

import pandas as pd

df_north = pd.DataFrame(sales_north, columns=['p1', 'p2', 'p3', 'p4'])
df_north.head()

df_south = pd.DataFrame(sales_south, columns=['p1', 'p2', 'p3', 'p4'])
df_south.head()

# bi-variate
np.corrcoef(df_north.p1, df_south.p1)

# multivariate
df_north.corr()
df_north.corrwith(df_south)

# plots

import seaborn as sns # pip install seaborn
sns.heatmap(df_north.corr(), annot=True)
import matplotlib.pyplot as plt
plt.show()

# canonical correlation

# https://cmdlinetips.com/2020/12/canonical-correlation-analysis-in-python/
# https://stackoverflow.com/questions/37398856/how-to-get-the-first-canonical-correlation-from-sklearns-cca-module

from sklearn.cross_decomposition import CCA

U = np.random.random_sample(500).reshape(100,5)
V = np.random.random_sample(500).reshape(100,5)

cca = CCA(n_components=1)
cca.fit(U, V)

cca.coef_.shape                   # (5,5)

U_c, V_c = cca.transform(U, V)

U_c.shape                         # (100,1)
V_c.shape                         # (100,1)

n_comp=1
result = np.corrcoef(U_c.T, V_c.T).diagonal(offset=n_comp) # array([0.38012262])
score = np.diag(np.corrcoef(cca.x_scores_, cca.y_scores_, rowvar=False)[:n_comp, n_comp:]) # array([0.38012262])

# https://github.com/gallantlab/pyrcca/ [another package]
