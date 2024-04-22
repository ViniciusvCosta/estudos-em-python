larg = float(input('Altura: '))
altu = float(input('Largura: '))
mq = larg * altu 
rend = int(input('Redimento do material em m²: '))
most = mq / rend
print('Você vai precisar de {} pra a area de {}m²'.format(most, mq))