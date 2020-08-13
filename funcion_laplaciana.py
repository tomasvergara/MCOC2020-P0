#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:02:10 2020

@author: Tomas
"""
import scipy
from scipy import linalg
import numpy as np
from numpy import zeros, float32 , float16 , float64 
from matplotlib.pylab import *


def matriz_laplaciana( N , dtype ):
    A = zeros( (N,N) , dtype = dtype )
    
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j] = 2
            if i+1 == j:
                A[i,j] = -1
            if i-1 == j:
                A[i,j] = -1
                
    return A      
