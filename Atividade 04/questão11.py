mercadoria = float(input('Informe o valor do produto: '))
porcentagem = float(input('Informe a porcentagem de desconto: '))

desconto = (mercadoria*porcentagem)/100
preco_final = mercadoria - desconto

print('O desconto foi de R$ %.2f e o produto custará R$ %.2f' %(desconto, preco_final))