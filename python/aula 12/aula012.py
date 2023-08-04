nome = str(input('Qual é o seu nome?'))
if nome == 'Wesley':
    print('Nossa que nome lindo, {}! Bom dia pra você!'.format(nome))
elif nome == 'Pedro' or 'Maria' or 'Beatriz':
    print('Seu nome é bem comum no Brasil.')
else:
    print('Seu nome é comum, {}, mas mesmo assim, bom dia.'.format(nome))