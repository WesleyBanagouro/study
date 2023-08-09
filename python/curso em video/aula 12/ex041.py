'''A confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com
a idade:

    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    - Até 20 anos: SÊNIOR
    - Acima: MASTER'''

ano = int(input('Qual o ano de seu nascimento?'))
idade = 2023 - ano

if idade <= 9:
    print('Como você tem {} anos, você é classificado como Mirim!'.format(idade))
elif 9 < idade <= 14:
    print('Como você tem {} anos, você é classificado como Infantil!'.format(idade))
elif 14 < idade <= 19:
    print('Como você tem {} anos, você é classificado como Junior!'.format(idade))
elif 19 < idade <= 20:
    print('Como você tem {} anos, você é classificado como Senior!'.format(idade))
else:
    print('Como você tem {} anos, você é classificado como Master!'.format(idade))
