valor1 = int(input('Digite um número inteiro: '))
valor2 = int(input ('Digite outro número inteiro: '))

print(valor1 == valor2)
print(valor1 > valor2)
print(valor1 < valor2)
print(valor1 >= valor2)
print(valor1 <= valor2)

numero = 10
print(numero>0 and numero<10)
print(numero>0 or numero <10)

valor3 =int(input('Digite um número: '))

resto = valor3 % 2
if resto==0:
    print('o numero é par')
else:
    print('O numero é impar')    



cupom = input('Digite o cupom: ')
if (cupom == 'aula1' or cupom == 'aula2' ):
    print('Voce ganhou 10% de desconto')
else:
    print ('cupom invalido')

cupom = input ('Digite o cupom: ')
if(cupom == 'aula1' or 'aula2' ):
    print('Cupom válido, voce ganhou 15% de desconto')
else:
    print('voce errou o cupom mas ganhou 5% de desconto!')    