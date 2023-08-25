'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A-) Quantas vezes apareceu o valor 9.

B-) Em que posição foi digitado o primeiro valor 3.

C-) Quais foram os números pares.'''

valores = ()
cont_9 = 0
cont = 0
posicao_3 = 0

while cont < 4:
    valor_entrada = int(input('Digite um valor: '))
    valores += (valor_entrada,)
    cont += 1

for valor in valores:
    if valor == 9:
        cont_9 += 1
    elif valor == 3:
    


print(valores)
