numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro número: '))
operacao = input('Informe qual operação deseja realizar (+, -, * ou /) ')
if operacao == "+":
    resultado = numero1+numero2
    print(f'O resultado é: {numero1:.0f} + {numero2:.0f} = {resultado:.0f}')
elif operacao == "-":
    resultado = numero1-numero2
    print(f'O resultado é: {numero1:.0f} - {numero2:.0f} = {resultado:.0f}')
elif operacao == "*":
    resultado = numero1*numero2
    print(f'O resultado é: {numero1:.0f} x {numero2:.0f} = {resultado:.0f}')
elif operacao == "/":
    resultado = numero1/numero2
    print(f'O resultado é: {numero1:.0f} / {numero2:.0f} = {resultado}')
else:
    print('Operação inválida')