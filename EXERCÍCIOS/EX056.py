SomaIdade = 0
MediaIdade = 0
MaiorIdadeHomen = 0
NomeVelho = ''
TotMulher20 = 0

for p in range(1, 5):
    print('----{}° PESOOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    SomaIdade += idade
    if p == 1 and sexo in 'Mm':
        MaiorIdadeHomen = idade
        NomeVelho = nome
    if sexo in 'Mm' and idade > MaiorIdadeHomen:
        MaiorIdadeHomen = idade
        NomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        TotMulher20 += 1

MediaIdade = SomaIdade / 4
print('A média de idade do grupo é de {} anos'.format(MediaIdade))
print('O homen mais velho tem {} anos e se chama {}'.format(MaiorIdadeHomen, NomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(TotMulher20))