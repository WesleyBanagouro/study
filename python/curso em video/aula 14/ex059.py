'''Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

numeros = []
alternativas = '[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa'

for num in range(2):
    num = int(input('Digite um número: '))
    numeros.append(num)

escolha = int(input('Os números digitados foram {} e {}. Agora escolha uma das opções abaixo: \n {} \n'.format(numeros[0], numeros[1], alternativas)))

while escolha != 5:
    if escolha == 1:
        print('A soma é igual a {}.'.format(sum(numeros)))
    elif escolha == 2:
        resultado = 1
        for num in numeros:
            resultado *= num
        print('A multiplicação é igual a {}.'.format(resultado))
    elif escolha == 3:
        maior = max(numeros)
        print('O maior número é {}.'.format(maior))
    elif escolha == 4:
        numeros.clear()
        for num in range(2):
            num = int(input('Digite um número: '))
            numeros.append(num)
    else:
        print('Opção inválida. Tente novamente.')

    escolha = int(input('Escolha uma das opções abaixo: \n {} \n'.format(alternativas)))

print('Fim do programa.')
