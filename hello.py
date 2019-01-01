# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:48:08 2018

@author: hkawaguc
"""

print("Hello Anaconda")

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,15,200)
plt.plot(x,np.sin(x))
