'''Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
Código Preço
1 0,50
2 1,00
3 4,00
5 7,00
9 8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.'''

total = 0
codigo = 1
while codigo != 0:
    codigo = int(input('Digite o codigo do produto ou 0 para terminar: '))
    if codigo != 0:
        quantidade = int(input('Digite a quantidade desse produto: '))
        if codigo == 1:
            total += (0.5 * quantidade)
            print(f'O produto {codigo} foi adicionado no carrinho!')
        elif codigo == 2:
            total += (1 * quantidade)
            print(f'O produto {codigo} foi adicionado no carrinho!')
        elif codigo == 3:
            total += (4 * quantidade)
            print(f'O produto {codigo} foi adicionado no carrinho!')
        elif codigo == 5:
            total += (7 * quantidade)
            print(f'O produto {codigo} foi adicionado no carrinho!')
        elif codigo == 9:
            total += (8 * quantidade)
            print(f'O produto {codigo} foi adicionado no carrinho!')
        else:
            print('Código inválido.')
print(f'O total da sua compra foi de R$ {total:.2f}.')
