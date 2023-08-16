'''Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) Quantas mulheres tem menos de 20 anos.'''

sexo = []
idade = []
cont_idade = 0
cont_homem = 0
cont_mulher = 0

while True:
    s = input('Digite um sexo: ').capitalize()
    while s != 'Feminino' and s != 'Masculino':
        print('Digite feminino ou masculino')
        s = input('Digite um sexo: ').capitalize()
    id = int(input('Digite uma idade: '))
    sexo.append(s)
    idade.append(id)
    if s == 'Feminino' and id < 20:
        cont_mulher += 1
    continuar = input('Quer continuar? ').capitalize()
    if continuar == 'Não':
        break

for i in idade:
    if i > 18:
        cont_idade += 1
for homem in sexo:
    if homem == 'Masculino':
        cont_homem += 1


print(f'Dos usuários cadastrados, {cont_idade} são maiores de idade.')
print(f'Dos usuários cadastrados, {cont_homem} são homens.')
print(f'Dos usuários cadastrados, {cont_mulher} são mulheres e menores de 20 anos.')