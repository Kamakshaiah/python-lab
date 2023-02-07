# corsstab
from scipy.stats.contingency import crosstab

a = ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B']
x = ['X', 'X', 'X', 'Y', 'Z', 'Z', 'Y', 'Y', 'Z', 'Z'] # three level vector
(alevels, xlevels), count = crosstab(a, x)
print(alevels)
print(xlevels)
print(count) # this is cross tab

# odds ratio

from scipy.stats import fisher_exact
table = [[6, 2],
        [1,  4]]

oddsr, p = fisher_exact(table, alternative='greater')
print([oddsr, p])


a = ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B']
x = ['X', 'X', 'X', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y'] # 2 level table
(_, _), table = crosstab(a, x)
print(table)

oddsr, p = fisher_exact(table, alternative='greater')
print([oddsr, p])
