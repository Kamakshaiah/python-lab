def paratovar(n, a):
    import random
    x = []
    for i in range(n):
        x.append(random.paretovariate(a))
    return(x)
