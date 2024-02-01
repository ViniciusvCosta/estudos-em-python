# Desconto 

nome = input('Produto: ')
valo = int(input('Preço: '))
perc = 5
desc = valo * (1 - perc / valo)
print('O valor com desconto de 5% é de {}'.format(desc))