lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print(f'O valor {num} foi adicionado com sucesso')
    else:
        print(f'O valor {num} esta duplicado!, não vou adicionalo novamente')
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
print('-=' *30)
lista.sort()
print(f'{lista}')