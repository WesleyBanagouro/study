'''Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
    - A media de idade do grupo.
    - Qual o nome do homem mais velho.
    - Quantas mulheres tem menos de 21 anos.'''
p1 = []
p2 = []
p3 = []
p4 = []
nomes = []
idades = []
sexos = []

for pessoa in range(0, 4):
    nome = input('Digite um nome:')
    idade = float(input('Digite uma idade:'))
    sexo = input('Digite um sexo:')
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
p1 = nomes[0], (idades[0]), sexos[0]
p2 = nomes[1], (idades[1]), sexos[1]
p3 = nomes[2], (idades[2]), sexos[2]
p4 = nomes[3], (idades[3]), sexos[3]

media = (p1[1] + p2[1] + p3[1] + p4[1])/4
print('A media de idades das 4 pessoas é igual a {}.'.format(media))

mais_velho = None

if p1[2] == 'masculino' and p2[2] == 'masculino' and p3[2] == 'masculino' and p4[2] == 'masculino':
    if p1[1] > p2[1] and p1[1] > p3[1] and p1[1] > p4[1]:
        mais_velho = p1
    elif p2[1] > p3[1] and p2[1] > p4[1]:
        mais_velho = p2
    elif p3[1] > p4[1]:
        mais_velho = p3
    else:
        mais_velho = p4

if mais_velho is not None:
    print('Dentre as 4 pessoas cadastradas, o homem mais velho é o {}, com {} anos'.format(mais_velho[0], mais_velho[1]))


