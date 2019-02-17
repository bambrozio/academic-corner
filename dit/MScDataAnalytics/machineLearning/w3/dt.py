#%% 
from sklearn.tree import DecisionTreeClassifier

from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
cancer
#%% 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(cancer, cancer.target, stratify = cancer.target, random_state = 42)

tree = DecisionTreeClassifier()
tree = DecisionTreeClassifier()

tree.fit(X_train, y_train)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')

tree.score(X_train, y_train)
tree.score(X_train, y_train)
1.0

tree.score(X_test, y_test)
tree.score(X_test, y_test)
0.9370629370629371

tree = DecisionTreeClassifier(random_state=0)

tree.fit(X_train, y_train)
tree.fit(X_train, y_train)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=0,
            splitter='best')

tree.score(X_train, y_train)
tree.score(X_train, y_train)
1.0

tree.score(X_test, y_test)
tree.score(X_test, y_test)
0.9370629370629371

tree = DecisionTreeClassifier(max_depth=3)

tree.fit(X_train, y_train)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')

tree.score(X_train, y_train)
0.9765258215962441

tree.score(X_test, y_test)
0.9440559440559441

from sklearn.tree import export_graphviz

import graphviz

from sklearn.datasets import load_breast_cancer
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(cancer.data, cancer.target)

dot_data = tree.export_graphviz(clf, out_file=None) 

graph = graphviz.Source(dot_data)

graph.render("cancer")
graph.render("cancer")
'cancer.pdf'

export_graphviz(clf, out_file = "tree.dot")

export_graphviz(clf, out_file = "tree.dot", feature_names = cancer.feature_names)

graph.render("cancer")
'cancer.pdf'
