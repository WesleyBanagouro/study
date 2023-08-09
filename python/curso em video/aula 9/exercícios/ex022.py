''' Crie um programa que leia o nome completo de uma pessoa
e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minusculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome:'))
print('Aqui está seu nome em maiúscula: {}!'.format(nome.upper()))
print('Aqui está seu nome em minúscula: {}!'.format(nome.lower()))
sem_espaco = nome.replace(' ', '')
print('Seu nome tem {} letras!'.format(len(sem_espaco)))
primeiro_nome = nome.split()
print('O seu primeiro nome é {} e tem {} letras!'.format(primeiro_nome[0], len(primeiro_nome[0])))