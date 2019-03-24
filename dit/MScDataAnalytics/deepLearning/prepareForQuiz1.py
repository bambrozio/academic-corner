#%%
import numpy as np
a1 = np.array([2,1,2])
a2 = np.array([4,4,4])
np.dot(a1, a2)

#%%
m1 = np.matrix('2 3; 4 5')
print(m1)
m2 = np.matrix('2 3; 4 5')
print(m2)
print(np.matmul(m1, m2))

#%%
i = np.identity(2)
print(i)
print(np.matmul(m1, i))
print(np.matmul(i, m1))

#%%
np.arange(3, 8, 0.1)

#%%
m1 = np.matrix('2 3; 4 5')
print(m1)
print(m1.T)

#%%
print(np.ravel(m1))
print(np.vstack(m1))

#%%
np.exp(np.array([2,3,4]))

#%%
np.ones(10)

#%%
Y = np.array([0, 1, 1, 0])
X1 = np.array([0,0,1,1])
X2 = np.array([0,1,0,1])
X3 = np.array([0,1,0,1])
X = np.vstack((X1, X2, X3)).T 
print(X)

#%%
X1 = np.array([3,0,1,0,-3,-9,1])
X2 = np.array([1,2,5,0,-2,9,-10])
print(np.maximum(X1, X2))
print(np.minimum(X1, X2))
