class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print("CC N°%s Saldo: %10.2f" %(self.número, self.saldo))
        for cliente in self.clientes:
            print('Nome: %s\nTelefone: %s\n'%(cliente.nome, cliente.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            print('Saldo insuficiente!')

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0],o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)

leandro = Cliente('Leandro','9999-8888')
anne = Cliente('Anne','7777-4444')

conta = Conta([leandro, anne], 123, 4000)
conta.resumo()