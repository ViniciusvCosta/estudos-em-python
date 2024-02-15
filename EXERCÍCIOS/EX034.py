nome = str(input('Qual é o nome do colaborador '))
salario = float(input('Qual é o salario do funcionario {} R$:'.format(nome)))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O novo salario do colaborador {} sera de {}'.format(nome, novo))