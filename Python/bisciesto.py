
a=int(input('Dime el año: \n'))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('El año', a ,'es bisciesto')

else:
    print('No es bisciesto')