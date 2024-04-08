num = [2, 5, 9, 1]
num [2] = 3 #para mudar um elemento da lista
num.append(7)
num.sort() #para organizar uma lista em ordem crecente
num.sort(reverse=True) #para organizar uma lista em forma decrecente
num.insert(2.0) #para adicionar um elemento em uma ordem especifica
num.pop() #para eliminar um elemto da lista, Se estiver sem parametro ele ira remover o ultimo elemento da lista
print(num)
print(f'Essa lista tem{len(num)} elementos.')