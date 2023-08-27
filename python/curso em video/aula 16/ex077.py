'''Crie um programa que tenha uma tupla com varias palavras 
(não usar acentos). Depois disso, voce deve mostrar, para cada palavra
quais são suas vogais.'''

palavras = ('hamburger', 'queijo', 'batata', 'refrigerante')
vogais = 'aeiouAEIOU'

for palavra in palavras:
    vogais_palavra = []
    for letra in palavra:
        if letra in vogais:
            vogais_palavra.append(letra)
    vogais_formatadas = ' '.join(vogais_palavra)
    print(f'Vogais em {palavra}: {vogais_formatadas}')


    
    
    