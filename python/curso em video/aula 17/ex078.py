'''Faça um programa que leia 5 valores numéricos e guarde-os em uma
lista.

No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista.'''

i = 0
numeros = []

while i < 5:
    numero = int(input('Digite um número para adicionar na lista: '))
    numeros.append(numero)
    i += 1

maior = max(numeros)
menor = min(numeros)
posicao_maior = []
posicao_menor = []

for posicao, num in enumerate(numeros):
    if num == maior:
        posicao_maior.append(posicao + 1)
    elif num == menor:
        posicao_menor.append(posicao + 1)
        

if len(posicao_maior) > 1:
    print(f'O maior numero digitado foi o {maior} nas posições {posicao_maior}')
else:
    print(f'O maior numero digitado foi o {maior} na posição {posicao_maior}')
if len(posicao_menor) > 1:
    print(f'O menor numero digitado foi o {menor} nas posições {posicao_menor}')
else:
    print(f'O menor numero digitado foi o {menor} na posição {posicao_menor}')