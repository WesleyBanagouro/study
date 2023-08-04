'''Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

razao = int(input('Digite a razão da PA:'))
primeiro = int(input('Digite o primeiro valor da PA:'))

for c in range(1, 10*razao, razao):
    primeiro += razao
    print(c)