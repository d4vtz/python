import math
import numpy as np
from sympy import Eijk, LeviCivita

a=[]
b=[]
c=[]



def suma(x,y):
    for k in range(len(x)):
        c.append=(x[k]+y[k])
    return c

def resta(x,y):
    for k in range(1,n+1):
        c.append=(x[k]-y[k])
    return c

def productoEscalar(x,y):
    for k in range(n):
        c.append=(x[k]*y[k])
    return c

def longitud(x):
    return math.sqrt(productoEscalar(x,x))

def angulo(x,y):
    ang=productoEscalar(x,y)/(longitud(x)*longitud(y))
    return math.acos(ang)


def componenteProdVectorial(x,y,l):
  
    e=np.zeros((3,3,3))
    
    for i in range(0,n+1):
        for j in range(0,n+1):
            for k in range(0,n+1):
                e[i,j,k]=LeviCivita(i,j,k)

    cont=0
    for a in range(0,n):
        for b in range(0,n+1):    
            cont = cont + x[a]*y[b]*e[a,b,l]        
    return cont        


def productoVectorial(x,y):
    c=[]
    for k in range(0,n+1):
         c.append(componenteProdVectorial(x,y,k))
    return c 




n=int(input('Dime el numero de dimensiones \n'))

print('Dame un vector A')
for i in range(1,n+1):
    a.append(input())
   
print('Dame un vector B')
for i in range(1,n+1):
    a.append(input())



op=int(input(' 1) Calcular la suma \n 2) Calcular la diferencia \n 3) Calcular el producto escalar \n 4) Calcular el producto vectorial \n 5) Calcular el ángulo (en grados) entre ellos \n 6) Calcular la longitud \n 7) Finalizar \n'))

if op == 1:
    print(suma(a,b))
    
   
if op == 2:
    print(resta(a,b))

if op == 3:
    print(productoEscalar(a,b))

if op == 4:
    print(productoVectorial(a,b))

if op == 5:
    print(angulo(a,b))

if op == 6:
    print(longitud(a))
    print(longitud(a))

if op == 7:
    print('Bye')
