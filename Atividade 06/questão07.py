primeiro=int(input('Informe o primeiro número: '))
segundo=int(input('Informe o segundo número: '))
x=1
resultado=0
while x <= segundo:
    resultado = resultado+primeiro
    x = x + 1
print(f'{primeiro} X {segundo} = {resultado}')