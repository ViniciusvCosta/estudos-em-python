from random import randint
from time import sleep
computador = randint(0,5) #Esse comando faz o computador sortear um nomero aleatoria entre 0 e 5
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('EU pensei no numero {}, Você ganhou o jogo'.format(computador))
else:
    print('EU pensei no numero {}, Eu ganhei o jogo'.format(computador))