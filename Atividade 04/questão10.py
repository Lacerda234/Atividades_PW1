salario = float(input('Informe seu salário: '))
porcentagem = float(input('Informe a porcentagem do aumento: '))

novo_salario = salario + ((salario*porcentagem)/100)
aumento = novo_salario - salario

print('O aumento foi de R$ %.2f e seu novo salário será de R$ %.2f' %(aumento, novo_salario))