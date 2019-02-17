#%%[markdown]
# 1 - Create a Jupyter notebook called "Week 03 work"

#%%[markdown]
# 2 - Print "Hello network"
print("Hello network")

#%%[markdown]
# 3 - ... creates an array with the integers 0 to 9, and print it
arr = range(10)
list(arr)

#%%[markdown]
# 4 - ... creates a numpy vector with the integers 0 to 9 and print it
import numpy as np
npArr = np.array(arr)
npArr

#%%[markdown]
# 5 - ... print out with a loop the cube of each element in the array created in item 3
for val in arr:
    print(val**3)

#%%[markdown]
# 6 - ... print out the cube of each element in the vector created in item 4... using vector notation
npArr**3

#%%[markdown]
# 7 - write a function name my_fun that takes 2 args as input. Assumes the first item is a vector and the second is a scalar. The function should return a new vector wich is the vector raised to the power of the scalar. Test it by printing restults.
def my_fun(vector, scalar):
    return vector**scalar

my_fun(npArr, 2)

#%%[markdown]
# 8 - ...write a function named my_fun2. Input: single numpy vector, and returns sum of the squares of that vector. Test with [1,1,1,1] and [2,2,2,2]
def my_fun2(npVector):
    return np.sum(npVector**2)

print(my_fun2(np.array([1,1,1,1])))
print(my_fun2(np.array([2,2,2,2])))

#%%[markdown]
# 9 - Write a function that takes as input a vector and a scalar... Return the sum of the square of the difference btw each individual item and the scalar. Test it
def my_fun3(vector, scalar):
    return np.sum((vector-scalar)**2)

print(my_fun3(np.array([1,1,1,1]), 3))
print(my_fun3(np.array([2,2,2,2]), 3))

#%%[markdown]
# 10 - Write a function.. param:vector. return: log of each item as another vector. Use values to test: 0, 0.5, 1, 1.5
def my_fun4(vector):
    return np.log(vector)

print(my_fun4(np.array([2,2,2,2])))
print(my_fun4(np.array([.5, 1, 1.5])))

#%%[markdown]
# 11 - Test function from item 10 with: .1, .2, .3, ... 2. Use matplotlib to plot the data with a line plot where the input numbers are the X axis and the returned values give the Y axis.

inputArr = np.linspace(0.1, 2.0, num=20)
print(inputArr)
fun4Ret = my_fun4(inputArr)
print(fun4Ret)
import matplotlib.pyplot as plt
plt.plot(inputArr, fun4Ret, linewidth=2.0)

#%%[markdown]
# 12 - .... give params Theta0 and Theta1 (see image at the paper).... Theta0 is "c" and Theta1 is "m" in the traditional highschool equation y=mx+c

#%%[markdown]
# 13 - Using matplot drow 2 lines in 3D that intersect
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

datasets = [{"x":[1,2,3], "y":[1,4,9], "z":[0,0,0], "colour": "red"} for _ in range(6)]

for dataset in datasets:
    ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["colour"])

for dataset in datasets:
    ax.plot(dataset["y"], dataset["x"], dataset["z"], color=dataset["colour"])


plt.show()