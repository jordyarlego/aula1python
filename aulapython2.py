#qual o ano do carro
#taxa de 1/100 antes de 1990
#taxa 1.5/100 depois de 1990
#pergunte o valor do carro:
"""anoCarro =int(input('Qual o ano do seu carro? '))
#pergunte o preço do carro:
precoCarro =float(input('Qual o valor do carro?'))
if anoCarro < 1990:
    print ('A taxa será de: ', precoCarro * 0.01)
else:
    print ('A taxa do seu carro será de: ', precoCarro * 0.015) """   

#Digite seu código
#pergunte o salario
#se ele não estiver entre os cargos, deverá receber um aumento de 40%
#mostre o salário antigo, o novo salário e a diferença

cargo=int(input("Digite o seu código de cargo: "))
salario=float(input('Digite o seu salário: '))

if cargo == 101:
    print('Seu salário é de ' , salario ,'Mas agora será de: ', salario + (salario * 0.1), 'Seu aumento salarial será de: ',(salario * 0.1))
elif cargo == 102:
    print ('Seu salário é de: ', salario, 'Mas agora será de: ', salario+ (salario * 0.2),'Seu aumento salarial será de: ',(salario * 0.2))
elif cargo == 103:
    print  ('Seu salário é de: ', salario, 'Mas agora será de: ', salario+ (salario * 0.3),'Seu aumento salarial será de: ',(salario * 0.3))
else:
    print  ('Seu salário é de: ', salario, 'Mas agora será de: ', salario+ (salario * 0.4), 'Seu aumento salarial será de: ',(salario * 0.4))



