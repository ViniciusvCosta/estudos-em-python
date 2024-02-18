nome = str(input('Digite o nome do aluno(a): '))
n1 = float(input('Digite a nota do PRIMEIRO bimestre: '))
n2 = float(input('Digite a nota do SEGUNDO bimestre: '))
n3 = float(input('Digite a nota do TERCEIRO bimestre: '))
n4 = float(input('Digite a nota do QUARTO bimestre: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5.0:
    print('O anluno(a) {} teve media de {}, portanto foi reprovado!'.format(nome, media))
elif media >= 5.0 and media <= 6.9:
    print('O aluno(a) {} teve media de {}, portanto ficou de recuperação!'.format(nome, media))
elif media >= 7.0:
    print('O aluno(a) {} teve media de {}, portanto foi aprovado!'.format(nome, media))