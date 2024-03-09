print('C.M.E')
#entrada de dados (nome, notas bimestrais)
nome = input('NOME DO ALUNO:')
n1 = float(input('Nota primeiro bimestre: '))
n2 = float(input('Nota segundo bimestre: '))
n3 = float(input('Nota terceiro bimestre: '))
n4 = float(input('Nota quarto bimestre: '))
#calculo de media
media = (n1 + n2 + n3 + n4) / 4
if media >= 7:
    print('O(a) aluno(a) \033[34m{}\033[m teve media de \033[34m{}\033[m, portanto foi \033[32maprovado\033[m'.format(nome, media))
elif media >=5:
     print('O(a) aluno(a) \033[34m{}\033[m teve media de \033[34m{}\033[m, portanto esta em \033[34mrecuparação\033[m'.format(nome, media))
else:
    print('O(a) aluno(a) \033[34m{}\033[m teve media de \033[34m{}\033[m, portanto foi \033[31mreprovado\033[m'.format(nome, media))