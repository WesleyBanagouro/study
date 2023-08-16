'''Crie um programa que leia o nome e o preço de varios
produtos. O produto deverá perguntar se o usuário vai continuar.
No final, mostre:
    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$ 1.000,00
    C) Qual é o nome do produto mais barato.'''

total_gasto = 0
produtos_mais_mil = 0
produto_mais_barato = None
preco_mais_barato = float('inf')  

while True:
    nome = input('Digite o nome do produto: ').capitalize()
    preco = float(input('Digite o preço do produto: '))
    total_gasto += preco

    if preco > 1000:
        produtos_mais_mil += 1

    if preco < preco_mais_barato:
        produto_mais_barato = nome
        preco_mais_barato = preco

    continuar = input('Vai continuar? (Sim/Não): ').capitalize()
    if continuar == 'Não':
        break

print(f"Total gasto na compra: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos custando mais de R$ 1.000,00: {produtos_mais_mil}")
print(f"Nome do produto mais barato: {produto_mais_barato} (R$ {preco_mais_barato:.2f})")
