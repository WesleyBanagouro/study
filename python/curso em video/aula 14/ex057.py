'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = input('Digite o sexo de uma pessoa: M ou F: ').upper()

while sexo != 'M' and sexo != 'F':
    print('Você é burro? Tem que ser M ou F. Vai de novo porra!')
    sexo = input('Digite o sexo de uma pessoa: M ou F: ').upper()
print('fim')