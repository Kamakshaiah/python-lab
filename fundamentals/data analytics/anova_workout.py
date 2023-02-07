# https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/

import pandas as pd
import Simulations as sml
import scipy.stats as stats

data = sml.simHetDat(30, 'all')
data.rename(columns={'numeric':'sal'}, inplace = True)

grps = pd.unique(data.gen.values)
d_data = {grp:data['sal'][data.gen == grp] for grp in grps}

k = len(pd.unique(data.gen))
N = len(data.values)
n = data.groupby('gen').size()[0]

DFbet = k - 1
DFwith = N - k
DFtot = N - 1

SSbet = (sum(data.groupby('gen').sum()['sal']**2)/n) \
    - (data['sal'].sum()**2)/N

sum_y_sq = sum([value**2 for value in data['sal'].values])

SSwith = sum_y_sq - sum(data.groupby('gen').sum()['sal']**2)/n

SStot = sum_y_sq - (data['sal'].sum()**2)/N

MSbet = SSbet/DFbet
MSwith = SSwith/DFwith
F = MSbet/MSwith

p = stats.f.sf(F, DFbet, DFwith)

eta_sqrd = SSbet/SStot
om_sqrd = (SSbet - (DFbet * MSwith))/(SStot + MSwith)

#print(F, p)
#print(d_data)
F, p = stats.f_oneway(d_data['male'], d_data['female'])
#print(F, p)


# --------------------------------------------------------------------------------------
# Two Way ANOVA
#---------------------------------------------------------------------------------------
data.gen = pd.Categorical(data.gen)
data['gender'] = data.gen.cat.codes
data.head()

data.occ = pd.Categorical(data.occ)
data['occupation'] = data.occ.cat.codes
data.head()

gm = data['sal'].mean()
ss_gen = sum([(data[data.gender ==l].sal.mean()-gm)**2 for l in data.occupation])
ss_occ = sum([(data[data.occupation ==l].sal.mean()-gm)**2 for l in data.gender])

#ss_gen = sum((data.groupby('gen').mean()['sal'] - gm)**2)
#ss_occ = sum((data.groupby('occ').mean()['sal'] - gm)**2)

ss_t = sum((data.sal - gm)**2)

male = data[data.gen == 'male']
female = data[data.gen == 'female']
employed = data[data.occ == 'employed']
unemployed = data[data.occ == 'unemployed']

male_occ_means = [male[male.occ == d].sal.mean() for d in male.occ]
female_occ_means = [female[female.occ == d].sal.mean() for d in male.occ]

ss_w = sum((female.sal - female_occ_means)**2) +sum((male.sal - male_occ_means)**2)

ss_genxocc = ss_t-ss_gen-ss_occ-ss_w

# MS

N = len(data.sal)
df_gen = len(data.gen.unique()) - 1
df_occ = len(data.occ.unique()) - 1
df_genxocc = df_gen*df_occ 
df_w = N - (len(data.gen.unique())*len(data.occ.unique()))

ms_gen = ss_gen/df_gen
ms_occ = ss_occ/df_occ
ms_genxocc = ss_genxocc/df_genxocc
ms_w = ss_w/df_w

f_gen = ms_gen/ms_w
f_occ = ms_occ/ms_w
f_genxocc = ms_genxocc/ms_w

p_gen = stats.f.sf(f_gen, df_gen, df_w)
p_occ = stats.f.sf(f_occ, df_occ, df_w)
p_genxocc = stats.f.sf(f_genxocc, df_genxocc, df_w)

results = {'sum_sq':[ss_gen, ss_occ, ss_genxocc, ss_w],
           'df':[df_gen, df_occ, df_genxocc, df_w],
           'F':[f_gen, f_occ, f_genxocc, 'NaN'],
            'PR(>F)':[p_gen, p_occ, p_genxocc, 'NaN']}
columns=['sum_sq', 'df', 'F', 'PR(>F)']
aov_table = pd.DataFrame(results, columns=columns,
                          index=['gen', 'occ', 
                          'gen:occ', 'Residual'])


print(aov_table)
