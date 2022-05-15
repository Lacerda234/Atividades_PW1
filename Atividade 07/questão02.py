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
terceira_lista=primeira_lista[:]
terceira_lista.extend(segunda_lista)
x=0
print('A terceira lista será: ')
while x<len(terceira_lista):
    print(f'{terceira_lista[x]}')
    x+=1