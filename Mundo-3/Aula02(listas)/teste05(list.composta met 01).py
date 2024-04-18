#Forma errada
'''
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste)
teste[0] = 'maria'
teste[1] = 22
galera.append(teste)
print(galera)


    Nesse exmplo o resultado que queremos é uma lista composta. Mas ao rodar o script
só serão exibidos osovalores inseridos após o galera.append(teste).
    Para conseguirmos uma lista composta devemos colocar [:] para assim farmos uma copia da lista teste.
    Dessa maneira galera.append(teste[:])
'''

#forma correta 
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)