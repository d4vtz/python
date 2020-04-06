import math
import numpy as np 
from sympy import Eijk as Levi_Civita


def metricaM(n):

    g=np.zeros((n,n))
    for i in range(n):
        if i == 0: 
            g[i,i] = 1
        else:
            g[i,i] = -1

    return g


def identidad(n):

    I=np.zeros((n,n))
    for i in range(n):
        I[i,i] = 1 
        
    return I


def productoEscalarM(n,x,y):

    prod = 0
    for i in range(n):
        for j in range(n):
                prod = prod + x[i]*metricaM(n)[i,j]*y[j]
            
    return prod

def productoEscalar(n,x,y):

    prod = 0
    for i in range(n):
        for j in range(n):
                prod = prod + x[i]*identidad(n)[i,j]*y[j]
            
    return prod



a = [[1,2,3],
     [2,1,1]]

b = [[1,2],
     [1,2],
     [2,3]]

c = []

#for i in range(len(a)):
#    for j in range(len(a)):    
#        for k in range(len(a)):

#            c[i,j] += a[i,k]*b[k,j]
            
#print(c)







