#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Tomas
"""
from matplotlib import pyplot as plt
from scipy import matmul, rand
from time import perf_counter
import numpy as np

#LISTA DE N PARA GRAFICAR, ME DIO SOLO HASTA 500 
lista_N = [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,300,500]
lista_T = []
lista_M = []

#FUNCION
def mimatmul(A,B): 
    C_inicial = np.zeros((len(A),len(A)))
    for i in range(len(A)): #codigo basado en uno encontrado en www.stackoverflow.com 
        for j in range(len(B[0])):
            for k in range(len(B)):
                C_inicial[i][j] += A[i][k] * B[k][j]
    
    return (C_inicial)

#CODIGO PARA GRAFICAR      
for j in range(10):
    elemento1 = []
    elemento2 = []
    for i in lista_N: 
        A = rand(i,i)
        B = rand(i,i)
    
        t1 = perf_counter()
        C = mimatmul(A,B)
        t2 = perf_counter()
    
        dt = t2 - t1
        size = 3 * (i**2) * 8
        
        elemento1.append(dt)
        elemento2.append(size)
        
    lista_T.append(elemento1)
    lista_M.append(elemento2)

    print ("Iteracion " + str(j+1) + " lista") #para verificar la realizacion de cada iteracion
    

x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xticks = ["","","","","","","","","","",""]

y1 = [ 0.1e-3 , 1e-3 , 1e-2 , 0.1 , 1. , 10. , 60 , 600 , 3600]
yticks1 = ["0.1 ms" , "1 ms" , "10 ms" , "0.1 s" , "1 s" , "10 s" , "1 min" , "10 min" , "1 h"]
    
plt.figure()
plt.subplot(2,1,1)
plt.loglog( lista_N , lista_T[0] , "-s")
plt.loglog( lista_N , lista_T[1] , "-s")
plt.loglog( lista_N , lista_T[2] , "-s")
plt.loglog( lista_N , lista_T[3] , "-s")
plt.loglog( lista_N , lista_T[4] , "-s")
plt.loglog( lista_N , lista_T[5] , "-s")
plt.loglog( lista_N , lista_T[6] , "-s")
plt.loglog( lista_N , lista_T[7] , "-s")
plt.loglog( lista_N , lista_T[8] , "-s")
plt.loglog( lista_N , lista_T[9] , "-s")

plt.xticks( x , xticks , rotation = 45 )
plt.yticks( y1 , yticks1 )
plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento de A*B")
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

plt.savefig("grafico.png" , bbox_inches = "tight") #codigo para guardar imagen del grafico con dimensiones en que se vea todo

plt.show()
