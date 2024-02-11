#conversor de moeda

#Entrada do valor em real
R = int(input('Qual é o valor a ser convertido R$:'))
#Entrada do nome da moeda
M = (input('Qual é a moeda que deseja fazer a coversão?: '))
#Entrada do valor atual da moeda
ME = int(input('Qual é o valor atual dessa moeda? '))
#Calculo de conversão
C = R / ME
print('O valor {} envertido em {} da {}'.format(R, M, C))