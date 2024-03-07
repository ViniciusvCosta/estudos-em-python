print('CALCULADORA DE MEDIA ESCOLAR')
#entrada de dados (nome, notas bimestrais)
nome = input('NOME DO ALUNO: ')
n1 = float(input('Nota primeiro bimestre: '))
n2 = float(input('Nota segundo bimestre: '))
n3 = float(input('Nota terceiro bimestre: '))
n4 = float(input('Nota quarto bimestre: '))
#calculo de media
media = (n1 + n2 + n3 + n4) / 4
if media >= 7:
    print('O(a) aluno(a) {} teve media de {}, portanto foi aprovado(a)'.format(nome, media))
elif media >=5:
     print('O(a) aluno(a) {} teve media de {}, portanto esta em recuparação'.format(nome, media))
else:
    print('O(a) aluno(a) {} teve media de {}, portanto foi reprovado(a)'.format(nome, media))