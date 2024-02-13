velocidade = float(input('Qula velocidade o carro está? '))
if velocidade > 80:
    print('MULTADO. Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você recebeu uma multa de R${:.2f}!'.format(multa))
print('Dirija com cuidado, tenha um otimo dia!')