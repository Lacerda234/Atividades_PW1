km = int(input('Informe a quantidade de quilometros percorridos: '))
dias = int(input('Informe quantos dias você ficou com o carro: '))

preco_por_dia = 60
preco_por_km = 0.15
preco_final = km * preco_por_km + dias * preco_por_dia

print('Total a pagar será R$ %.2f'%preco_final)