'''Crie um programa onde o usuário possa digitar vários valores 
numéricos e cadastre-os em uma lista. Caso o número já exista la
dentro, ele não será adicionado. No final, serão exibidos todos os
valores unicos digitados em ordem crescente.'''

valores = []
c = input('Vamos começar?').upper()

while c == 'S':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Esse valor já foi digitado. Ele não será adicionado.')
        c = input('Quer continuar? (s/n)').upper()
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
        c = input('Quer continuar? (s/n)').upper()
print(valores.sort())
    