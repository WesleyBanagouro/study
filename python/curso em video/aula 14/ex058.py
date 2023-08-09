'''Melhore o desafio 28 onde o computador vai "pensar" em um numero entre 0 e 5.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''

import random

tentativas = 0
numeros = [0, 1, 2, 3, 4, 5]
aleatorio = random.choice(numeros)
seu_numero = int(input('O computador pensou em um número de 0 a 5, tente adivinhar:'))
print(aleatorio)
while seu_numero != aleatorio:
    seu_numero = int(input(('Você errou, tente novamente.')))
    tentativas += 1
print('Parabéns, você é o bichão memo!. Você acertou na {}º tentativa.'.format(tentativas + 1))