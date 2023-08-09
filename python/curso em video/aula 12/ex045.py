'''Crie um programa que faça o computador jogar Jokenpô com você.'''
import random

jokenpo = ['pedra', 'papel', 'tesoura']
pc = random.choice(jokenpo)
voce = str(input('Qual sua jogada: '))
voce_ganhou = 'Parabéns, voce ganhou do pc'
voce_perdeu = 'Que pena, o pc ganhou de voce'

if pc == 'pedra' and voce == 'papel':
    print(voce_ganhou)
elif pc == 'papel' and voce == 'pedra':
    print(voce_perdeu)
elif pc == 'pedra' and voce == 'tesoura':
    print(voce_perdeu)
elif pc == 'tesoura' and voce == 'pedra':
    print(voce_ganhou)
elif pc == 'papel' and voce == 'tesoura':
    print(voce_ganhou)
elif pc == 'tesoura' and voce == 'paple':
    print(voce_perdeu)
elif pc == voce:
    print('Empate!')

print('A jogada do pc foi: {}.'.format(pc))
print('A sua jogada foi: {}.'.format(voce))
