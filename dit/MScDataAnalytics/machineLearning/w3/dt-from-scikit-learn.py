#%%[markdown]
# # Decision Tree with Scikit-learn
# Got from: https://scikit-learn.org/stable/modules/tree.html#tree
#
#As with other classifiers, DecisionTreeClassifier takes as input two arrays: an array X, sparse or dense, of size [n_samples, n_features] holding the training samples, and an array Y of integer values, size [n_samples], holding the class labels for the training samples:

#%%
from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

#%%[markdown]
# After being fitted, the model can then be used to predict the class of samples:

#%%
clf.predict([[2., 2.]])

#%%[markdown]
# Alternatively, the probability of each class can be predicted, which is the fraction of training samples of the same class in a leaf:

#%%
clf.predict_proba([[2., 2.]])

#%%[markdown]
# DecisionTreeClassifier is capable of both binary (where the labels are [-1, 1]) classification and multiclass (where the labels are [0, …, K-1]) classification.
#
# Using the Iris dataset, we can construct a tree as follows:

#%%
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

#%%[markdown]
# Once trained, we can export the tree in Graphviz format using the export_graphviz exporter. If you use the conda package manager, the graphviz binaries and the python package can be installed with
#
# `conda install python-graphviz`
# 
# Alternatively binaries for graphviz can be downloaded from the graphviz project homepage, and the Python wrapper installed from pypi with pip install graphviz.
#
# Below is an example graphviz export of the above tree trained on the entire iris dataset; the results are saved in an output file iris.pdf:

#%%
import graphviz 
import os
os.chdir("/Users/bambrozi/workspace/github.com/bambrozio/academic-corner/dit/MScDataAnalytics/machineLearning/w3/")
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") # will create the file iris.pdf

#%%[markdown]
# The export_graphviz exporter also supports a variety of aesthetic options, including coloring nodes by their class (or value for regression) and using explicit variable and class names if desired. Jupyter notebooks also render these plots inline automatically:

#%%
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=iris.feature_names,  
                     class_names=iris.target_names,  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph