nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()

print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('seu primero nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
#print('seu primeiro nome tem {}'.format(nome.find(' ')))
