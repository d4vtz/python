import math
import numpy as np
from sympy import Eijk, LeviCivita

def componenteProdVectorial(x,y,l):
  
    e=np.zeros((3,3,3))
    
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                e[i,j,k]=LeviCivita(i,j,k)

    cont=0
    for a in range(0,3):
        for b in range(0,3):    
            cont = cont + x[a]*y[b]*e[a,b,l]        
    return cont        


def productoVectorial(x,y):
    c=[]
    for k in range(0,3):
         c.append(componenteProdVectorial(x,y,k))
    return c 

a=[1,2,3]      
b=[3,2,1]

print(productoVectorial(a,b))