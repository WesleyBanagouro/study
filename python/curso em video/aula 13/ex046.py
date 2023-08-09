'''Faça um programa que mostre na tela uma contagem regressiva para o
estouro de fogos de artificios, indo de 10 até 0, com uma pausa de 1
segundo entre eles.'''
import time

for c in range(11, 0, -1):
    print(c)
    time.sleep(1)
print('Feliz ano novo!')



