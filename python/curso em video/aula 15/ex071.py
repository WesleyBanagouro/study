'''Crie um programa que simule o funcionamento de um 
caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1. '''

valor_saque = int(input("Digite o valor a ser sacado: "))

cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0

while True:
    if valor_saque >= 50:
        valor_saque -= 50
        cedulas_50 += 1
    elif valor_saque >= 20:
        valor_saque -= 20
        cedulas_20 += 1
    elif valor_saque >= 10:
        valor_saque -= 10
        cedulas_10 += 1
    elif valor_saque >= 1:
        valor_saque -= 1
        cedulas_1 += 1
    else:
        break

print(f"Quantidade de cédulas de R$ 50: {cedulas_50}")
print(f"Quantidade de cédulas de R$ 20: {cedulas_20}")
print(f"Quantidade de cédulas de R$ 10: {cedulas_10}")
print(f"Quantidade de cédulas de R$ 1: {cedulas_1}")
