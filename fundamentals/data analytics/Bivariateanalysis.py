def twoWayAnovaSS(vector, factor1, factor2):
    ''' Calcualtes SS_Between for given factors and SS_Total for Two Way Anova.
        Inputs:
            Vector: a numeric vector
            Factors: a numeric vectors with categories
        Outputs:
            SS_Between
            SS_Total '''
    import pandas as pd

    data = pd.DataFrame({'vector': vector, 'factor1': factor1, 'factor2':factor2})

    data.factor1 = pd.Categorical(data.factor1)
    data['factor1'] = data.factor1.cat.codes

    data.factor2 = pd.Categorical(data.factor2)
    data['factor2'] = data.factor2.cat.codes

    gm = data['vector'].mean()

    ss_fact1 = sum([(data[data.factor1 ==l].vector.mean()-gm)**2 for l in data.factor2])
    ss_fact2 = sum([(data[data.factor2 ==l].vector.mean()-gm)**2 for l in data.factor1])

    ss_t = sum((data.vector - gm)**2)

    return({'ssa': ss_fact1, 'ssb': ss_fact2, 'sst': ss_t})

def factorCategoriesData(vector, factor1, factor2):

    ''' Return factor level data for factor 1 '''

    import pandas as pd

    data = pd.DataFrame(dict(vector=vector, factor1=factor1, factor2=factor2))

    factor1levels = data['factor1'].unique()
    catData = []
    for i in factor1levels:
        catData.append(pd.DataFrame(data[data['factor1'] == i]))

    return(catData)

def factorialMeans(catData):

    ''' Return factor level means for factor 2 '''

    import pandas as pd

    fact2means = []

    for i in range(len(catData)):
        fact2means.append(pd.DataFrame(catData[i][catData[i].factor2 == d].vector.mean() for d in catData[i].factor2))

    return(fact2means)

def sumSqPadasVars(var1, var2):

    ''' Utility function to make sum of squares for Two Way Anova '''

    import pandas as pd
    
    var1 = var1.to_list()
    var2 = var2[var2.columns[0]].to_list()

    sumSq = []
    for i, j in zip(var1, var2):
        sumSq.append((i - j)**2)
    return(sumSq)

def twoWayAnovaSSWithin(factor1levels, fact2means):

    ''' Return SS_Within for
        Inputs:
            Factor levels data for factor 1
            Factor means for factor 2

        Output:
            SS_Within value '''
            
    out = 0
    for i in range(len(factor1levels)):
        out += sum(sumSqPadasVars(factor1levels[i].vector, fact2means[i]))

    return(out)

def twoWayAnovaSSInt(sst, ssa, ssb, ssw):
    ''' Returns SS_Interaction for factor A and factor B '''

    ss_int = sst-ssa-ssb-ssw

    return(ss_int) 

def twoWayAnovaSSs(vector, factor1, factor2):

    ''' Returns all SSs for
        Inputs:
            Vector: dependent variable (numeric)
            Factor 1: independent factor (numeric)
            Factor 2: independent factor (nemeric)
        Output:
            All SSs
            '''

    import pandas as pd
    data = pd.DataFrame({'vector': vector, 'factor1': factor1, 'factor2':factor2})

    ssa = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['ssa']
    ssb = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['ssb']
    sst = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['sst']

    factorleveldata = factorCategoriesData(data['vector'], data['factor1'], data['factor2'])
    fact2means = factorialMeans(factorleveldata)

    ssw = twoWayAnovaSSWithin(factorleveldata, fact2means)
    ssi = twoWayAnovaSSInt(sst, ssa, ssb, ssw)

    return({'ssa':ssa, 'ssb':ssb, 'ssi': ssi, 'sst':sst, 'ssw':ssw})

def twoWayAnovaMSs(vector, factor1, factor2):

    ''' '''
    import pandas as pd
    data = pd.DataFrame({'vector': vector, 'factor1': factor1, 'factor2':factor2})

    N = len(data.vector)
    df_a = len(data.factor1.unique()) - 1
    df_b = len(data.factor2.unique()) - 1
    df_int = df_a * df_b
    df_w = N - (len(data.factor1.unique())*len(data.factor2.unique()))

    ssa = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['ssa']
    ssb = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['ssb']
    sst = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['sst']

    factorleveldata = factorCategoriesData(data['vector'], data['factor1'], data['factor2'])
    fact2means = factorialMeans(factorleveldata)

    ssw = twoWayAnovaSSWithin(factorleveldata, fact2means)

    ssint = twoWayAnovaSSInt(sst, ssa, ssb, ssw)

    msa = ssa/df_a
    msb = ssb/df_b
    msint = ssint/df_int
    msw = ssw/df_w

    return({'msa': msa, 'msb':msb, 'msint':msint, 'msw':msw})

def twoWayAnova(vector, factor1, factor2):

    import pandas as pd
    data = pd.DataFrame({'vector': vector, 'factor1': factor1, 'factor2':factor2})
    
    msa = twoWayAnovaMSs(data['vector'], data['factor1'], data['factor2'])['msa']
    msb = twoWayAnovaMSs(data['vector'], data['factor1'], data['factor2'])['msb']
    msi = twoWayAnovaMSs(data['vector'], data['factor1'], data['factor2'])['msint']
    msw = twoWayAnovaMSs(data['vector'], data['factor1'], data['factor2'])['msw']

    f_a = msa/msw
    f_b = msb/msw
    f_i = msi/msw

    return({'f_a': f_a, 'f_b': f_a,'f_i': f_i,})

def twoWayAnova(vector, factor1, factor2):

    import scipy.stats as stats
    import pandas as pd
    data = pd.DataFrame({'vector': vector, 'factor1': factor1, 'factor2':factor2})

    N = len(data.vector)
    df_a = len(data.factor1.unique()) - 1
    df_b = len(data.factor2.unique()) - 1
    df_i = df_a * df_b
    df_w = N - (len(data.factor1.unique())+len(data.factor2.unique()))

    ssa = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['ssa']
    ssb = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['ssb']
    sst = twoWayAnovaSS(data['vector'], data['factor1'], data['factor2'])['sst']

    factorleveldata = factorCategoriesData(data['vector'], data['factor1'], data['factor2'])
    fact2means = factorialMeans(factorleveldata)

    ssw = twoWayAnovaSSWithin(factorleveldata, fact2means)

    ssi = twoWayAnovaSSInt(sst, ssa, ssb, ssw)

    msa = ssa/df_a
    msb = ssb/df_b
    msi = ssi/df_i
    msw = ssw/df_w

    f_a = msa/msw
    f_b = msb/msw
    f_i = msi/msw

    p_a = stats.f.sf(f_a, df_a, df_w)
    p_b = stats.f.sf(f_b, df_b, df_w)
    p_i = stats.f.sf(f_i, df_i, df_w)

    results = {'df': [df_a, df_b, df_i, df_w],
               'sum_sq': [ssa, ssb, ssi, ssw],
               'mean_sq': [msa, msb, msi, msw],
               'F': [f_a, f_b, f_i, None],
               'PR(>F)': [p_a, p_b, p_i, None]}
    columns = ['df', 'sum_sq', 'mean_sq', 'F', 'PR(>F)']
    aov_table = pd.DataFrame(results, columns = columns, index = ['a', 'b', 'axb', 'Resid.'])
    return(aov_table) 
    

def expectedFreq(m):

    ''' Calculates expected frequencies for given input matrix 'm' '''

    import Pythonprogramming as pp

    rs = pp.rowSums(m)
    cs = pp.colSums(m)

    data = pp.matrixMultiplication(pp.matrixTranspose([rs]), [cs])

    out = sum(data, [])

    exmat = []
    for i in out:
        exmat.append(i/sum(rs))
    rows = len(data)
    cols = len(data[0])

    ll = []
    ul = []

    for i in range(rows):
        ll.append(i*cols)

    for i in ll:
        ul.append(i+cols)
    res = []

    for i, j in zip(ll, ul):
        res.append(exmat[i:j])

    return(res) 

def chiContingency(m):

    ''' Calculates chisquare statistic for given matrix 'm' '''

    import Pythonprogramming as pp
    
    ef = expectedFreq(m)
    diff = pp.matrixSubtraction(m, ef)

    ominusesqure = pp.matPower(diff, 2)
    chibe = pp.matrixDivision(ominusesqure, ef)
    chistat = sum(sum(chibe, []))

    rows = len(m)
    cols = len(m[0])

    dof = (rows-1)*(cols-1)

    return({'chisq-statistic': chistat, 'dof': dof}) 

def oddsRatio(m):

    ''' Calculates odds ratio for input matrix 'm' '''

    import Pythonprogramming as pp
    numer = pp.Product(pp.Diagonals(m)['diagonal'])
    denom = pp.Product(pp.Diagonals(m)['rev-diagonal'])
    return(numer/denom)

def phiCoef(m):

    ''' Calculates phi coefficient for 2 X 2 cross tab for input matrix 'm' '''

    chistat = chiContingency(m)['chisq-statistic']
    n = sum(m[0])+sum(m[1])
    phi = (chistat/n)**0.5
    return(phi)

def crammersCandV(m, *args):

    ''' Computes Crammer's C and V for symmetric and non-symmetric matrix of 'm'  '''
        
    chistat = chiContingency(m)['chisq-statistic']
    dof = chiContingency(m)['dof']
    n = sum(m[0])+sum(m[1])
    k = min(len(m), len(m[0]))

    r = len(m)
    c = len(m[0])

    cstat = (chistat/(n + chistat))**0.5

    if '2x2' in args:
        C = cstat/(((k - 1)/k)*0.5)
        
    else:
        C = cstat/((((r-1)/r)+((c-1)/c))**(1/4))

    V = (chistat/(n*(k - 1)))*0.5

    return({'C': C, 'V': V})

def gammaTest(vec1, vec2):

    ''' Computes GK Gamma (G) for given input vectors '''

    n = len(vec1)
    cp = sum([i == j for i, j in zip(vec1, vec2)])
    dp = n - cp

    g = (cp-dp)/(cp+dp)

    t = g*((cp+dp)/(n*(1-g**2)))**2

    return({'G': g, 'T Stat': t})
    
def yulesQ(m):

    ''' Calculates Yules' Q for 2 X 2 input matrix '''

    odds = oddsRatio(m)

    q = (odds - 1)/(odds + 1)

    return(q) 

def kendallsTau(vec1, vec2):

    ''' Return Kendalls' Tau for input vectors '''

    n = len(vec1)
    cp = sum([i == j for i, j in zip(vec1, vec2)])
    dp = n - cp

    tau = (2/(n*(n-1)))*(cp - dp)

    z = (3*(cp - dp))/((n*(n-1)*(2*n + 5))/2)**0.5

    return({'T': tau, 'Z Statistic': z}) 

           
def correlCoef(x, y):

    ''' Calculates Karl Pearson's r for x, y '''

    import Descriptives as dsc

    n = len(x) or len(y) 

    r = dsc.CoVar(x, y)/(dsc.Std(x) * dsc.Std(y))
    t = r *((n - 2)/(1 - r**2))**0.5

    return({'r':r, 't': t})

def spearmanRho(x, y):

    ''' Calculates spearman rho for x, y input variables '''

    import Pythonprogramming as pyp
    
    xs = pyp.rankData(x)
    ys = pyp.rankData(y)

    n = len(x) or len(y)

    ds = [(i-j)**2 for i, j in zip(xs, ys)]

    sr = 1 - (6 * sum(ds))/(n * (n**2 - 1))

    return(sr)

def Slope(x, y):

    ''' Computes beta 1 for input variables x, y '''

    import Descriptives as dsc

    slope = dsc.CoVar(x, y)/dsc.Var(x)

    return(slope) 

def Intercept(x, y):

    ''' Computes beta 0 for input variables x, y '''

    import Descriptives as dsc
    
    b1 = Slope(x, y)
    b0 = dsc.Mean(y) - (b1 * dsc.Mean(x))

    return(b0)


def regEstimates(x, y):

    ''' Computes beta 0, beta 1 for input variables x, y '''

    b1 = Slope(x, y)
    b0 = Intercept(x, y)

    return({'b0':b0, 'b1': b1})

def fitValues(x, y):

    ''' Computes fit/predicted values for x, y '''

    b0 = Intercept(x, y)
    b1 = Slope(x, y)

    fitvals = [b0 + (b1 * i) for i in x]

    return(fitvals)

def regSSs(x, y):

    import Descriptives as dsc

    ''' Computes all sums of squares for regression model for x, y '''

    sse = sum([(i - j)**2 for i, j in zip(y, fitValues(x, y))])
    ssr = sum([(i - dsc.Mean(y))**2 for i in fitValues(x, y)])
    sst = sum([(i - dsc.Mean(y))**2 for i in y])

    return({'sse':sse, 'ssr':ssr, 'sst':sst})

def regMSs(x, y):

    ''' Calculates mean squared errors for simple linear regression between x, y '''

    ssm = regSSs(x, y)['ssr']
    sse = regSSs(x, y)['sse']
    sst = regSSs(x, y)['sst']

    p = 2
    n = len(x) or len(y)
    
    dfm = p -1
    dfe = n - p
    dft = n - 1

    msm = ssm/dfm
    mse = sse/dfe

    f = msm/mse

    return(f)

def coefDeter(x, y):

    ''' Calculates r^2 value for x, y variables '''

    rsq = 1 - (regSSs(x, y)['ssr']/regSSs(x, y)['sst'])

    return(rsq)

def regSignificanceTests(x, y):

    import Descriptives as dsc

    ''' Performs significance tests for b_0 and b_1 '''
    n = len(x) or len(y)
    
    b0 = Intercept(x, y)
    b1 = Slope(x, y)
    
    sigmab1 = regSSs(x, y)['sse']*(1/(dsc.Var(x)))**0.5
    sigmab0 = regSSs(x, y)['sse']*((1/n)+(dsc.Mean(x)**2/dsc.Var(x)))**0.5

    tb0 = b0/sigmab0
    tb1 = b1/sigmab1

    return({'tb0': tb0, 'tb1': tb1})
    
    
def regFit(x, y):

    ''' Calculates R^2 and F Statistic for linear regression '''

    rsq = coefDeter(x, y)
    f = regMSs(x, y)

    return({'rsq': rsq, 'F': f})
    
    
def logOddsLR(x, y):

    ''' Calculates log-odds for x, y '''

    b0 = Intercept(x, y)
    b1 = Slope(x, y)

    log_odds = [b0 + (b1 * i) for i in x]

    return(log_odds)

def oddsLR(x, y):

    ''' Calculates odds ratio for x, y '''
    import math
    
    b0 = Intercept(x, y)
    b1 = Slope(x, y)
    odds = [math.exp(b0+(b1 * i)) for i in x]

    return(odds)

def probsLR(x, y):

    ''' Calculates probabilities for x, y '''

    import math
    
    b0 = Intercept(x, y)
    b1 = Slope(x, y)

    probs = [1/(1+math.exp(b0+(b1 * i))) for i in x]

    return(probs)

def logitLR(x, y):

    ''' Calculates log-odds, odds, and probabilities for x, y '''

    logOdds = logOddsLR(x, y)
    odds = oddsLR(x, y)
    probs = probsLR(x, y)

    return({'log-odds': logOdds, 'odds': odds, 'probs': probs})
    
