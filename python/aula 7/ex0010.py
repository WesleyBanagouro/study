# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$ = R$ 3,27.
carteira = float(input('Quanto você tem na carteira?'))
dolar = 3.27
print('Com toda essa grana você consegue comprar US$ {:.2f}!'.format(carteira/dolar))