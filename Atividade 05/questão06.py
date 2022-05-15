valor = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário: '))
anos = int(input('Informe a quantidades de anos para pagar: '))
meses = anos * 12
prestacao = valor/meses
if prestacao > salario * 0.3:
    print('Desculpe, o empréstimo não pode ser aprovado')
else:
    print(f'Empréstimo aprovado, o valor das parcelas será: R${prestacao:.2f}')