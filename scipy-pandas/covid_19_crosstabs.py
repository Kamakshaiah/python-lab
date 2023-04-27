# covid 19

remdesvir = np.random.choice([0, 50, 100], 30, replace = True)
remdesvir
azithromycin = np.random.choice([0, 50, 100], 30, replace = True)
effect = np.random.choice(['yes', 'no'], 30, replace = True)
covid_19_treatment = pd.DataFrame({'remdesvir':remdesvir, 'azithromycin': azithromycin, 'effect': effect})
covid_19_treatment.head()
covid_19_treatment.groupby('effect').count()
covid_19_treatment.groupby('effect').mean()
covid_19_treatment.groupby('effect').get_group('yes')
covid_19_treatment.groupby('effect').get_group('no')

pd.crosstab(covid_19_treatment.remdesvir, covid_19_treatment.azithromycin)
sp.stats.chi2_contingency(pd.crosstab(covid_19_treatment.remdesvir, covid_19_treatment.azithromycin)) # Chi2ContingencyResult(statistic=4.155917159763314, pvalue=0.38531580762893597, dof=4, expected_freq=array([[5.2       , 4.        , 2.8       ],        [2.16666667, 1.66666667, 1.16666667],        [5.63333333, 4.33333333, 3.03333333]])) 

ct = pd.crosstab([df['remdesvir'], df['azythromycin']], df['effect'])
sp.stats.chi2_contingency(ct)
