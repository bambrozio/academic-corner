#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:05:29 2019

@author: bambrozi
"""

import pandas as pd
df = pd.read_csv('github.com/bambrozio/academic-corner/dit/MScDataAnalytics/machineLearning/w2/iris.csv')
from sklearn.decomposition import PCA
pca = PCA()
orig = df.drop('Species', axis = 'columns')
pcs = pca.fit_transform(orig)
pca.components_

pca.explained_variance_ratio_

# Let's say I want only the first 2
pca = PCA(n_components=2)
reduced = pca.fit_transform(orig)
recovered = pca.inverse_transform(reduced)
import numpy as np
np.allclose(recovered, orig)

from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
pcs = pca.fit_transform(x)
import matplotlib.pyplot as plt
plt.figure(figsize = (10, 4))
plt.plot(pcs[y==0, 0], pcs[y==0, 1], 'ro', label = "Setosa")
plt.plot(pcs[y==1, 0], pcs[y==1, 1], 'go', label = "Versicolor")
plt.plot(pcs[y==2, 0], pcs[y==2, 1], 'bo', label = "Virginica")