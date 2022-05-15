L=[15,7,27,39]
p=int(input('Digite o primeiro número a procurar: '))
v=int(input('Digite o segundo númeoro a procurar: '))
x=0
achou_p=-1
achou_v=-1
primeiro=0
while x<len(L):
    if L[x] == p:
        achou_p=x
    if L[x] == v:
        achou_v=x
    x+=1
if achou_p != -1:
    print('%d encontrado na posição %d' %(p,achou_p))
else:
    print('%d não encontrado' %p)
if achou_v != -1:
    print('%d encontrado na posição %d' %(v,achou_v))
else:
    print('%d não encontrado' %v)
if achou_p != -1 and achou_v != -1:
    if achou_p <= achou_v:
        print('O primeiro número foi achado antes do segundo')
    else:
        print('O segundo número foi achado antes do primeiro')