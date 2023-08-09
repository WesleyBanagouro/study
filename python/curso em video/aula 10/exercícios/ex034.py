'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input('Digite aqui o salario:'))
aumento10 = 10/100
aumento15 = 15/100
if salario > 1250:
    aumento = salario * (1 + aumento10)
else:
    aumento = salario * (1 + aumento15)

print('O salario final é de R${:.2f}'.format(aumento))