#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção Inteira.
import math
num = float(input('Digite um número:'))
partint = math.trunc(num)

print(partint)
