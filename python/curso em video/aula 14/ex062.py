'''Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

razao = int(input('Digite a razão da PA: '))
primeiro = int(input('Digite o primeiro valor da PA: '))
quantos_termos = int(input('Quantos termos você quer que mostre: '))
numero = 1  

while quantos_termos != 0:
    while numero <= quantos_termos:
        print(primeiro, end=' ')
        primeiro += razao
        numero += 1

    print('PAUSA')
    quantos_termos = int(input('Quer mostrar mais quantos termos? Digite 0 para sair: '))
    numero = 1  # Reseta a variável para recomeçar a contagem dos termos

print('Fim do programa.')
