from random import randint
v = 0
while True:
    jogador = int(input('Diga u valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I] ', end ='')).strip().upper() [0]
    print('Você jogou {} e o computador {}. Total de {}'.format(jogador, computador, total))
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print('GAME OVER! Você venceu {} vezes. ',format(v))