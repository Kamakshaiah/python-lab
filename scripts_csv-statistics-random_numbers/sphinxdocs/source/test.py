def Mean(vec):

    ''' return arithmetic mean '''

    return sum(vec)/len(vec)

def summaryStatistics(vec, *args, **kwargs):
    ''' this function returns summary statistics as by the request of the user
        avg = True : average
        min = True : minimum
        max = True : maximum '''

    for arg in args:
        print(arg)

    if 'mean' in kwargs:
        print(Mean(vec))
    if 'minimum' in kwargs:
        print(min(vec))
    if 'maximum' in kwargs:
        print(max(vec))


def summaryStatisticsSwitchDemo(vec, stat):

    ''' this function is useful to compute summary statitics using switch dict in python '''

    summaries={

        'mean' : Mean(vec),
        'minimum' : min(vec),
        'maximum' : max(vec)
        }

    return summaries.get(stat)

    
