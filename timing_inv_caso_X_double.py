#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:08:38 2020

@author: Tomas
"""

from numpy import zeros, float32, float64, float16
import numpy as np
import scipy as sp
from scipy import linalg
from matplotlib import pyplot as plt
from time import perf_counter
from funcion_laplaciana import matriz_laplaciana

#LISTA DE N PARA GRAFICAR, ME DIO SOLO HASTA 500 
lista_N = [ 2, 5, 10, 12, 15, 20, 30, 40, 45, 50,55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000,10000]
lista_T_numpy = []
lista_T_scipy_t = []
lista_T_scipy_f = []
lista_M = []

#CODIGO PARA GRAFICAR   

for j in range(1):
    elemento1 = []
    elemento2 = []
    for i in lista_N: 
        A = matriz_laplaciana(i , np.double)
        
        t1 = perf_counter()
        C = np.linalg.inv(A)
        t2 = perf_counter()
    
        dt = t2 - t1
        size = (i**2) * 11
        
        elemento1.append(dt)
        elemento2.append(size)
        
    lista_T_numpy.append(elemento1)
    lista_M.append(elemento2)
    
for j in range(1):
    elemento3 = []
    elemento4 = []
    for i in lista_N: 
        A = matriz_laplaciana(i , np.double)
        
        t3 = perf_counter()
        C = sp.linalg.inv(A)
        overwrite_a = True
        t4 = perf_counter()
    
        dt1 = t4 - t3
        size1 =  (i**2) * 11
        
        elemento3.append(dt1)
        elemento4.append(size1)
        
    lista_T_scipy_t.append(elemento3)
    lista_M.append(elemento4)
    
for j in range(1):
    elemento5 = []
    elemento6 = []
    for i in lista_N: 
        A = matriz_laplaciana(i , np.double)
        
        t5 = perf_counter()
        C = sp.linalg.inv(A)
        overwrite_a = False
        t6 = perf_counter()
    
        dt2 = t6 - t5
        size2 =  (i**2) * 11
        
        elemento5.append(dt2)
        elemento6.append(size2)
        
    lista_T_scipy_f.append(elemento5)
    lista_M.append(elemento6)

x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xticks = ["","","","","","","","","","",""]

y1 = [ 0.1e-3 , 1e-3 , 1e-2 , 0.1 , 1. , 10. , 60 , 600 , 3600]
yticks1 = ["0.1 ms" , "1 ms" , "10 ms" , "0.1 s" , "1 s" , "10 s" , "1 min" , "10 min" , "1 h"]
    
plt.figure()
plt.subplot(2,1,1)

plt.loglog( lista_N , lista_T_numpy[0] , "-rs")
plt.loglog( lista_N , lista_T_scipy_t[0] , "-bs")
plt.loglog( lista_N , lista_T_scipy_f[0] , "-gs")

plt.xticks( x , xticks , rotation = 45 )
plt.yticks( y1 , yticks1 )
plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento INV de matriz")
plt.grid()

xticks1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]

y2 = [ 10**3 , 10**4 , 10**5 , 10**6 , 10**7 , 10**8 , 10**9 , 10**10 , 10**11]
yticks2 = ["1 KB" , "10 KB" , "100 KB" , "1 MB" , "10 MB" , "100 MB" , "1 GB" , "10 GB"]

plt.subplot(2,1,2)
plt.loglog( lista_N , lista_M[0] , "-o")
plt.xticks( x , xticks1 , rotation = 45)
plt.yticks( y2 , yticks2 )
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Uso de memoria")
plt.grid()

plt.axhline(y=20000000000, xmin=0.001, xmax=0.9999,color="black",ls="--")

plt.savefig("grafico_double.png" , bbox_inches = "tight") #codigo para guardar imagen del grafico con dimensiones en que se vea todo

plt.show()

