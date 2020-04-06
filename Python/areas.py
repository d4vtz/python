import math

def area(b,h):
    return b*h

print('Dime que figura queres calcular el perimetro y el area (1-4).\n')
print(' 1) \tCirculo \n 2) \tcuadrado \n 3) \tRecatngulo \n 3) \tTriangulo \n')

n=int(input())

if n == 1:
    r=float(input('Dime el radio: \n'))
    s=math.pi*r**2
    p=2*math.pi*r
    print(p,'\t',s)

elif n == 2 :
    b=float(input('Dime la longitud de su base: \n'))    
    print(4*b,'\t',area(b,b))

elif n == 3 :
    b=float(input('Dime la base: \n'))    
    h=float(input('Dime la altura: \n'))
    print(2*b+2*h,'\t',area(b,h))

elif n == 4 :
    b=float(input('Dime la base: \n'))    
    h=float(input('Dime la altura: \n'))
    c=math.sqrt(h**2+(b/2)**2)
    p=2*c+b    
    print(p,'\t',(area(b,h))/2)