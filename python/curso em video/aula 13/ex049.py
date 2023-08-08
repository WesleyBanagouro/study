'''Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usúario escolher, só que agora utilizando o laço for.'''

valor = int(input('Digite um numero de 1 a 10: '))

if valor > 10:
    print('É um valor de 1 a 10. Recomece o programa.')
else:
    for c in range(0, 10+1):
        resultado = valor * c
        print('{} x {} = {}'.format(valor, c, resultado))
print('fim')