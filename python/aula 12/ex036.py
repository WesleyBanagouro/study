''' Escreva um programa para aprovar um emprestimo bancario para uma
compra de uma casa. O programa vai perguntar o valor da casa, o salario
do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação
mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo
será negado.'''

casa = float(input('Qual o valor do imovel?'))
salario = float(input('Qual é o seu salario?'))
anos = int(input('Em quantos anos voce pretende pagar?'))
meses = anos*12
mensalidade = casa/meses

if casa/meses <= (30/100)*salario:
    print('Parabens, seu emprestimo foi aprovado e o valor da mensalidade é de {}.'.format(mensalidade))
elif casa/meses >= (30/100)*salario:
    print('Não poderemos te conceder o emprestimo pois a mensalidade ultrapassa os 30% do seu salario.')