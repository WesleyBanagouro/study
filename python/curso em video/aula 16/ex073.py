'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol, na ordem de colocação. Depois 
mostre:

A-) Apenas os 5 primeiros colocados.
B-) Os ultimos 4 colocados da tabela.
C-) Uma lista com os times em ordem alfabética.
D-) em que posição na tabela esta o time do São Paulo.'''

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'Grêmio', 'Red Bull Bragantino', 'Athletico-PR', 'Fortaleza', 'Cuiabá', 'São Paulo', 'Atlético-MG', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco', 'Coritiba', 'América-MG')

print('Os 5 primeiros colocados são: ')

for colocacao in range(0, len(times[0:5])):
    print(f'{times[colocacao]} em {colocacao + 1}º lugar.')
print('-' * 30)

print('Os 4 ultimos colocados são: ')
for colocacao in range(len(times) - 4, len(times)):
    print(f'{times[colocacao]} em {colocacao + 1}º lugar.')
print('-' * 30)

print('Arqui está os times em ordem alfabética: ')
print(sorted(times))

t = times.index('São Paulo')
print(f'O São Paulo está na {t + 1}º posição.')



