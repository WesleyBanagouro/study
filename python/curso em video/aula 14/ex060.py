'''Faça um programa que leia um numero qualquer e mostre 
o seu fatorial.'''

num = int(input('Digite um número: '))
fatoriais = []
resultado = 1

i = 1

while i <= num:
    resultado *= i
    fatoriais.append(i)
    i += 1

fatoriais_str = ', '.join(map(str, fatoriais))
print('Você digitou o número {}, ou seja, os fatoriais são os números {}. O resultado é igual a {}.'.format(num, fatoriais_str, resultado))
