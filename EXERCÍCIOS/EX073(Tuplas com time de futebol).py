times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'atletico', 'Botafogo',
         'Atletico-PR', 'Bahia', 'São paulo', 'Fluminense', 'Sport recife', 'EC vitoria', 'Coritiba', 'Avai', 'Ponte preta', 'Atletico-Go')
print('-=' * 15)
print('Lista de times: {}'.format(times))
print('-=' * 15)
print('Os cinoc primeiroa time são: {}'.format(times[0:5]))
print('-=' * 15)
print('Os quantro ultimos são: {}'.format(times[-4:]))
print('-=' * 15)
print('Times em oderm alfabetica: {}'.format(sorted(times)))
print('-=' * 15)
print('O chapecoense está na {} posição'.format(times.index('Chapecoense')+1))
print('-=' * 15)
