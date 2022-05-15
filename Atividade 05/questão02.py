numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
menor = numero1
if numero2 < numero3 and numero2 < numero1:
    menor = numero2
if numero3 < numero2 and numero3 < numero1:
    menor = numero3
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")