#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual o salário? '))
aum = 0.15
print('Parabéns, seu salario teve um aumento de {}%, ou seja, agora ele é R$ {}'.format(aum*100, sal*(1+aum)))