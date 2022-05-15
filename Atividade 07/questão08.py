T=[-10,-8,0,1,2,5,-2,-4]
minima=T[0]
maxima=T[0]
soma=0
for k in T:
    if k<minima:
        minima=k
    if k>maxima:
        maxima=k
    soma=soma+k
print(f'Temperatura máxima: {maxima} °C')
print(f'Temperatura mínima: {minima} °C')
print(f'Temperatura média: {soma / len(T)} °C')