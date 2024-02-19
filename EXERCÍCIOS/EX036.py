ValCasa = float(input('Valor da casa: '))
RendaMen = float(input('Sua renda mensal: '))
QuaAnos = int(input('Qauntos anos de financiamento: '))
ValPrest = ValCasa / (QuaAnos * 12)
print('O valor da prestação será de R${:.2f} por mês'.format(ValPrest))
if ValPrest >= RendaMen * 30 / 100:
    print('Financiamento foi negado!')
else:
    print('Financiamento foi aceito!.')
