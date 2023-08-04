'''Faça um programa que leia uma frase pelo teclado e
mostre:
- Quantas vezes aparece a letra 'A'.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a ultima vez'''

frase = str(input('Digite uma frase:'))
a = frase.lower().count('a')
print('A sua frase tem {} letras a'.format(a))
pri_a = frase.lower().find('a')
print('A primeira letra a aparece no caractere {}'.format(pri_a))
ult_a = frase.lower().rfind('a')
print('A ultima letra a aparece no caractere {}'.format(ult_a))
