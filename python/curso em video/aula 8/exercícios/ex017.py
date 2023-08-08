# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math

co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
h = print('Considerando que o triangulo tem {} como cateto oposto, {} como cateto adjacente, sua hipotenusa vale {}.'.format(co, ca, math.hypot(co, ca)))
