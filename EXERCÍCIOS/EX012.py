# Desconto 

nome = input('Produto: ')
valo = int(input('Preço: '))
perc = valo * 0.05
desc = valo - perc
print('O valor com desconto de 5% é de {}'.format(desc))