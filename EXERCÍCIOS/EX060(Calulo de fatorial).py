''' from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O factorial de {} é {}'.format(n,f)) '''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n 
f = 1
while c > 0:
    print('{} '.format(c), end='')
    print('X' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))