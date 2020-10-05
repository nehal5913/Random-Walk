# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:45:47 2020

@author: Nehal
"""
import matplotlib.pyplot as plt
import numpy as np
N=1000
pos=0
time=0
y=[pos]
x=[time]
for i in range(0,N):
    rdm=np.random.random()
    if rdm<0.5:
        pos+=1
        time+=1
    elif rdm>0.5:
        pos+=-1
        time+=1
    y.append(pos)
    x.append(time)
plt.plot(x,y,'g',linewidth=2,label='random walk')
plt.title('Randomwalk')
plt.show()