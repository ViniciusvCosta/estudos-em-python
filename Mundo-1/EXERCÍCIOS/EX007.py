# Media dos alunos

nome = input('DIgite o nume do aluno: ')
n1 = int(input('Nota primeiro semestre: '))
n2 = int(input('Nota segundo semestre: '))
n3 = int(input('Nota terceiro semestre: '))
n4 = int(input('Nota quarto semestre: '))
m = (n1 + n2 + n3 + n4) / 4
print('A media do aluno {} é {}'.format(nome, m))