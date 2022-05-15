contador=0
soma=0
while True:
    numero=int(input('Informe um número: '))
    if numero == 0:
        break
    soma=soma+numero
    contador=contador+1
print('Você digitou %d números' %contador)
print('A soma dos números é %d '%soma)
print(f'A média dos números digitado é: {soma/contador:.2f}')