#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:11:31 2020

@author: Tomas
"""

from time import perf_counter
import scipy as sp
import scipy.linalg as splinalg
import numpy as np
from numpy import zeros, float32
from matplotlib import pyplot as plt


def matriz_laplaciana( N , dtype = float32):
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

def plotting(names):
    xticks = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

    y1 = [ 0.1e-3 , 1e-3 , 1e-2 , 0.1 , 1. , 10. , 60 , 600 ]
    yticks1 = ["0.1 ms" , "1 ms" , "10 ms" , "0.1 s" , "1 s" , "10 s" , "1 min" , "10 min"]
    
    plt.figure()
    
    for name in names:
        data = np.loadtxt(name)
        N = data[:,0]
        dts = data[:,1]
        
        print("N: ", N)
        print("dts: ",dts)
        
        plt.loglog( N , dts.T, "-o", label=name )
        plt.ylabel("Tiempo transcurrido")
        plt.xlabel("Tamaño matriz")
        plt.grid(True)
        plt.xticks( xticks, xticks, rotation = 45)
        plt.yticks( y1 , yticks1)
    
    plt.tight_layout()
    plt.legend(loc = "upper left")
    plt.show()
        

N = [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]

Ncorridas = 10

names = ["A_invB_inv.txt","A_invB_npSolve.txt"] 

files = [open(name,"w") for name in names]

for N in N:
    dts = np.zeros((Ncorridas, len(files)))
    print(f"N = {N}")
    
    for i in range(Ncorridas):
        print (f"i = {i+1}")
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt
        
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve( A , B )
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1] = dt
    print ("dts : ",dts) 
    
    suma1 = 0
    suma2 = 0
    for i in range(Ncorridas):
        suma1 = suma1 + dts[i][0]
        suma2 = suma2 + dts[i][1]
    promedio = [(suma1/Ncorridas),(suma2/Ncorridas)]
    print ("Promedio: " , promedio)
    
    for j in range(len(files)):
        files[j].write(f"{N} {promedio[j]}\n")
        files[j].flush()
        
[file.close() for file in files]

plotting(names)
plt.savefig("graficoINV.png" , bbox_inches = "tight")




