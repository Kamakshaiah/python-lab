# t tests

## simulations

sales1 = np.random.random_sample(30)*100
salesdf = pd.DataFrame({'sales 1': sales, 'salse 2': sales1})
print(salesdf)
salesdf.dtypes
##salesdf.ndim # 2
##salesdf.size # 60
##salesdf.columns
print(salesdf['sales 1'])

# tests
sp.stats.ttest_1samp(salesdf['sales 1'], 0) # TtestResult(statistic=10.126717188075688, pvalue=4.955969674492966e-11, df=29)
sp.stats.ttest_ind(salesdf['sales 1'], salesdf['sales 2']) # Ttest_indResult(statistic=0.9653598949889254, pvalue=0.3383726024299203)
sp.stats.ttest_rel(salesdf['sales 1'], salesdf['sales 2']) # TtestResult(statistic=0.8397628256700137, pvalue=0.4079113629817226, df=29)
