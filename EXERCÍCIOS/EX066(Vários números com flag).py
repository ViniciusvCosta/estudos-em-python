n = s = c = 0
while True:
    n = int(input('Digite um numero ou digite [999] para sair: '))
    if n == 999:
        break
    s += n
    c += 1

print('Você digitou {} e a soma dos valores digitados foi {}'.format(c, s))
print('=' * 15, 'fim', '=' * 15)
