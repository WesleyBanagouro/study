'''Crie um programa que tenha uma tupla com varias palavras 
(não usar acentos). Depois disso, voce deve mostrar, para cada palavra
quais são suas vogais.'''

palavras = ('hamburger', 'queijo', 'batata', 'refrigerante')
vogais = 'aeiouAEIOU'

for palavra in palavras:
    for letra in palavra:
        vogais_palavra = []
        if letra in vogais:
            vogais_palavra.append(letra)
print(vogais_palavra)
    
    
    