from algebraLineal import LeviCivita
import numpy as np

x=[[1,2],[3,5]]
y=[[4,6],[1,2]]


a=np.zeros((2,2))


for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                a[i,j]=LeviCivita(2)[k,i]*LeviCivita(2)[l,i]*x[k][i]*x[l][j]

print(a)