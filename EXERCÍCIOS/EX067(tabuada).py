print('=' * 15, 'TABUDA', '=' * 15)
while True:
    n = int(input('Qual tabuada você quer ver? '))
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n*c))
print('=' * 15, 'FIM', '=' * 15)