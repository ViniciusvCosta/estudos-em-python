import datetime 
Nasc = int(input('Digite sua data de nascimento: '))
DataNasc = datetime.datetime.strptime(Nasc, format)
DataAtual = datetime.today()
Idade = DataAtual - DataNasc
if Idade < 18:
    print('Você ainda vai ter que se alistar!')
elif Idade == 18:
    print('Já esta na hora de se alistar!')
elif Idade > 18:
    print('Já passou da hora de fazer seu alistamento!')