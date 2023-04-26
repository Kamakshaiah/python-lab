# https://pypi.org/project/factor-analyzer/

# pip install factor_analyzer

# EFA

import pandas as pd
from factor_analyzer import FactorAnalyzer

df_features = pd.read_csv('tests/data/test02.csv')
fa = FactorAnalyzer(rotation=None)

fa.fit(df_features)

FactorAnalyzer(bounds=(0.005, 1), impute='median', is_corr_matrix=False,
               method='minres', n_factors=3, rotation=None, rotation_kwargs={},
               use_smc=True)

fa.loadings_

fa.get_communalities()

# CFA

from factor_analyzer import (ConfirmatoryFactorAnalyzer, ModelSpecificationParser)

df_features = pd.read_csv('tests/data/test11.csv')

model_dict = {"F1": ["V1", "V2", "V3", "V4"], "F2": ["V5", "V6", "V7", "V8"]}

model_spec = ModelSpecificationParser.parse_model_specification_from_dict(df_features, model_dict)
cfa = ConfirmatoryFactorAnalyzer(model_spec, disp=False)
cfa.fit(df_features.values)

cfa.loadings_
cfa.factor_varcovs_
cfa.transform(df_features.values)
