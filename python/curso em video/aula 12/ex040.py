'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

    - Media abaixo de 5.0: REPROVADO
    - Media entre 5.0 e 6.9: RECUPERAÇÃO
    - Media 7.0 ou superior: APROVADO'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2

if m < 5:
    print('Você está reprovado!')
elif 5 <= m < 6.9:
    print('Você está de recuperação!')
else:
    print('Você foi aprovado!')