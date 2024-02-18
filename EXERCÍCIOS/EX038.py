n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
if n1 > n2:
    print('O numero {} é maior que {}'.format(n1,n2))
elif n1 < n2:
    print('O numero {} é maior que {}'.format(n2,n1))
elif n1 == n2:
    print('Os dois numeros que voce digitou são iguais')