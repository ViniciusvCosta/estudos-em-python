print('-=' * 20)
print('Analisador de Trinangulos')
print('-=' * 20)
r1 = float(input("Primeira medida "))
r2 = float(input("Segunda medida "))
r3 = float(input("Terceira medida "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas acima PODEM fomar um triangulo!', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('As medidas acima NÂO PODEM fromar um triangulo!')