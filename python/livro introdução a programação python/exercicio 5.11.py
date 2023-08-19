'''Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de 
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
Escreva o total ganho com juros no período.'''

meses = 0
inicial = float(input('Digite o deposito inicial: '))
juros = float(input('Qual é a taxa de juros em%: '))/100

while meses <= 24:
    