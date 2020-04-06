
def f(x):
    return x**2

def Sum(n):
    s=0
    for i in range(1,n+1):
        s=s+f(i)
        i=i+1
    return s


n=int(input('Dime el número asta el cual queres sumar\n'))
print(Sum(n))
