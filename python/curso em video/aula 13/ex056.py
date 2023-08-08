nomes = []
idades = []
sexos = []

for pessoa in range(4):
    nome = input('Digite um nome: ')
    idade = int(input('Digite uma idade: '))
    sexo = input('Digite um sexo (masculino ou feminino): ').lower()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

media_idades = sum(idades) / len(idades)
print('A média de idades das 4 pessoas é igual a {:.2f}.'.format(media_idades))

mais_velho = None
for i in range(4):
    if sexos[i] == 'masculino':
        if mais_velho is None or idades[i] > mais_velho[1]:
            mais_velho = (nomes[i], idades[i])

if mais_velho is not None:
    print('Dentre as 4 pessoas cadastradas, o homem mais velho é o {}, com {} anos.'.format(mais_velho[0], mais_velho[1]))

mulheres_menos_de_21 = sum(1 for i in range(4) if sexos[i] == 'feminino' and idades[i] < 21)
print('Quantidade de mulheres com menos de 21 anos: {}'.format(mulheres_menos_de_21))
