# Faça um programa que leia um número Inteiro e mostre na tela seu sucessor e seu antecessor.
num = int(input('Digite um número: '))
sus = num + 1
ant = num - 1
print('O antecessor do número {} é {} e seu sucessor é {}!'.format(num, ant, sus))