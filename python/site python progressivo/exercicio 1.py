'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

numeros_invalidos = []
numeros_corretos = []

while True:
    n = int(input('Digite um número (de 0 a 10): '))
    if n >= 0 and n <= 10:
        numeros_corretos.append(n)
        continuar = input('Quer continuar? S ou N: ')
        if continuar.upper() == 'N':
            break
    else:
        numeros_invalidos.append(n)
        print('É para digitar apenas números de 0 a 10. Tente novamente.')

print('Números inválidos:', numeros_invalidos)
print('Números corretos:', numeros_corretos)
print('Fim.')
