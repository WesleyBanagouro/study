'''Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo.'''

numero = int(input('Digite um número inteiro: '))

# Verifica se o número é negativo, zero ou igual a 1
if numero <= 1:
    print('O número não é primo.')
else:
    # Loop para verificar se o número é divisível por algum valor no intervalo de 2 a (numero - 1)
    for divisor in range(2, numero):
        if numero % divisor == 0:
            print('O número não é primo.')
            break
    else:
        print('O número é primo.')
