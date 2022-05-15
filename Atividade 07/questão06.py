L=[15,7,27,39]
p=int(input('Digite o primeiro número a procurar: '))
v=int(input('Digite o segundo númeoro a procurar: '))
x=0
achou_p=False
achou_v=False
primeiro=0
while x<len(L):
    if L[x] == p:
        achou_p=True
        if not achou_v:
            primeiro=1
    if L[x] == v:
        achou_v=True
        if not achou_p:
            primeiro=2
    x+=1
if achou_p:
    print('%d encontrado' % p)
else:
    print('%d não encontrado' % p)
if achou_v:
    print('%d encontrado' % v)
else:
    print('%d não encontrado' % v)
if primeiro == 1:
    print('O primeiro número foi achado antes do segundo')
elif primeiro == 2:
    print('O segundo número foi achado antes do primeiro')