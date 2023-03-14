# quantiles

a = np.arange(24).reshape(2,3,4)
np.quantile(a, 0.5, axis=0); np.quantile(a, 0.5, axis=1)

# percentiles

a = np.array([[10, 7, 4], [3, 2, 1]])
np.percentile(a, 50, axis=0)
np.percentile(a, 50, axis=1)

# averages

data = np.arange(1, 5)
np.average(data)
np.average(np.arange(1, 11), weights=np.arange(10, 0, -1)) # weighted average

data = np.arange(6).reshape((3, 2))
np.average(data, axis=1, weights=[1./4, 3./4]) # col-wise wt. average

# summries 
a = np.array([[5, 9, 13], [14, 10, 12], [11, 15, 19]])
a.sum()/a.size
a.mean()

a = np.array([[1, 2], [3, 4]])
np.mean(a)
np.mean(a, axis=0)
np.mean(a, axis=1)

a.std()
np.std(a, axis=0)
np.std(a, axis=1)

a.var()
np.var(a, axis=0)
np.var(a, axis=1)

np.median(a, axis=0)
np.median(a, axis=1)

# covariance

x = np.array([[0, 2], [1, 1], [2, 0]]).T
# x
np.cov(x)
x = [-2.1, -1, 4.3]
y = [3, 1.1, 0.12]
np.cov(x, y)
X = np.stack((x, y), axis=0)
# X
np.cov(X)

# correlation

import numpy as np
rng = np.random.default_rng(seed=42)
rng # Generator(PCG64) at 0x24D740552A0
xarr = rng.random((3, 3)) # xarr
R1 = np.corrcoef(xarr) # correlation matrix for xarr

yarr = rng.random((3, 3))
R2 = np.corrcoef(xarr, yarr) # correlation matrix for yarr
# R2

R3 = np.corrcoef(xarr, yarr, rowvar=False) # bi-variate correlation between x and y

# curve fitting

p = np.poly1d([1, 2, 3])
p
print(p)
p(0.5) # if x = 0.5
p.r # roots
p.c # coefficients

## interpolation

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(x, y, 3)
# z

p = np.poly1d(z)
p(0.5)

 



             
