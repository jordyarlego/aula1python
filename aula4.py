tupla_nova = 10, 20, 30
print(tupla_nova)

tupla_vazia = ()
print(tupla_vazia)

nova_tupla = tuple('Teste')
print(nova_tupla)

tupla_nomes = ('Marlene', 'Zezinho', 'Marlene', 'Cibele', 'Zuely')
print(tupla_nomes.count('Marlene'))

print(tupla_nomes.count('Suely'))
print (tupla_nomes.count('Zezinho'))

#crie uma tupla com os elementos: 1,2,2,3,4,4,4,5 e depois utilize a função count do objeto tupla para verificar quantas vezes o numero 4 aparece na tupla.

tupla_numeros = 1,2,2,3,4,4,4,5

print(tupla_numeros.count(4))


#criando um dicioário:

dicio={'chave':'valor'}
print(type(dicio))

#O que acontece em cada sequencia de comandos  a seguir?

d ={'laranjas': 15, 'bananas': 35, 'siriguelas':12}
print (d['bananas'])

#revisão list =[] tuple = () dict {:}

#o que acontece em cada sequencia de comandos a segui?
#b)

d['pitomba'] =20
print (len(d))
print (d)


#c)

print ('pitomba' in d)

#D)

print ('pears' in d)

#f)

del d ['laranjas']

print('laranjas' in d)

frutas = ['pinha', 'oiti coró', 'jaca', 'tamarindo']
print ([1,2]+[3,4])
print(frutas + [6,7,8,9])

print ([0]*4)
print([1,2,['oi', 'tchau']]*2)