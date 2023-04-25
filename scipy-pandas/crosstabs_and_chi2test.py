# numerical to categorical

import numpy as np
##np.random.random_sample(10)*100 # decimal data
salary = np.random.randint(20, 100, 30) # integer data
print(salary)

import pandas as pd
sal_cat = pd.cut(salary, [0, 25, 50, 75, 100], labels=['0 to 25', '25 to 50', '50 to 75', '75 to 100'])
for i in sal_cat:
    print(i)

gender = np.random.choice(['male','female'], 30, replace=True)
print(gender)

df = pd.DataFrame({'gender': gender, 'salary': sal_cat})
df.dtypes
pd.crosstab(df['gender'], df['salary'])

# other crosstabs (using groupby function)

df.groupby('gender').count() # gender wise table for df
df.groupby('gender').mean() # gender wise table for numeric vars in df

df.groupby('gender').get_group('male').count()
df.groupby('gender').get_group('female').count()

df.groupby('gender').get_group('male')
df.groupby('gender').get_group('female')

import scipy as sp
sp.stats.chi2_contingency(pd.crosstab(df['gender'], df['salary']))


# categorical to numerical

df['gender'].replace(['male', 'female'], [0, 1], inplace=True)
print(df)



sp.stats.ttest_1samp(df.gender, 0) # popmean = 0

df['gender'].replace([0, 1], ['male', 'female'], inplace=True)
print(df)
