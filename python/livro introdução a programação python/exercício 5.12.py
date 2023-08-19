'''Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor 
depositado mensalmente. Esse valor será depositado no início de cada mês, e você 
deve considerá-lo para o cálculo de juros do mês seguinte.'''

meses = 0
inicial = float(input('Digite o depósito inicial: '))
juros = float(input('Qual é a taxa de juros em %: '))
valor_ganho = 0

while meses < 24:
    validação = input('Você vai aportar? ').capitalize()
    if validação == 'Sim':
        aporte = float(input('Quanto: '))
        inicial = inicial + aporte
    inicial = inicial * (1 + (juros/100))
    meses += 1
    valor_ganho += inicial - (inicial / (1 + juros/100)) - aporte  # Calcula o valor ganho com juros no mês
    print(f'No mês {meses} você está com R$ {inicial:.2f}.')
    
print(f'Agora você tem R$ {inicial:.2f}.')
print(f'Total ganho com juros no período: R$ {valor_ganho:.2f}')
