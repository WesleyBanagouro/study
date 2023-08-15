'''Faça um programa que jogue par ou ímpar com o computador. O 
jogo só será interrompido quando o jogador perder, mostrando o total de 
vitórias consecutivas que ele conquistou no final do jogo.'''
import random
cont = 0

while True:
    ganhador = 0
    escolha = 0

    while escolha != 'P' and escolha != 'I':
        escolha = input('Digite sua jogada (P/I): ').capitalize()
    numero = int(input('Escolha um número de 0 a 10: '))
    num_pc = random.randint(1, 10)
    if (num_pc + numero) % 2 == 0:
        ganhador = 'P'
    else:
        ganhador = 'I'
    if escolha == ganhador:
        print('Você ganhou porra!')
        print(f'Sua escolha: {numero}. Escolha do PC: {num_pc}. A soma dos dois vale {num_pc + numero}, ou seja é {ganhador}.')
        cont += 1
    else:
        print('O computador ganhou!')
        print(f'Sua escolha: {numero}. Escolha do PC: {num_pc}. A soma dos dois vale {num_pc + numero}, ou seja é {ganhador}.')
        break
print(f'Você ganhou {cont} vezes consecutivas.')

