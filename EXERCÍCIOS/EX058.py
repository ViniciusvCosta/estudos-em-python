from random import randint
computador = randint(0,10) #Esse comando faz o computador sortear um nomero aleatoria entre 0 e 10
acertou = False
palpites = 0
print('EU sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinha qual foi? ')
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez')
print('Acertou!')
print('Você precisou de {} para acertar!'.format(palpites))


