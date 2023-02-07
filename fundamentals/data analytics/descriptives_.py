def myMean(x):
	return sum(x)/float(len(x))

def myVar(x):
    ss = sum([(i-myMean(i))**2 for i in x])
    return float(ss)/(len(x) - 1)
