'''Faça um programa que leia um ano qualquer e mostre
se ele é BISSEXTO.'''
ano = int(input('Digite um ano aqui:'))
if ano % 4 == 0:
    print('Esse ano é bissexto')
elif ano % 400 == 0:
    print('Esse ano é bissexto')
elif ano % 100 == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')