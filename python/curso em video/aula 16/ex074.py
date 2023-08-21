'''Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e tambem
indique o menor e o maior valor que estão na tupla.'''

import random

t = ()

while len(t) <= 4:
    n = (random.randint(1, 10))
    t = t + (n,)

print('Os números sorteados foram:', end=' ')
for n in t:
    print(n, end=' ')
print(f"\nO maior valor na tupla é: {max(t)}")
print(f"O menor valor na tupla é: {min(t)}")