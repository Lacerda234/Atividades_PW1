total=0
while True:
    codigo=int(input('Informe o código do produto: '))
    preco=0
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print('Código inválido')
    if preco != 0:
        quantidade=int(input('Informe a quantidade comprada: '))
        total=total+(preco*quantidade)
print(f'O total das compras foi de R${total:.2f}')