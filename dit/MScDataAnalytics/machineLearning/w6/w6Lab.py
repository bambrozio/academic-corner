#%%[markdown]
# Q3) Using Scikit Learn load the built-in boston regression dataset.
# a) Set aside 20% of the data as a final test set.
from sklearn.datasets import load_boston
boston = load_boston()
print(boston.data.shape)