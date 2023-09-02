'''Crie um programa onde o usuário digite uma expressão qualquer 
que use parenteses. Seu aplicativo deverá analisar se a expressão 
passada esta com os parenteses abertos e fechados na ordem correta.'''


expressao = input('Digite aqui sua expressão: ')
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida! Parabéns')
else:
    print('Sua expressão está errada!')
