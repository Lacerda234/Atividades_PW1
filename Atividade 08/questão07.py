def valida_string(palavra, minimo, maximo):
    tamanho = len(palavra)
    return minimo <= tamanho <= maximo

print(valida_string('leandro', 1, 7))
print(valida_string('programação', 2, 5))
print(valida_string('python', 3, 8))