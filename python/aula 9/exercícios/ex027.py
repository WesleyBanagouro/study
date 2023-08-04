'''Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o segundo nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Segundo = Souza'''

nome = str(input('Digite seu nome completo:'))
sep = nome.split()
print('O seu primeiro nome é {} e o segundo é {}.'.format(sep[0], sep[1]))

