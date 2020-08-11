#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:16:45 2020

@author: Tomas
"""
import numpy as np

#FUNCION
def mimatmul(A,B): 
    C_inicial = np.zeros((len(A),len(A)))
    for i in range(len(A)): #codigo basado en uno encontrado en www.stackoverflow.com 
        for j in range(len(B[0])):
            for k in range(len(B)):
                C_inicial[i][j] += A[i][k] * B[k][j]
    
    return (C_inicial)