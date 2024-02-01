R = int(input('Qual é o valor a ser convertido R$:'))
M = (input('Qual é a moeda que deseja fazer a coversão?: '))
ME = int(input('Qual é o valor atual dessa moeda? '))
C = R / ME
print('O valor {} envertido em {} da {}'.format(R, M, C))