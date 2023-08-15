'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''

cont = 0
sum = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    sum += num
    cont += 1
print(f'Você digitou {cont} números antes do flag e a soma entre os números digitados é igual a {sum}.')
print('Acabou')