import math
a=int(input('Dime a: \n'))
b=int(input('Dime b: \n'))
c=int(input('Dime c: \n'))

det=b**2-4*a*c

if det >= 0:
    x1=(-b+math.sqrt(det))/2*a
    x2=(-b-math.sqrt(det))/2*a
    print(x1,'\t',x2)
else:
    print('La ecuación no se puede resolver en los reales')
    