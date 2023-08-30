'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequencia.

No final, mostre uma listagem de preços, organizando os dados em forma
tabular.'''

produtos = ['notebook', 'monitor', 'mouse', 'teclado']
precos = [2500, 1000, 250, 250]

print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

for produto, preco in zip(produtos, precos):
    print(f'{produto:.<20} R$ {preco:>7.2f}')

print('-' * 30)
