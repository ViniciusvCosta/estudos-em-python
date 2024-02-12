# Media do aluno
nome = str(input('Qual é o nome do aluno: ')).strip().lower()
n1 = float(input('Nota primeiro bimestre: '))
n2 = float(input('Nota segundo bimestre: '))
n3 = float(input('Nota terceiro bimestre: '))
n4 = float(input('Nota quarto bimestre: '))
media = (n1 + n2 + n3 + n4) / 4
if media >= 7:
    print('O aluno {} foi APROVADO'.format(nome))
else:
    print('O aluno {} foi REPROVADO!'.format(nome))