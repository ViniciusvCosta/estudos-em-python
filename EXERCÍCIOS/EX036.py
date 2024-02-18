ValCasa = float(input('Valor da casa: '))
RendaMen = float(input('Sua renda mensal: '))
QuaAnos = int(input('Tempo do financiamento: '))
ValPrest = ValCasa / QuaAnos
if ValPrest >= 30% RendaMen:
    print('Seu financiamento foi negado!')
else:
    print('Seu financiamento foi aceito!, parabens.')
