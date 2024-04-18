a = [2,3,4,7]
# b = a :Aqui temos uma ligação entre a lista A e a lista B
b = a[:]#aqui temos uma copia da lista a
b[2] = 8
print(f'lista A: {a}')
print(f'Lista B: {b}')