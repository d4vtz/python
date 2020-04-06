
def fac(x):
    f=1
    for n in range(1,x+1):
       f=f*n
       n=n+1 
    return f

def Combinatoria(n,m):
    return (fac(n))/(fac(m)*fac(n-m))

print(Combinatoria(15,10))


