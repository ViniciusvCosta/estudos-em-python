'''import datetime 
Nasc = int(input('Digite sua data de nascimento: '))
DataNasc = datetime.datetime.strptime(Nasc, format)
DataAtual = datetime.today()
Idade = DataAtual - DataNasc
if Idade < 18:
    print('Você ainda vai ter que se alistar!')
elif Idade == 18:
    print('Já esta na hora de se alistar!')
elif Idade > 18:
    print('Já passou da hora de fazer seu alistamento!')'''

from datetime import date
AnoAtual = date.today().year
AnoNasc = int(input('Digite o ano de nascimento'))
idade = AnoAtual - AnoNasc

if idade == 18:
    print('Já esta na hora de se alistar!') 

elif idade < 18:
    saldo = 18 - idade
    print('Você ainda vai ter que se alistar em {} anos!'. format(saldo))

elif idade > 18:
    saldo = idade -18
    print('Voê deveria ter se alistado ha {} anos!'.format(saldo))