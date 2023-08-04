'''Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderar o flag 999)'''

n = 0
cont = 0
soma = 0 - 999

while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n

print('-'*30)
print('Foram digitados {} valores.'.format(cont - 1))
print('-'*30)
print('A soma dos {} valores digitados é igual a {}.'.format(cont-1, soma))
print('-'*30)
print('FIM')