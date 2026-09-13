#!/usr/bin/env python
# coding: utf-8
"""Design Matrices with Python, patsy and statsmodels

Author:  Polina Lemenkova
ORCID:   https://orcid.org/0000-0002-5759-1089
Archive: https://doi.org/10.13140/RG.2.2.14575.89764
License: MIT

See README.md for details.
"""
from __future__ import print_function

import os

# %matplotlib inline
import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices

os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv("Tab-Morph.csv")
df = df.dropna()
df[-10:]

y, X = dmatrices('profile ~ sedim_thick + igneous_volc + slope_angle',
                 data=df, return_type='dataframe')
y[:7]
X[:7]
