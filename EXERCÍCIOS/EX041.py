from datetime import date
atual = date.today().year
nascimento = int(input('Em qual ano você nascel '))
idade = atual - nascimento
print('O atleta tem {}'.format(idade))

if idade <= 9:
    print('categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER') 



