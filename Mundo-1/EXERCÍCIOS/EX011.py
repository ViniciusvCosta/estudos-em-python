larg = int(input('Altura: '))
altu = int(input('Largura: '))
mq = larg * altu 
rend = int(input('Redimento do material em m²: '))
resu = rend * mq
most = resu / rend
print('Você vai precisar de {} pra a {}m²'.format(most, mq))