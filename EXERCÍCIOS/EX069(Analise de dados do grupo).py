tot18 = totH = totM20 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >=18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Total de pessoas com mais de 10 anos: {}'.format(tot18))
print('Ao todo temos {} homens cadastrados'.format(totH))
print('E temos {} ,ulheres com menos de 20 anos'.format(totM20))