# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
prod = float(input('Qual o preço do produto? '))
desc = prod * (95/100)
print('Parabéns! Você conseguiu um desconto de 5%, ou seja, pagará apenas R$ {:.2f}'.format(desc))