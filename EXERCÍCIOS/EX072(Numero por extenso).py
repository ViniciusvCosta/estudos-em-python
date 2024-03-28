resp = 'S'
cont = ('zero', 'um', 'dois', 'tres', 'quatro',
         'cinco', 'seis','sete', 'oito', 'nove', 
         'dez', 'onze', 'doze', 'treze', 'quartorze', 
         'quinze', 'dezesseis', 'dezessete', 'dezoito', 
         'dezenove', 'vinte')
while resp not in 'N':
    while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print('Você digitou o numero {}'.format(cont[num]))
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()     
print('Fim de programa!')