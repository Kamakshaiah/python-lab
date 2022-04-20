def computeIQR(v1):
    ''' Computes Inter Quartile Range (IQR) for word's frequency - input should be univariate distribution '''

    from scipy import stats
    stat = stats.iqr(v1, axis=0)
    return stat


    
def twoSampleIndTTest(v1, v2):
    ''' Performs two sample ind. T Test for two different samples - for termmat and distinctwords distributions '''
    
    from scipy import stats
    res = stats.ttest_ind(v1, v2)
    return res

def moodsTest(v1, v2, ties=True):
    ''' Performs moods test for two different serach phrases '''

    from scipy.stats import median_test
    
 
    if ties:
        try:
            g, p, med, tbl = median_test(v1, v2, lambda_="log-likelihood", ties="above")
        except Exception as e:
            print(e, " occured! Test doesn't work")
    else:
        try:
            g, p, med, tbl = median_test(v1, v2, lambda_="log-likelihood")
        except Exception as e:
            print(e, " occured! Test doesn't work")
            
    return {'g': g, 'p': p, 'med': med, 'tbl': tbl}


def bartlettTest(v1, v2):
        ''' Useful for performing bartletts test of spherecity. Input data should be numerical (may be word frequencies) '''
        from scipy.stats import bartlett

        stat, p = bartlett(v1, v2)
        
        return {'stat': stat, 'p-value': p}

def barChart(self, distinctwords):

    ''' Creates barchart for termmat (TM)/distinct words matrix (DWM)'''

    import matplotlib.pyplot as plt
    keys = list(distinctwords.keys())
    plt.bar(distinctwords[keys[0]], distinctwords[keys[1]])
    plt.xticks(rotation=45)
    plt.show()

def pieChart(self, distinctwords):

    ''' Create Pie chart TM/DWM '''

    import matplotlib.pyplot as plt
    keys = list(distinctwords.keys())
    plt.pie(distinctwords[keys[1]], labels = distinctwords[keys[0]])
    
    plt.show()
    
def boxPlot(data):
    
    ''' Boxplot for data vector(s); supports only pandas dataframe '''
    import matplotlib.pyplot as plt
    
    data.boxplot()
    plt.show()


def reshapeData(data):
    ''' Reshapes input data into required format for cluster analysis '''
    import numpy as np

    idx = list(data.keys())[1]

    out = np.reshape(data[idx], (1, -1)).T

    return out


def clusterAnalysis(data, path, nc=2, output=False):
    ''' Performs cluster analysis on input data.
        data - a dictionary such as TM or DWM
        nc - num of clusters
        path - path for output file (default name out.csv
        output = True makes output to file path '''

    from sklearn import cluster
    from sklearn import metrics
    import pandas as pd
    import numpy as np
    
    idx0 = list(data.keys())[0]
    idx1 = list(data.keys())[1]

    req_data = np.reshape(data[idx1], (1, -1)).T
           
    kmeans = cluster.KMeans(n_clusters=nc)
    kmeans.fit(req_data)

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    kmeansclus = pd.DataFrame({'words': data[idx0], 'freq': data[idx1], 'labels':list(labels)})

    pathch = path + 'out.csv'

    if output:
        kmeansclus.to_csv(pathch)
        
    score = kmeans.score(req_data)
    silhouette_score = metrics.silhouette_score(req_data, labels, metric='euclidean')

    out = {'labels': labels, 'centroids': centroids, 'score': score, 'silhouette_score': silhouette_score}
    return out

def wordsByCategory(file_path, nclus):
    ''' Reads data from file system (file_path) and makes cluster wise words.
        Output has a dictionary with cluster number as keys and words as values '''

    import pandas as pd

    clusdata = pd.read_csv(file_path)
    num_clus = list(range(nclus))

    cluswords = {}
    
    for i in num_clus:
        cluswords[i] = clusdata[clusdata.labels == num_clus[i]]['words']

    return cluswords

def pieForCategories(cats):
    ''' Pie chart for categories. Requires cluster wise words (such as created by the method 'wordsByCategory' '''

    import matplotlib.pyplot as plt

    vals = []
    for i in cats.values():
        vals.append(len(i))

    plt.pie(vals, labels=vals)
    plt.show()

def crosstabFromWordsMatrix(file_path, output=False, norm=True):
    ''' Reads data from file system (file_path) and creates cross tabs for further analysis.
        The input file must be an TM/DWM (out.csv).
        Outputs crosstab for words and lables '''
    
    import pandas as pd
    from scipy import stats
    
    dataforctbl = pd.read_csv(file_path)
    ctbl = pd.crosstab(dataforctbl['words'], dataforctbl['labels'], normalize = norm)

    pathch = file_path + 'ctbl.csv'

    if output:
        ctbl.to_csv(pathch)

    out = stats.chi2_contingency(ctbl)

    return {'ctbl': ctbl, 'results': {'chi_sq': out[0], 'p_value': out[1], 'dof': out[2]}}

if __name__ == '__main__':
    import numpy as np
    v1 = np.random.randint(1, 10, 30)
    v2 = np.random.randint(1, 10, 30)
##    print(bartlettTest(v1, v2))
##    print(computeIQR(v1))
    print(moodsTest(v1, v2))
