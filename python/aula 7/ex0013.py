sal = float(input('Qual o salário? '))
aum = 0.15
novo_salario = sal * (1 + aum)
print(f'Parabéns, seu salário teve um aumento de {aum * 100}%, ou seja, agora ele é R$ {novo_salario:.2f}')
