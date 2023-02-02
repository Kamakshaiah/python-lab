def twoWayAnovaSS(vector, factor1, factor2):
    ''' Calcualtes SS_Between, SS_Within, SS_Total measures for Two Way Anova.
        Inputs:
            Vector: a numeric vector
            Factors: a numeric vectors with categories
        Outputs:
            SS_Between
            SS_Within
            SS_Total '''
    import pandas as pd

    data = pd.DataFrame({'vector': vector, 'factor1': factors[0], 'factor2':factors[1]})

    data.factor1 = pd.Categorical(data.factor1)
    data['factor1'] = data.factor1.cat.codes

    data.factor2 = pd.Categorical(data.factor2)
    data['factor2'] = data.factor2.cat.codes

    return(data.head())
