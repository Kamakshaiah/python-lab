def myMean(x):
    ''' calculates arithmetic mean '''
    return sum(x)/float(len(x))

def myMedian(x):
    ''' calculates median '''
    n = len(x) 
    x.sort() 
  
    if n % 2 == 0: 
        median1 = x[n//2] 
        median2 = x[n//2 - 1] 
        return((median1 + median2)/2)
    else: 
        median = x[n//2]
        return("Median is: " + str(median)) 

def myMode(x):
    ''' calculates mode '''
    from collections import Counter 
  
    n = len(x) 
  
    data = Counter(x) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
    if len(mode) == n: 
        get_mode = "No mode found"
        return(get_mode)
    else: 
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
        return(get_mode) 
