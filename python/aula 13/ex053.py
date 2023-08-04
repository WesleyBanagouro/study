'''Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços.'''

frase = input('Digite uma frase: ')

# Remover espaços da frase
frase_sem_espacos = frase.replace(' ', '')

# Verificar se a frase sem espaços é igual à sua inversão
palindromo = True
for i in range(len(frase_sem_espacos)):
    if frase_sem_espacos[i] != frase_sem_espacos[-i - 1]:
        palindromo = False
        break

if palindromo:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
