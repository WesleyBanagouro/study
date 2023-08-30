'''Crie um programa que tenha uma tupla com varias palavras 
(não usar acentos). Depois disso, voce deve mostrar, para cada palavra
quais são suas vogais.'''

palavras = ('python', 'programacao', 'linguagem', 'computador', 'desenvolvimento')

vogais = 'aeiou'

for palavra in palavras:
    vogais_encontradas = [letra for letra in palavra if letra in vogais]
    print(f'Vogais em {palavra}: {", ".join(vogais_encontradas)}')


    
    
    