from random import randint
num = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),)
print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print('\nO maior valor sorteado foi {}'.format(max(num)))
print('O menor valor sorteado foi {}'.format(min(num)))