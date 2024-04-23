while True:
    nome = str(input('Qual é o seu nome? ')).strip().lower()
    if nome == 'vinicius':
        print('Que nome lindo caraa!')
    elif nome == 'pedro' or nome == 'maria' or nome =='paulo':
        print('Seu nome é bem comun aqui no brasil')
    
    elif nome in 'mamaco aranha':
        print('É hora do heroi (musica foda)')
        break
