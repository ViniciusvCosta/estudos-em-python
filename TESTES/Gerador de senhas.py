import random
num = str(random.randint(1048698735, 9187642503))
while True:                         
    senha =''
    for numero in num:
        if numero in '0': senha += 'A'
        elif numero in '1': senha += '5'
        elif numero in '2': senha += 'q' 
        elif numero in '3': senha += '@'
        elif numero in '4': senha +='k'
        elif numero in '5': senha += 'H'
        elif numero in '6': senha += '9'
        elif numero in '7': senha += '&'
        elif numero in '8': senha += '#'
        elif numero in '9': senha += '?'
        
    print('-=' *30)
    print(f'Senha: {senha}')
    print('-=' *30)
    r = str(input('Outra? [S/N] '))
    if r in 'Nn':
        break