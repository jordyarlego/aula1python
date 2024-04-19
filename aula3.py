L = []
L = list() #consultor de listas

dias = [3,1,10]
dias= [0]

Z =[3,8,9]
Z [0] =7
Z 

V = [6,7,5,8,9]
Z = V
Z



a = [81,82,83]
b= a[:] #cria um clone com fatia
print(a==b)
print(a is b)
b[0] =5
print(a)
print(b)

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])

a=[1,2,3]
b=a[:]
b[0] =5
print(a[2])

#crie uma lista chamada minhaLista com os seguintes itens: 76, 92.3, "oi", True, 4, 76. Depois execute os seguintes comendos:
#a) inserir "pitomba" e 76 no final da lista.
#b)inserir o valor "cibele" na posição de índice 3.
#c)inserir o valor 99 no inicio da lista
#d) encontrar o indice de "oi".


minhaLista = [76, 92.3 ,"oi" ,True , 4, 76]
minhaLista2 =["pitomba", 76]
lista = minhaLista + minhaLista2
print (minhaLista + minhaLista2)
minhalista3 =['Cibele']
print(minhaLista[0:3]+ minhalista3 + lista [3:])
minhaLista4 =[99]
print(minhaLista4+minhaLista[0:3]+ minhalista3 + lista [3:] )
#encontrar o indice de 'oi'
if(minhaLista [0]== 'oi'):
    print('indice 1')
elif(minhaLista [1] == 'oi'):
    print('indice 2 ')
elif(minhaLista [2]== 'oi'):
    print('indice 3')
elif(minhaLista [3] == 'oi'):
    print('indice 4 ')
elif(minhaLista [4]== 'oi'):
    print('indice 5')
else:
    print('indice 6')    
