lista = []
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? S/N '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de paresé {pares}')
print(f'A lista de impares é {impares}')