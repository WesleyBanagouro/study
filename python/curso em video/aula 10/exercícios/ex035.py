
import math
l1 = int(input('Digite o primeiro lado:'))
l2 = int(input('Digite o segundo lado:'))
l3 = int(input('Digite o terceiro lado:'))

if l1 > math.fabs(l2 - l3) < l2 + l3:
    print('O triangulo pode ser formado')
else:
    print('O triangulo não pode ser formado')
