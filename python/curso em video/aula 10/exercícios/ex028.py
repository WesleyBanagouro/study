'''Escreva um programa que faça o computador
"pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random

numeros = [0, 1, 2, 3, 4, 5]
aleatorio = random.choice(numeros)
seu_numero = int(input('O computador pensou em um número de 0 a 5, tente adivinhar:'))
print(aleatorio)
if seu_numero == aleatorio:
    print('Parabéns, você é o bichão memo!')
else:
    print('Não, você errou!')
