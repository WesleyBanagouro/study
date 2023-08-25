'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A-) Quantas vezes apareceu o valor 9.

B-) Em que posição foi digitado o primeiro valor 3.

C-) Quais foram os números pares.'''

valores = ()
cont = 0
posicao_3 = 0
pares = ()

while cont < 4:
    valor_entrada = int(input('Digite um valor: '))
    valores += (valor_entrada,)
    cont += 1

for valor in valores:
    if valor % 2 == 0:
        pares += (valor,)

cont_9 = valores.count(9)
posicao_3 = valores.index(3)

print(valores)
print(f'Na tupla digitada, há {cont_9} números 9.')
print(f'Na tupla digitada, o número 3 encontra - se na {posicao_3 + 1}ª posição.')
print(f'Os números pares são {pares}.')
