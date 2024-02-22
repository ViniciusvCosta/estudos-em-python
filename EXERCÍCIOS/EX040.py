nome = str(input('Digite o nome do aluno(a): '))
nota1 = float(input('Digite a nota do PRIMEIRO bimestre: '))
nota2 = float(input('Digite a nota do SEGUNDO bimestre: '))
nota3 = float(input('Digite a nota do TERCEIRO bimestre: '))
nota4 = float(input('Digite a nota do QUARTO bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media < 5.0:
    print('O anluno(a) {} teve media de {}, portanto foi reprovado!'.format(nome, media))
elif media >= 5.0 and media <= 6.9:
    print('O aluno(a) {} teve media de {}, portanto ficou de recuperação!'.format(nome, media))
elif media >= 7.0:
    print('O aluno(a) {} teve media de {}, portanto foi aprovado!'.format(nome, media))