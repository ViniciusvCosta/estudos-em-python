n = 1
par = impar = 0
while n != 0:
    n = int(input('DIGITE EM VALOR: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de pares é de {} e a de impares é de {}'.format(par, impar))