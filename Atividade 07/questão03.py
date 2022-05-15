primeira_lista=[]
segunda_lista=[]
print('Vamos preencher a primeira lista,informe o valor 0 quando desejar parar.')
while True:
    l=int(input('Informe um número para a primeira lista: '))
    if l == 0:
        break
    primeira_lista.append(l)
print('Vamos preencher a segunda lista,informe o valor 0 quando desejar parar.')
while True:
    l=int(input('Informe um número para a segunda lista: '))
    if l == 0:
        break
    segunda_lista.append(l)
terceira_lista=[]
listas_unidas=primeira_lista[:]
listas_unidas.extend(segunda_lista)
x=0
while x<len(listas_unidas):
    k=0
    while k<len(terceira_lista):
        if listas_unidas[x] == terceira_lista[k]:
            break
        k+=1
    if k == len(terceira_lista):
        terceira_lista.append(listas_unidas[x])
    x+=1
x=0
print('A lista sem os elementos repetidos nas duas outras lista será: ')
while x<len(terceira_lista):
    print(f'{terceira_lista[x]}')
    x+=1