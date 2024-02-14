from datetime import date
ano = int(input('Que ano você quer analisar? Digite 0 para analisar p ano atual!: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %  400 == 0:
    print('O ano {} é BISEXTO'.format(ano))
else:
    print('O ano {} NÂO È BISEXTO'.format(ano))