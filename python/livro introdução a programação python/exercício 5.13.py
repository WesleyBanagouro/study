'''Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e 
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número 
de meses para que a dívida seja paga, o total pago e o total de juros pagos.'''

divida = float(input('Qual o valor da sua dívida: '))
juros = float(input('Qual os juros mensais em %: '))
pagamento = float(input('Quanto você pode pagar por mês: '))
mes = 0
total_pago = 0
total_juros = 0

while divida > 0:
    juros_pago = divida * (juros/100)
    total_juros += juros_pago
    divida += juros_pago  # Adiciona os juros ao valor da dívida
    divida -= pagamento
    total_pago += pagamento
    mes += 1

print(f'Você pagará a dívida em {mes} meses.')
print(f'Total pago: R$ {total_pago:.2f}')
print(f'Total de juros pagos: R$ {total_juros:.2f}')
