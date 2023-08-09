'''Refaça o desafio 51, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.'''

razao = int(input('Digite a razão da PA: '))
primeiro = int(input('Digite o primeiro valor da PA: '))
numero = 1  # Variável para contar o número de termos exibidos

while numero <= 10:  # Vamos exibir os 10 primeiros termos da PA
    print(primeiro, end=' ')
    primeiro += razao
    numero += 1
