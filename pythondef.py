"""def funcaoLeitura():
    for num in [1,2,3,4,5]:
        print("Numero" , num)


def funcaoLeitura():
    for num in range (S):
        print("numero" , num)


def addNum (n1, n2):
    print("O primeiro numero é: ", n1)
    print("O segundo numero é: ", n2)
    print("A soma numero é: ", n1+n2)

varGlobal = 10
def multiplicacao (num1, num2):
    varGlobal =(num1 * num2)
    print ("variavel da funcao mutiplica: ", varGlobal)
    multiplicacao (5,4)
    print(varGlobal)




varGlobal=10
def multiplicacao (num1, num2):
    varLocal=(num1 * num2)
    print("variavel da função multiplica: ", varLocal)
    print(varLocal)  

def separarTexto (texto):
    return texto.split()
    


separarTexto ("cibele maria suely")

def variosParametros(*parametros):
    for n, item in enumerate (parametros):
        print("parametro", n, item)
    return

variosParametros("cibele", "suely", "giggio", "mada", "luquinhas")

variosParametros("pitomba", "jambo", "siriguela", "umbu")"""


def soma (n1,n2):
    return n1+n2
def subitrai(n1,n2):
    return n1-n2
def multiplicacao(n1,n2):
    return n1 * n2
def divide (n1,n2):
    return n1/n2

while True:
    print("+=======================+")
    print("| MENU DE OPERAÇÕES     | ")
    print("| 1 - somar             | ")
    print("| 2 - subtrair          |")
    print("| 3- multiplicar        | ")
    print("| 4- Dividir            | ")
    print("| 0- Sair               | ")
    print("+=======================+")

    op = int(input())
    if op ==0:
     break
    n1= int(input("primeiro número: "))
    n2 = int(input("Segundo numero: "))

    if op ==1:
        print("o resultado da some é: ", soma (n1,n2))
    elif op ==2:
        print("o resultado da subtracao é: "), subitrai(n1,n2)
    elif op ==3:
        print("o resultado da multiplicacao é: ") , multiplicacao(n1,n2)
    elif op ==4:
        print("o resultado da divisao é: "), divide(n1,n2)
    elif op ==5:
        break    
