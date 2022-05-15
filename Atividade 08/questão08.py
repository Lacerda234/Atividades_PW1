def procura_string(palavra, lista):
    if palavra in lista:
        return True
    else:
        return False

L = ['python', 'ADS', 'leandro', 'programação web']

print(procura_string('carro', L))
print(procura_string('leandro', L))
print(procura_string('programação web', L))
print(procura_string('cálculo', L))
print(procura_string('algoritmo', L))