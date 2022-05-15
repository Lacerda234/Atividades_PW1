def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None

L = [1,2,3,4,5]
print(pesquise(L,2))
print(pesquise(L,10))