# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
aluno = input('Qual é o aluno? ')
n1 = int(input('Qual a primeira nota: '))
n2 = int(input('Qual a segunda nota: '))
print('O aluno {} teve como primeira nota {}, segunda nota {}, ou seja, sua média é {:.1f}!'.format(aluno, n1, n2, (n1+n2)/2))
