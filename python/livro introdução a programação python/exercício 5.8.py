'''Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da 
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e 
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resultado = 0

while n2 > 0:
    resultado += n1
    n2 -= 1

print(resultado)
