salario = float(input('Informe seu salário: '))
aumento = 15

if salario == 750:
    print(salario * (salario * aumento / 100))
else:
    print('Seu salário não terá acrescimo')