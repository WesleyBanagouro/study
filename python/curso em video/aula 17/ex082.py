'''Crie um programa que vai ler vários números e colocar em uma
lista.

Depois disso, crie duas listas extras que vão conter apenas os 
valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteudo das tres listas geradas.'''

c = 0

numeros = []
pares = []
impares = []

while c != 'N':
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    c = input('Quer continuar? (s/n)').upper()
print(f'A lista de números digitados: {numeros}.')
if len(pares) == 0:
    print('Você não digitou pares.')
else:
    print(f'A lista de números pares digitados: {pares}.')
if len(impares) == 0:
    print('Você não digitou ímpares.')
else:
    print(f'A lista de números impares digitados: {impares}.')