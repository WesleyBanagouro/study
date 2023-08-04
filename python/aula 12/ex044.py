'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

    - à vista dinheiro/ cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros'''

valor = float(input('Digite o valor da compra: '))
print('Opções de pagamento:\n'
      '1- À vista dinheiro/ cheque: 10% de desconto;\n'
      '2- à vista no cartão: 5% de desconto\n'
      '3- em até 2x no cartão: preço normal\n'
      '4- 3x ou mais no cartão: 20% de juros')
desconto_dinheiro = 1-(10/100)
desconto_cartao = 1-(5/100)
juros = 1+(20/100)
pagamento = int(input('Selecione um tipo de pagamento: '))
print('-=' * 11)
if pagamento == 1:
    print('O pagamento à vista em dinheiro/cheque oferece 10% de desconto, ou seja, você pagará R$ {:.2f}.'.format(valor*desconto_dinheiro))
elif pagamento == 2:
    print('O pagamento à vista no cartão oferece 5% de desconto, ou seja, você pagará R$ {:.2f}.'.format(valor*desconto_cartao))
elif pagamento == 3:
    parcelas_sem = int(input('Em quantas vezes: '))
    if parcelas_sem > 2:
        confirmacao = str(input(print('Haverá uma taxa de juros de 20% para parcelamentos maiores do que 2, quer continuar?')))
        if confirmacao == 'Sim':
            parcelas_juros = int(input('Quantas vezes deseja parcelar: '))
            print('Você pagará R$ {:.2f} em {} parcelas de R$ {:.2f}.'.format(valor * juros, parcelas_juros, (valor * juros) / parcelas_juros))
        elif confirmacao == 'Não':
            parcelas = int(input('Quantas vezes deseja parcelar: '))
            print('Não há descontos, você pagará R$ {:.2f} em {} parcelas de R$ {:.2f}.'.format(valor, parcelas, valor / parcelas))
    else:
        print('Não há descontos, você pagará R$ {:.2f} em {} parcelas de R$ {:.2f}.'.format(valor, valor/parcelas_sem))
elif pagamento == 4:
    parcelas = int(input('Em quantas vezes: '))
    print('Aqui há juros de 20% para parcelamento, ou seja, você pagará R$ {:.2f} em {} parcelas de R$ {:.2f}.'.format(valor*juros, parcelas, (valor*juros)/parcelas))
