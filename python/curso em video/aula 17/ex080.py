'''Crie um programa onde o usuário possa digitar cinco valores númericos
e cadastre-os em uma lista, ja na posição correta de inserção (sem usar o
metodo sort()).

No final, mostre a lista ordenada na tela.'''

valores = []

for i in range(7):
    valor = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(valor)
    else:
        for j, v in enumerate(valores):
            if valor <= v:
                valores.insert(j, valor)
                break
        else:
            valores.append(valor)
print(valores)

                

