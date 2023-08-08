'''Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50.'''

pares = []
for c in range(0, 51):
    if c % 2 == 0:
        pares.append(c)
print(pares)
print('fim')