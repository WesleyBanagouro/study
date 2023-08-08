'''Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.'''
vel = int(input('Qual foi a velocidade do carro?'))
if vel > 80:
    multa = 7 * (vel - 80)
    print('Foi multado, sua multa é no valor de R$ {:.2f}'.format(multa))
else:
    print('Não foi multado, passou na velocidade de {}Km/h.'.format(vel))