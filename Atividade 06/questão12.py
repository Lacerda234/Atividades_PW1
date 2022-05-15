valor_divida=float(input('Informe o valor da dívida: '))
taxa_juros=float(input('Informe a taxa de juros: '))
pagamento=float(input('Informe o valor pago mensalmente: '))
mes=1
if (valor_divida * (taxa_juros/100) > pagamento):
    print('Sua dívida nunca será paga, pois os juros são maiores que o valor de pagamento!')
else:
    saldo=valor_divida
    juros_pago=0
    while saldo>pagamento:
        juros=saldo*taxa_juros/100
        saldo=saldo+juros-pagamento
        juros_pago=juros_pago+juros
        print(f'Saldo da dívida no mês {mes} é de R${saldo:.2f}')
        mes=mes+1
    print(f'Para pagar uma dívida de R${valor_divida:.2f}, a {taxa_juros:.0f}% de juros,')
    print(f'Você precisará de {mes-1} meses, pagando um total de R${juros_pago:.2f} de juros')
    print(f'No último mês você teria um saldo residual de R${saldo:.2f} a pagar')