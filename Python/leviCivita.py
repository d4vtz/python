import numpy as np
from sympy import Eijk, LeviCivita


e=np.zeros((3,3,3))

for i in range(3):
    for j in range(3):
        for k in range(3):
            e[i,j,k]=LeviCivita(i,j,k)
            
            
print(e[0,1,2])       
