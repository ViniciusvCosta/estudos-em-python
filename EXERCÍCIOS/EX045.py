#Calculo de jogada do computador
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

#Calculo de jogada do jogador
print('''SUAS OPÇÔES:
      [0]
      [1]
      [2]''')
jogador = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

#Resultado
print('-=' *11)
print('O computador escolheu: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
if computador == 0: #Computador jogou pedra
      if jogador == 0:
            print('DEU EMPATE')
      elif jogador == 1:
            print('JOGADOR GANHOU')
      elif jogador == 2:
            print('COMPUTADOR GANHOU')

elif computador == 1: #Computador jogou Papel
      if jogador == 0:
            print('COMPUTADOR GANHOU')
      elif jogador == 1:
            print('DEU EMPATE')
      elif jogador == 2:
            print('JOGADOR GANHOU')
    
elif computador == 2: #Computador jogou Tesoura
      if jogador == 0:
            print('JOGADOR GANHOU')
      elif jogador == 1:
            print('COMPUTADOR GANHOU')
      elif jogador == 2:
            print('DEU EMPATE')

print('-='*11)
print('FIM DE JOGO')