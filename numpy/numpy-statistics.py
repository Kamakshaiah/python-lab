import numpy as np
##print(np.random.rand(3,2))
##print(np.random.randint(100, size=10))

data = np.random.randint(10, size=20).reshape(5, 4)
print(data)
print(np.mean(data, axis=1))
print(np.median(data, axis=1))
print(np.max(data, axis=1))
##print(np.apply_along_axis(np.mean, 1, data))
##print(np.apply_along_axis(np.std, 1, data))
##print(np.apply_along_axis(np.var, 1, data))
