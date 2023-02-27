
def arithmeticmean(x):
    return sum(x)/len(x)

def geometricmean(x):
    import functools
    out_ = functools.reduce(lambda i, j: i * j, x)
    return out_**(1/len(x))

def harmonicmean(x):
    numer = len(x)
    denom = sum([1/i for i in x])
    return numer/denom

if __name__ == '__main__':
    print(arithmeticmean(range(1, 10)))
    print(geometricmean(range(1, 10)))
    print(harmonicmean(range(1, 10)))
