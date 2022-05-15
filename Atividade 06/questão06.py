tabuada=int(input('Tabuada de:'))
inicio=int(input('Iniciando a partir de:'))
fim=int(input('Finalizando em:'))
numero=inicio
while numero <=fim:
    print(f'{tabuada} X {numero} = {tabuada * numero}')
    numero+=1