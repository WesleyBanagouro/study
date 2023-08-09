'''Crie um programa que leia o nome de uma cidade e
diga se ela começa ou não com o nome "Santo".'''
cidade = str(input('Digite aqui uma cidade:'))
print(cidade[:5] == 'Santo')