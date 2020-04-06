# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:22:44 2019

@author: Administrator
"""

from PyEMD import EMD
import numpy as np
s = np.random.random(100)
emd = EMD()
IMFs = emd(s)
print(IMFs.shape)
print(s.shape)