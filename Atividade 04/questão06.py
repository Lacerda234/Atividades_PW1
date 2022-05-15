materia1 = float(input('Informe a sua primeira nota: '))
materia2 = float(input('Informe a sua segunda nota: '))
materia3 = float(input('Informe a sua terceira nota: '))

media = (materia1+materia2+materia3)/3

if media >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')