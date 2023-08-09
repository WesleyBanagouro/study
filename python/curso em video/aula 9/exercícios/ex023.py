''' Faça um programa que leia um valor de 0 a 9999 e mostre
na tela cada um dos digitos separados.
Ex: Digite um número: 1998
unidade:8
dezena:9
centena:9
milhar:1
'''

valor = str(input('Digite um valor de 0 a 9999:'))
unidade = valor[3]
dezena = valor[2]
centena = valor[1]
milhar = valor[0]
print('Unidade: {}.'.format(unidade))
print('Dezena: {}.'.format(dezena))
print('Centena: {}.'.format(centena))
print('Milhar: {}.'.format(milhar))