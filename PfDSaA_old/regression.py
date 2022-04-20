# regression

def mean(x):

    ''' this function returns arithmetic mean of the given vector '''

    return(sum(x)/len(x))

def dev(x):

    ''' this function returns deviation of the given vector '''

    dev_x = sum([(i - mean(x)) for i in x])

    return(dev_x)

def mean_dev(x):

    ''' this function returns mean deviation of the given vector '''

    dev_x = sum([(i - mean(x)) for i in x])
    return(dev_x/len(x))

def sum_prod(x, y):

    ''' this function returns sum of the product of deviations of the any two vectors '''
    
    dev_x = [(i - mean(x)) for i in x]
    dev_y = [(i - mean(y)) for i in y]

    return(sum(list(map(lambda x, y: x *y, dev_x, dev_y))))

def sum_squared_dev(x):

    ''' this function returns sum of the squared deviations of the given vector '''
    
    m = mean(x)

    return(sum([(i - m)**2 for i in x]))

def sum_squares(x):

    ''' this function returns sum of the squares for given vector '''

    return(sum([i**2 for i in x]))
    
def var(x):

    ''' this function returns variance of the given vector '''

    dev = [i-mean(x) for i in x]
    sum_sq = sum([i**2 for i in dev])
    return(sum_sq/len(x))

def stdev(x):
    ''' this function returns standard deviation of the given vector '''
    return(var(x)**0.5)
        
def covar(x, y):
    ''' this function returns covariance of any two given vectors '''

    return(sum_prod(x, y)/(len(x) - 1))

def slope(x, y):

    ''' this function return slope for any two given vectors '''
    
    numer = sum_prod(x, y)
    denom = sum_squared_dev(x)

    return(numer/denom)

def intercept(x, y):

    ''' this function return intercept of the given vectors '''

    y_bar = mean(y)
    x_bar = mean(x)

    inter = y_bar - (slope(x, y) * x_bar)

    return(inter)

def fit_values(x, y):

    ''' this function returns fitted values for given regression fit '''

    fv = [intercept(x, y) - (slope(x, y) * i ) for i in range(len(x))]

    return(dict(sum = sum(fv), fit_vals = fv))

def SSR(x, y):

    ''' this function returns regression sum of squares for given regression fit '''

    return(fit_values(x, y)['sum']/(len(x)- 2))

def SSE(x, y):

    ''' this function returns sum of squares for error variable for given regression fit '''
    fv = fit_values(x, y)['fit_vals']

    return(sum(list(map(lambda i, j: (i - j)**2, y, fv))))


def sigma_e(x, y):

    ''' this function returns error variance for given variables '''

    numer = SSR(x, y)
    denom = len(x) - 2

    return(numer/denom)

def sigma_b1(x, y):

    ''' this function return se for beta one '''

    se = sigma_e(x, y)

    ss = sum_squared_dev(x)

    return(se * (1/ss)**0.5)

def sigma_b0(x, y):

    ''' this function returns se for beta zero '''

    b1 = sigma_b1(x, y)
    m2 = (sum_squares(x)/len(x)**0.5)

    return(b1/m2)

def beta_test(x, y):

    ''' this function returns t statistics for given variables '''

    b0 = intercept(x, y)
    b1 = slope(x, y)

    s1 = sigma_b0(x, y)
    s2 = sigma_b1(x, y)

    t1 = b0/s1
    t2 = b1/s2

    return({'t1':t1, 't2':t2})

def r_squared(x, y):

    ''' this function returns R^2 value for given variables '''

    sse = SSE(x, y)
    ssr = SSR(x, y)

    r_s = 1-(ssr/(ssr+sse))

    return(r_s)

