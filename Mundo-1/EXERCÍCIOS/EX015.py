dias = int(input('Por qunatos dias o carro foi alugado? '))
km = float(input('Quantos kM foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser para é de R${:.2f}'.format(pago))
