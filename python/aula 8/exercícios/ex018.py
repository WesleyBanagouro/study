# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math

ang_graus = int(input('Digite um angulo em graus:'))
ang_rad = math.radians(ang_graus)
sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tang = math.tan(ang_rad)
print('Baseado no angulo {}, informado acima, o valor do seu seno é {}, o valor do seu cosseno é {} e sua tangente é {}.'.format(ang_graus, sen, cos, tang))
