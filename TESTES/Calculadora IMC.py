print('Calculadora de indece de massa corporal (I.M.C)')
nome = str(input('Digite seu nome: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/ (altura **2)

if imc <= 18.5:
    print('{} seu IMC é de {:.2f}, você esta classificado como ABAIXO DO PESO'.format(nome, imc))
elif imc <= 24.9:
    print('{} seu IMC é de {:.2f}, você esta classificado como PESO NORMAL'.format(nome, imc))
elif imc <= 29.9:
    print('{} seu IMC é de {:.2f}, você esta classificado como SOBREPESO'.format(nome, imc))
elif imc <= 34.9:
    print('{} seu IMC é de {:.2f}, você esta classificado como OBESIDADE'.format(nome, imc))
elif imc <= 39.9:
    print('{} seu IMC é de {:.2f}, você esta classificado como OBSIDADE GRAU II'.format(nome, imc))
else:
    print('{} seu IMC é de {:.2f}, você esta classificado como OBSIDADE MÓRBIDA'.format(nome, imc))