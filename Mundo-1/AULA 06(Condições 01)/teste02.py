#Nome bonito
nome = str(input('Qual é o seu nome? ')).strip().lower()
print('Bom dia, {}'.format(nome))
if nome == 'vinicius':
    print('Que nome bonito você tem!')
else:
    print('Seu nome é tão normal! ')
