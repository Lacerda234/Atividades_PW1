expressao=input('Informe a sequência a ser validada: ')
x=0
pilha=[]
while x<len(expressao):
    if expressao[x] == "(":
        pilha.append("(")
    if expressao[x] == ")":
        if len(pilha)>0:
            topo=pilha.pop(-1)
        else:
            pilha.append(")")
            break
    x+=1
if len(pilha) == 0:
    print('OK')
else:
    print('Erro')