def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

while True:
    print("+=================+")
    print("| MENU DE OPERAÇÕES")
    print("| 1 - somar        ")
    print("| 2 - subtrair     ")
    print("| 3 - multiplicar  ")
    print("| 4 - dividir      ")
    print("| 0 - sair         ")
    print("+=================+")

    op = int(input())
    if op == 0:
        break

    n1 = int(input("primeiro numero: "))
    n2 = int(input("segundo numero: "))

    if op == 1:
        print("O resultado da soma é:", soma(n1, n2))
    elif op == 2:
        print("O resultado da subtração é:", subtrai(n1, n2))
    elif op == 3:
        print("O resultado da multiplicação é:", multiplica(n1, n2))
    elif op == 4:
        print("O resultado da divisão é:", divide(n1, n2))
    elif op == 5:
        break