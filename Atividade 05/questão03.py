salario = float(input('Qual o valor do seu salário?'))
aumento_maior = 0.15
aumento_menor = 0.10
if salario >=1 and salario <=1250:
    aumeto = salario * aumento_maior
    salario_acrescido = salario + aumeto
    print(f'Seu salário receberá um aumento de R${aumeto:.2f} e passará a ser de R${salario_acrescido:.2f}')
elif salario >1250:
    aumeto = salario * aumento_menor
    salario_acrescido = salario + aumeto
    print(f'Seu salário receberá um aumento de R${aumeto:.2f} e passará a ser de R${salario_acrescido:.2f}')