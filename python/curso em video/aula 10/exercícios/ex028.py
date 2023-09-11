'''Escreva um programa que faça o computador
"pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random

numeros = [0, 1, 2, 3, 4, 5]
aleatorio = random.choice(numeros)

print("Vou pensar em um número de 0 a 5. Tente adivinhar...")

tentativas = 0
while True:
    seu_numero = int(input('Qual é o seu palpite? '))
    tentativas += 1

    if seu_numero == aleatorio:
        print(f'Parabéns, você acertou em {tentativas} tentativas!')
        break
    else:
        print('Não, tente novamente.')

print(f'O número escolhido pelo computador era: {aleatorio}')

