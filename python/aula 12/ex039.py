'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar;
    - Se é a hora de se alistar;
    - Se já passou do tempo de alistamento.

Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.'''

idade = int(input('Digite sua idade:'))

if idade < 18:
    print('Voce ainda vai se alistar, faltam {} anos para voce se alistar. Se prepare!'.format(18 - idade))
elif idade == 18:
    print('Chegou a hora de voce se alistar!')
elif idade > 18:
    print('Voce passou {} anos do alistamento.'.format(idade - 18))