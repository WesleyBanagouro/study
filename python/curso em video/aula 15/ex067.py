'''Faça um programa que mostre a tabuada de vários números, um
de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo.'''

import time

while True:
    num = int(input('Digite o número que você quer saber a tabuada (digite um número negativo para sair): '))
    
    if num < 0:
        print('Programa encerrado.')
        break
    
    tab = 1
    while tab <= 10:
        print(f'{num} x {tab} = {num * tab}')
        print('-=' * 10)
        time.sleep(0.5)
        tab += 1



