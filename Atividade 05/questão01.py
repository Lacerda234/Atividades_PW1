velocidade = int(input('Informe a sua velocidade: '))
if velocidade>= 0 and velocidade <=80:
    print('Velocidade dentro do limite')
else:
    print(f'Velocidade acima do limite, será multado em R${(velocidade-80)*5}')