'''Desenvolva um programa que pergunte a distancia
de uma viagem em Km. Calcule o preço da passagem,
cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para
viagens mais longas.'''
viagem = float(input('Qual a distancia da viagem:'))
if viagem <= 200:
    custo = 0.5 * viagem
    print('O valor dessa viagem é de R$ {:.2f}'.format(custo))
else:
    custo = 0.45 * viagem
    print('O valor dessa viagem é de R$ {:.2f}'.format(custo))
