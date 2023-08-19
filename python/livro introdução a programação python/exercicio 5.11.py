'''Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de 
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
Escreva o total ganho com juros no período.'''

meses = 0
inicial = float(input('Digite o depósito inicial: '))
juros = float(input('Qual é a taxa de juros em %: '))
valor_ganho = 0

while meses < 24:
    meses += 1
    inicial = inicial * (1 + (juros/100))
    valor_ganho += inicial - (inicial / (1 + juros/100))  # Calcula o valor ganho com juros no mês
    print(f'No mês {meses} você está com R$ {inicial:.2f}.')
    
print(f'Agora você tem R$ {inicial:.2f}.')
print(f'Total ganho com juros no período: R$ {valor_ganho:.2f}')
