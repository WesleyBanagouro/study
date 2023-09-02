'''Crie um programa que vai ler vários números e colocar em uma
lista.

Depois disso, crie duas listas extras que vão conter apenas os 
valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteudo das 3 listas geradas.'''

numeros = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número para separar entre pares e ímpares: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    
    c = input('Quer continuar digitando? (s/n)').strip().upper()
    if c != 'S':
        break

print(f'A lista completa de números digitados: {numeros}.')
if pares:
    print(f'A lista de números pares digitados: {pares}.')
else:
    print('Você não digitou números pares.')
if impares:
    print(f'A lista de números ímpares digitados: {impares}.')
else:
    print('Você não digitou números ímpares.')
