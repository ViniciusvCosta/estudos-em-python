print('-=' *20)
resultado = 0
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segunod valor: '))
print('''Escolha a operação
      Para Adição [1]
      Para Subtração [2]
      Para multiplicação [3]
      Para divisão [4]
      Para novos valores [5]
      Para encerar [0]''')
opecao = int(input('Sua escolha: '))

if opecao == 1:
    resultado = num1 + num2
    print('A soma de {} e {} é  {}'.format(num1, num2, resultado))
elif opecao == 2:
    resultado = num1 - num2
    print('O resultado da subtração de {} e {} é  {}'.format(num1,num2,resultado))
elif opecao == 3:
    resultado = num1 * num2
    print('O resultado da multiplicação de {} por {} é  {}'.format(num1,num2,resultado))
elif opecao == 4:
    resultado = num1 / num2
    print('O resultada da divisão de {} por {} é {}'.format(num1,num2,resultado))
elif opecao == 5:
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segunod valor: '))
    print('''Escolha a operação
      Para Adição [1]
      Para Subtração [2]
      Para multiplicação [3]
      Para divisão [4]
      Para novos valores [5]
      Para encerar [0]''')
    opecao = int(input('Sua escolha: '))
elif opecao == 0:
    print('Fim do programa!')

print('-=' * 20)