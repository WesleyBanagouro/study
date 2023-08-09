'''Faça um programa que leia o peso de cinco pessoas. No
 final, mostre qual foi o maior e o menor peso lidos.'''

pesos = []

for peso in range(0, 5):
    peso = float(input('Digite o peso:'))
    pesos.append(peso)
print('O maior peso digitado é o de {}kg.'.format(max(pesos)))

