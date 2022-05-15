distancia = float(input('Informe a distância que deseja percorrer: '))
if distancia <= 200:
    passagem = 0.5 * distancia
else:
    passagem = 0.45 * distancia
print(f'Preço da passagem será: R${passagem:.2f}')