'''Crie um programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
 e quantas já são maiores.'''
maiores = []

for ano in range(0, 7):
    ano = int(input('Digite a data de nascimento:'))
    idade = 2023 - ano
    if idade >= 18:
        maiores.append(ano)
print('Com base nos 7 anos de nascimentos digitados, {} desses anos são pessoas maiores de idade.'.format(len(maiores)))
