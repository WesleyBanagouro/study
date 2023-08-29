'''Crie um programa que tenha uma tupla com varias palavras 
(não usar acentos). Depois disso, voce deve mostrar, para cada palavra
quais são suas vogais.'''

def calcular_media_soma(valores):
    soma = sum(valores)
    media = soma / len(valores)
    return media, soma

# Valores de exemplo (você pode substituí-los por seus próprios valores)
valores = (10, 20, 30, 40, 50)

media, soma = calcular_media_soma(valores)

print(f'Valores: {valores}')
print(f'Média: {media:.2f}')
print(f'Soma: {soma}')


    
    
    