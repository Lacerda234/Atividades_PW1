deposito_inicial=float(input('Informe o valor do depósito: '))
taxa_juros=float(input('Informe a taxa de juros: '))
deposito_mensal=float(input('Informe o valor do depósito mensal: '))
mes=1
saldo=deposito_inicial
while mes <=12:
    saldo=saldo+(saldo*(taxa_juros / 100))+deposito_mensal
    print(f'Saldo do mês {mes} é de R${saldo:.2f}')
    mes=mes+1
print(f'O ganho obtido com os juros foi de R${saldo-deposito_inicial:.2f}')