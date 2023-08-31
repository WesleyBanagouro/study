'''Crie um programa que vai ler vários números e colocar em 
uma lista.

Depois disso, mostre:

A-) Quantos números foram digitados.

B-) A lista de valores, ordenada de forma descrescente.

C-) Se o valor 5 foi digitado esta ou não na lista.'''

c = 0
i = 0
numeros = []

while c != 'N':
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    i += 1
    c = input('Quer continuar? (s/n)').upper()
print(f'A-) Foram digitados {i} valores.')
numeros.sort(reverse = True)
print(f'B-) A lista de forma decrescente: {numeros}.')
if 5 in numeros:
    print(f'Você digitou um número 5.')
else:
    print('Você não digitou um número 5.')