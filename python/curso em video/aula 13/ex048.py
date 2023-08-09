'''Faça um programa que calcule a soma entre todos os números ímpares
que são multiplos de tres e que se encontram no intervalo de 1 até 500.'''

soma = 0  # Variável para acumular a soma dos números ímpares múltiplos de 3

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c  # Adiciona o número c à soma

print('A soma dos números ímpares múltiplos de 3 é:', soma)
print('fim')
