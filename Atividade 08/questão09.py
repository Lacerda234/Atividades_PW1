import random
n = random.randint(1,10)
tentativas = 3
while tentativas > 0:
    x = int(input('Escolha um número entre 1 e 10: '))
    if (x == n):
        print('Você acertou!')
        break
    elif (tentativas == 1):
        print('As tentativas acabaram, você perdeu!')
    else:
        print('Você errou!')
        print(f'Restam {tentativas-1} tentativas')
    tentativas -= 1