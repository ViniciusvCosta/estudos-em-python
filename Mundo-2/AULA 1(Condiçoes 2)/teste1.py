nome = str(input('Qual é o seu nome? ')).strip().lower()
if nome == 'vinicius':
    print('Que nome lindo caraa!')
elif nome == 'pedro' or nome == 'maria' or nome =='paulo':
    print('Seu nome é bme comun aqui no brasil')
elif nome == 'mamaco aranha':
    print('É hora do heroi (musica foda)')
else:
    print('Seu nome é normal')
print('Prazer em te conhecer {}'.format(nome))