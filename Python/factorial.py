n=int(input('Dime el número al cual le quieres sacar el factorial. \n'))

fac=1

for i in range(1,n+1):
    fac=fac*i
    i=i+1

print('El factorial de',n,'es',fac)

