#1)
#%%
import matplotlib.pyplot as plt
import numpy as np
import librosa

x = np.array([1, 0, -1], dtype = np.float32)
print(x)

#2)
print(np.cos(x))
#%%

#3)
#%%
m1 = [[0, 1, 2, 3, 2, 1, 0, -1, -2, -3] , [0, 1 ,2 ,3 ,2 ,1 , 0, -1, -2, -3]]
a2 = np.array(m1, dtype = np.float32)
print(a2.shape)
#%%

#4)
#%%
m2 = [ [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] , [ 0, .1, .2, .3 ,2 ,1 , 0, .1, .2, .3 ]]
a1 = np.array(m2, dtype = np.float32)
# p l o t(x, y, properties) where r means red ;
# − means a solidline; x means mark points with an x
plt.plot(a1[0, :], a1[1, :])
#%%

#5)
#%%
F = 10 
amp = 0.5
t = np.arange(-1, 1+1/fs, 1/fs)     # seconds
phase = np.pi
y = amp*np.cos(2*np.pi*F*t+phase)

#t = np.arange(-1,1+1/fs,1/fs)
#print( 'size of t: ', t.size)
#print('t:', t)

plt.figure()
plt.plot(t, y)
# units here are seconds on the x−axis as we are # plotting the signal over time
#plt.xlabel(time(s), fontsize=16)
#%%