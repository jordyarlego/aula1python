"""#1) verifique se uma letra digitada é vogal ou con

pergunta = input('Digite uma letra:')

if pergunta.lower() in 'aeiou':
    print('vogal')        
else:
    print('consoante')    
"""

"""#2)

preco1 = float(input('Digite o preço do primeiro produto:  '))
preco2 = float(input('Digite o preço do segundo produto:  '))
preco3 = float(input('Digite o preço do terceiro produto:  '))

if preco1 < preco2 and preco1 <preco3:
    print('você deve comprar o primeiro produto...')
elif preco2 < preco1 and preco2 < preco3:
    print('Você deve comprar o segundo produto...')
else:
    print('Você deve comprar o terceiro produto..')     """   

"""#3)

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Agora digite o o ultimo número: '))

numeros = [numero1, numero2, numero3]
numeros_decre = sorted(numeros, reverse = True)
print('Os numeros em ordem decrescente são: ', numeros_decre)"""


"""#4)

turnos =  input('Digite digite o turno que você estuda entre M = matutino V = vespetino  e N = noturno: ')

if turnos == "M":
    print('Bom dia!!!!!!')
elif turnos == "V":
    print('Boa tarde my friend kk!!')
elif turnos == "N":
    print ('Boa noite meu caro.. cuidado com os ladrões da cidade..')

else:
    print('Meu patrão, só pode escrever M V ou N.. me irrite não vá..')      """      

"""diasSemana = {
    1:'Segunda-feira',
    2: 'Terça-feira',
    3: 'quarta feira',4:'quinta-feira', 5:'sexta-feira', 6: 'sábado', 7:'domingo'
}

numeral = int(input('Digite um número de 1 a 7 e irá descobrir qual número da semana esse se refere: '))

if numeral in diasSemana:
    print(diasSemana[numeral])
else:
    print('Meu fi, escreva de 1 a 7, só isso, qual a dificuldade? aiai..')   """ 

#5.2)
"""nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if 9.0 <= media <10.0:
    conceito = "A"
elif 7.5 <= media <9.0:
    conceito="B"
elif 6.0 <= media < 7.5:
    conceito ="C"
elif 4.0 <= media < 6.0:
    conceito = "D"
elif 0<= media < 4.0:
    conceito = "E"
else:
    conceito = "conceito inválido"
if conceito in ['A', 'B', 'C']:
    situacao = 'APROVADO!'
else:
    situacao= "REPROVADO!"        
print ("média:", media , "e o Seu conceito foi de: ", conceito, "e você foi ", situacao)  """    


#6)

"""ano = int(input('Digite um ano: '))
if (ano %4 == 0 and ano %100 != 0) or (ano % 400 == 0):
    print(f'O ano{ano} é bissexto..')
else:
    print(f"o ano{ano} não é bissexto..")    """
#7)

"""numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input('Digite o segundo numero: '))

operacoes = input('Escolha a operação desejada (+, -,*,/,**): ')
if operacoes not in ['+', '-', '*', '/', '**']:
    print('operacao invalida')
resultado = eval(f'{numero1}',{operacoes}, {numero2})
#professora eu tive que pesquisar esse eval, pq eu n tava conseguindo fazer esse não..
par_impar = "par" if resultado % 2 ==0 else "impar"
positivo_negativo_zero = "positivo" if resultado > 0 else "negativo " if resultado < 0 else "zero"
inteiro_decimal = 'inteiro' if resultado.is_integer() else "decimal"
print(f"o resultado da operação é: {resultado}, e tbm é {par_impar}, e por incrivel que pareça ele é{inteiro_decimal}..")"""
#NAO CONSEGUI FAZER ESSE 7!!!!!!!!!!!!!!!!!
#8)

"""idade = int(input('Digite sua idade: '))
if 0<= idade <= 150:
    print(f'sua idade é de {idade}')
else:
    print('idade inválida meu caro..')  """

#9)       
"""num = []

for j in range(5):
    numero = float(input(f'digite o {j +1}º número: '))
    num.append(numero)
soma = 0
for numero in num:
    soma += numero
media = soma / len(num)

print(f'a soma dos numeros deu: {soma}')
print(f'a média dos numeros deu: {media}')"""

#10)
"""
pergunta = int(input('digite um numero inteiro: '))
if pergunta >1:
    for j in range(2, int(pergunta**0.5)+1):
        if pergunta % j ==0:
            print(f'{pergunta} não é um número primo..')
            #pq ta indo 2x? se eu colocar o break, da erro.. pelo menos tentei rs
        else:
          print(f'{pergunta} não é um número primo.')
else:
    print(f"{pergunta} não é um número primo.")            """


#11)

"""
temp = []

for j in range(5):
    temps = float(input(f'digite a temperatura {j+1}: '))
    temp.append(temps)

menor_temp = min(temp)
maior_temp = max(temp)

media_temps = sum(temp) / len(temp)

print(f'a menor temperatura é:  {menor_temp}')
print(f'a maior temperatura é: {maior_temp}')
print(f'a média das temperaturas é: {media_temps}')"""

#12)
"""saldo_medio = float(input("Digite o saldo médio do cliente: "))

if saldo_medio <= 200:
    print(f"Saldo médio: {saldo_medio:.2f}")
    print("Nenhum crédito disponível.")
elif saldo_medio <= 400:
    credito = saldo_medio * 0.2
    print(f"Saldo médio: {saldo_medio:.2f}")
    print(f"Seu crédito especial é de {credito:.2f}.")
elif saldo_medio <= 600:
    credito = saldo_medio * 0.3
    print(f"Saldo médio: {saldo_medio:.2f}")
    print(f"Seu crédito especial é de {credito:.2f}.")
else:
    credito = saldo_medio * 0.4
    print(f"Saldo médio: {saldo_medio:.2f}")
    print(f"Seu crédito especial é de {credito:.2f}.")"""

#13)

"""nome = input('diga o seu nome: ')
idade = int(input(f'{nome} quantos anos voce tem?? '))

ano = 2024
idade_max = 65
ano_aposentadoria = ano + (idade_max - idade)

print(f'{nome} voce podera se aposentar em {ano_aposentadoria}..')
"""

#14)

"""valor_hora = float(input("Qual o valor da sua hora de trabalho? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou neste mês? "))


salario_bruto = valor_hora * horas_trabalhadas

#prof eu sei que poderia ter feito uma lista aqui, ne
if salario_bruto <= 2112.00:
    porcentagem_ir = 0
elif salario_bruto <= 3751.05:
    porcentagem_ir = 0.075
elif salario_bruto <= 4664.68:
    porcentagem_ir = 0.225
else:
    porcentagem_ir = 0.275


desconto_ir = salario_bruto * porcentagem_ir


desconto_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11


salario_liquido = salario_bruto - desconto_ir - desconto_sindicato


print("\nFolha de Pagamento:")
print(f"Salário Bruto: R$ {salario_bruto:.2f}\n"
      f"Desconto do Imposto de Renda: R$ {desconto_ir:.2f}\n"
      f"Desconto do Sindicato: R$ {desconto_sindicato:.2f}\n"
      f"FGTS: R$ {fgts:.2f}\n"
      f"Salário Líquido: R$ {salario_liquido:.2f}")"""