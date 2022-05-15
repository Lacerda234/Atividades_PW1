numero=int(input('Informe um número: '))
if numero < 0:
    print('Número inválido, Informe apenas números positivos')
else:
    if numero>=1:
        print('2')
        p = 1
        y = 3
        while p < numero:
            x=3
            while(x<y):
                if y%x==0:
                    break
                x=x+2
            if x==y:
                print(x)
                p=p+1
            y=y+2