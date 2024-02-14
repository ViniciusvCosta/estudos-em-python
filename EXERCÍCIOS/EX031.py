distancia = float(input('Qual é a distancia da viagem que você ira fazer '))
print('Você esta prestese a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Sua passagem ira custar {:.2f}'.format(preço))