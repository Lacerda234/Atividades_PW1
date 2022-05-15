consumo = int(input('Informe o consumo em KWh: '))
tipo = input('Informe qual o tipo de instalação (residencial, comercial ou industrial): ')
if tipo == "residencial":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "industrial":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "comercial":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print('Operação inválida')
custo = consumo * preco
print(f'O valor a pagar será: R${custo:.2f}')