"""for produto in range(0,4):
    p =str(input("digite o nome do produto: "))
    v = float(input("digite o valor do produto: "))

for elemento in [1,2,3,4,5,6]:
    print('estamos no elemento', elemento) 


for elemento in 'String':
    print ('estamos no elemento', elemento)

for elemento in range (len("string")):
    print('estamos no elemento', elemento)

produto = 0
while produto <4:
    p = str(input('Digite o nome do produto: '))
    v = float(input('Digite o valor do produto: '))

elemento = 0
while elemento <= len ([1,2,3,4,5,6]):
    print('Estamos no elemento', elemento)
    elemento +=1

s= 'STRING'
indice = 0
while indice in range (len(s)):
    print('Estamos no elemento', s[indice])
    indice +=1    """

"""
palavra = 'tranquilo'
for indice, letra in enumerate(palavra):
    print(indice, letra)"""

"""s ="viva o python"
for ch in s:
    print("oi")"""

"""s = "viva o python"
for ch in s[3:8]:
    print("oi")"""


#faça um programa que peça 10 numeros inteiros, calcule e mostre a quantidade de numeros pares e a quantidade de numeros impar
impar=0
par=0
for num in range (1,11): 
    numeros_inteiros = int(input('Digite 10 numeros inteiros: '))
    if numeros_inteiros %2==0:
        par+=1
    else:
        impar+=1   
print('A quantidade de numeros par é: ',par)
print('A quantidade de numeros impar é:',impar)