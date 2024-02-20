num = int(input('Digite um numero: '))
print('''Escolha uma das bases  para conversão:
    [1] Converter para BINARIO
    [2] Converter para OCTAL
    [3] Converter para HEXADECIMAL''')
opeção = int(input('Sua opção: '))
if opeção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opeção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opeção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('''ERRO! OPEÇÂO INVALIDA!
          Tente novamente''')

