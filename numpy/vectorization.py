# along axis

b = np.array([[8,1,7], [4,3,9], [5,2,6]])

np.apply_along_axis(sorted, 0, b)
np.apply_along_axis(sorted, 1, b)
np.apply_along_axis(np.diag, -1, b)

a = np.arange(24).reshape(2,3,4)

def my_func(a):
    """Average first and last element of a 1-D array"""
    return (a[0] + a[-1]) * 0.5

np.apply_along_axis(my_func, 0, b)
np.apply_along_axis(my_func, 1, b)

# over axis

a = np.arange(24).reshape(2,3,4)

np.apply_over_axes(np.sum, a, [0,2])
np.sum(a, axis=(0,2), keepdims=True) # same

# vectorize

def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"

    if a > b:
        return a - b
    else:
        return a + b

vfunc = np.vectorize(myfunc)
vfunc(range(1, 10), 5)
out = vfunc([1, 2, 3, 4], 2)
type(out[0]) # <class 'numpy.int32'>
vfunc = np.vectorize(myfunc, otypes=[float])
out = vfunc([1, 2, 3, 4], 2)
type(out) # <class 'numpy.ndarray'>
type(out[0]) # <class 'numpy.float64'>
