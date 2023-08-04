'''Desenvolva uma logia que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

    - Abaixo de 18.5: abaixo do peso
    - Entre 18.5 e 25: peso ideal
    - 25 até 30: sobrepeso
    - 30 até 40: obesidade
    - Acima de 40: obesidade mórbida'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('De acordo com os dados fornecidos, seu imc é de {:.2f}. Você esta sendo considerado abaixo do peso.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('De acordo com os dados fornecidos, seu imc é de {:.2f}. Você esta com o peso ideal para sua altura.'.format(imc))
elif imc > 25 and imc < 30:
    print('De acordo com os dados fornecidos, seu imc é de {:.2f}. Você esta com sobrepeso.'.format(imc))
elif imc > 30 and imc < 40:
    print('De acordo com os dados fornecidos, seu imc é de {:.2f}. Você esta com obesidade.'.format(imc))
elif imc > 40:
    print('De acordo com os dados fornecidos, seu imc é de {:.2f}. Você esta com obesidade mórbida.'.format(imc))